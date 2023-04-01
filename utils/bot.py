import motor.motor_asyncio as motor
import time
import os
os.system("pip install git+https://github.com/Nirlep5252/discord.py")
import re
import discord
import aiohttp
import sys
import jishaku
import traceback
from discord.ext import commands, tasks
from pymongo import UpdateOne
from utils.embed import success_embed
from utils.ui import DropDownSelfRoleView, ButtonSelfRoleView



OWNERS = [
  1018139793789563000
]
#add owner's id above

MONGO_URL = "mongodb+srv://PRINCE123:nxtontop@cluster0.wr5qth2.mongodb.net/?retryWrites=true&w=majority"

class Bot(commands.AutoShardedBot):
    def __init__(self, beta: bool = False):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            owner_ids=OWNERS,
            command_prefix='-',
            intents=intents,
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False, roles=False),
            strip_after_prefix=True,
            help_command=None,
            cached_messages=10000,
            activity=discord.Activity(type=discord.ActivityType.playing, name="$help"),
            shard_count=1  # remove this if your bot is under 1000 servers
        )
        cluster = motor.AsyncIOMotorClient(MONGO_URL)
        self.session = aiohttp.ClientSession()

        self.cache_loaded = False
        self.cogs_loaded = False
        self.rolemenus_loaded = False

        self.db = cluster['Rbot']

        self.self_roles = self.db['self_roles']

        self.welcome = self.db['welcome']

        # i'm gonna fill these up with my cu- i mean cache!


        if not self.cogs_loaded:
            self.load_extension('jishaku')
            print("Loaded jsk!")
            self.loaded, self.not_loaded = self.loop.run_until_complete(self.load_extensions('./cogs'))
            self.loaded_hidden, self.not_loaded_hidden = self.loop.run_until_complete(self.load_extensions('./cogs_hidden'))
            self.cogs_loaded = True


    async def load_extensions(self, filename_):
        loaded = []
        not_loaded = {}
        i = 0
        total = 0
        for filename in os.listdir(filename_):
            if filename.endswith('.py'):
                total += 1
                h = f'{filename_[2:]}.{filename[:-3]}'
                try:
                    self.load_extension(h)
                    loaded.append(h)
                    i += 1
                except Exception as e:
                    not_loaded.update({h: e})
        print(f"Loaded {i}/{total} extensions from {filename_}")
        return loaded, not_loaded

    async def load_rolemenus(self, dropdown_view, button_view):
        i = 0
        cursor = self.self_roles.find({})
        h = await cursor.to_list(length=None)
        for amogus in h:
            guild = self.get_guild(amogus['_id'])
            if guild is not None:
                role_menus = amogus['role_menus']
                for msg_id, menu in role_menus.items():
                    if menu['type'] == 'dropdown':
                        self.add_view(dropdown_view(guild, menu['stuff']), message_id=int(msg_id))
                        i += 1
                    if menu['type'] == 'button':
                        self.add_view(button_view(guild, menu['stuff']), message_id=int(msg_id))
                        i += 1
        self.rolemenus_loaded = True

        print(f"Self role views has been loaded. | {i} views")

    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        await self.process_commands(message)


    async def on_ready(self):

        if not self.rolemenus_loaded:
            await self.load_rolemenus(DropDownSelfRoleView, ButtonSelfRoleView)
            print("Reaction view has been loaded.")

        print(f"Logged in as {self.user}")
        print(f"Connected to: {len(self.guilds)} guilds")
        print(f"Connected to: {len(self.users)} users")
        print(f"Connected to: {len(self.cogs)} cogs")
        print(f"Connected to: {len(self.commands)} commands")
        print(f"Connected to: {len(self.emojis)} emojis")
        print(f"Connected to: {len(self.voice_clients)} voice clients")
        print(f"Connected to: {len(self.private_channels)} private_channels")

        embed = success_embed(
            "Bot is ready!",
            f"""
    **Loaded cogs:** {len(self.loaded)}/{len(self.loaded) + len(self.not_loaded)}
    **Loaded hidden cogs:** {len(self.loaded_hidden)}/{len(self.loaded_hidden) + len(self.not_loaded_hidden)}
            """
        )
        if self.not_loaded:
            embed.add_field(
                name="Not loaded cogs",
                value="\n".join([f"`{cog}` - {error}" for cog, error in self.not_loaded.items()]),
                inline=False
            )
        if self.not_loaded_hidden:
            embed.add_field(
                name="Not loaded hidden cogs",
                value="\n".join([f"`{cog}` - {error}" for cog, error in self.not_loaded_hidden.items()]),
                inline=False
            )
        webhook = self.get_channel()
        await webhook.send(embed=embed)