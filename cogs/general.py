import time
import discord
import logging
import requests
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color
from utilities.Tools import*

logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour.green()
        self.connection = mongodb.AsyncIOMotorClient(
            "mongodb+srv://hacker:chetan2004@secure.9rv0s.mongodb.net/secure?retryWrites=true&w=majority"
        )
        self.db = self.connection["secure"]["servers"]




    

    @commands.group(name="emoji",
                      description="Shows emoji syntax",
                      usage="emoji [emoji]")
    @blacklist_check()
    async def emoji(self, ctx, emoji: discord.Emoji):
        return await ctx.send(
            embed=discord.Embed(title="emoji",
                                description="emoji: %s\nid: **`%s`**" %
                                (emoji, emoji.id),
                                color=0xFF1B1B))

    @commands.group(name="user",
                      description="Shows user syntax",
                      usage="user [user]")
    @blacklist_check()
    async def user(self, ctx, user: discord.Member = None):
        return await ctx.send(
            embed=discord.Embed(title="user",
                                description="user: %s\nid: **`%s`**" %
                                (user.mention, user.id),
                                color=0xFF1B1B))

    @commands.group(name="role",
                      description="Shows role syntax",
                      usage="role [role]")
    @blacklist_check()
    async def role(self, ctx, role: discord.Role):
        return await ctx.send(
            embed=discord.Embed(title="role",
                                description="role: %s\nid: **`%s`**" %
                                (role.mention, role.id),
                                color=0xFF1B1B))

    @commands.group(name="channel",
                      description="Shows channel syntax",
                      usage="channel [channel]")
    @blacklist_check()
    async def channel(self, ctx, channel: discord.TextChannel):
        return await ctx.send(
            embed=discord.Embed(title="channel",
                                description="channel: %s\nid: **`%s`**" %
                                (channel.mention, channel.id),
                                color=0xFF1B1B))

    @commands.group(name="boosts",
                      description="Shows boosts count",
                      usage="boosts",
                      aliases=["bst"])
    @blacklist_check()
    async def boosts(self, ctx):
        await ctx.send(
            embed=discord.Embed(title="boosts",
                                description="**`%s`**" %
                                (ctx.guild.premium_subscription_count),
                                color=0xFF1B1B))

    @commands.group(name="emoji-add",
                      description="Adds a emoji",
                      usage="emoji-add [emoji]",
                      aliases=["eadd"])
    @commands.has_permissions(manage_emojis=True)
    @blacklist_check()
    async def steal(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url)
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name,
                                                                image=img)
                    return await ctx.send(
                        embed=discord.Embed(title="",
                                            description="added \"**`%s`**\"!" %
                                            (emote),
                                            color=0xFF1B1B))
                except Exception:
                    return await ctx.send(
                        embed=discord.Embed(title="",
                                            description=f"failed to add emoji",
                                            color=0xFF1B1B))
            else:
                return await ctx.send(
                    embed=discord.Embed(title="",
                                        description=f"invalid emoji",
                                        color=0xFF1B1B))
        except Exception:
            return await ctx.send(
                embed=discord.Embed(title="",
                                    description=f"failed to add emoji",
                                    color=0xFF1B1B))

    @commands.group(name="emoji-delete",
                      description="Deletes a emoji",
                      usage="emoji-delete [emoji]",
                      aliases=["edel"])
    @commands.has_permissions(manage_emojis=True)
    @blacklist_check()
    async def deleteemoji(self, ctx, emote: discord.Emoji):
        return await ctx.send(
            embed=discord.Embed(title="emoji-delete",
                                description="deleted \"**`%s`**\"!" % (emote),
                                color=0xFF1B1B))

def setup(bot):
    bot.add_cog(general(bot))
