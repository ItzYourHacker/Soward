import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
from .utils.config import *
import io
import textwrap
import json
import datetime
import sys
import jishaku
from discord.ui import Button, View
import psutil
import time
import platform
from utilities.Tools import *



class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.load_extension('jishaku')
        jishaku.Flags.NO_DM_TRACEBACK = True
        jishaku.Flags.NO_UNDERSCORE = True
  
    @commands.group(name='eval', invoke_without_command=True)
    @commands.is_owner()
    async def _infinity(self, ctx: commands.Context):
        guilds = len(self.bot.guilds)
        users = len(set(self.bot.get_all_members()))
        channels = len(set(self.bot.get_all_channels()))
        owner = self.bot.get_user(self.bot.owner_ids[0])
        em = discord.Embed(title=' Eval', description=f' discord.py `{discord.__version__}`\n python version {sys.version}\n **{guilds}** guilds\n **{users}** users\n **{channels}** channels', color=0xFF1B1B)
        em.set_footer(text=f'{owner}', icon_url=owner.avatar)
        await ctx.send(embed=em)
        
    @_infinity.command(aliases=['python'])
    @commands.is_owner()
    async def py(self, ctx: commands.Context, *, code):
        code = clean_code(content=code)
        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": self.bot,
            "ctx": ctx,
            "message": ctx.message,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "self": self,
        }

        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '   ')}", local_variables
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        await ctx.send(f'```py\n{result}\n```')

    @_infinity.command(aliases=['reload'])
    @commands.is_owner()
    async def _reload(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to reload {cog}\n Error: {e}")
    
    @_infinity.command(aliases=['load'])
    @commands.is_owner()
    async def _load(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.load_extension(cog)
            await ctx.send(f"Loaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to load {cog}\n Error: {e}")
    
    @_infinity.command(aliases=['unload'])
    @commands.is_owner()
    async def _unload(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            await ctx.send(f"Unloaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to unload {cog}\n Error: {e}")

    @_infinity.command(aliases=['dbg'])
    async def debug(self, ctx: commands.Context, *, command: str):
        command = self.bot.get_command(command)
        
        if command is None:
            await ctx.send("Command not found")
            return
        
        try:
            await ctx.invoke(command)
        except Exception as e:
            await ctx.send(f"```py\n{e.__traceback__}\n```")


    @commands.command(name="stats", aliases=["statistics", "st"], usage='stats', brief='.stats')
    @blacklist_check()
    async def hestatsha(self, ctx):
        """Shows some usefull information about PyBot"""
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        # revision = self.get_last_commits()
 
        total_memory = psutil.virtual_memory().total >> 20
        used_memory = psutil.virtual_memory().used >> 20
        cpu_used = str(psutil.cpu_percent())
 
 
        total_members = sum(g.member_count for g in self.bot.guilds if g.member_count != None)
        cached_members = len(self.bot.users)
 
        b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=1004248513435152484&permissions=8&scope=bot')
        view = View()
        view.add_item(b)
        b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/zenox-5355/upvote#goog_rewarded')
        b2 = Button(label='invite me', style=discord.ButtonStyle.link,url='https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=1101052116095&scope=applications.commands%20bot')
        b3 = Button(label='support', style=discord.ButtonStyle.link,url='https://discord.gg/q8es72uZ7X')
        view = View()
        view.add_item(b)
        view.add_item(b2)
        view.add_item(b3)
 
        embed = discord.Embed(colour=0xFF1B1B)
 
         #start_time = calendar.timegm(time.strptime(start_time.strftime("%Y-%m-%d %H:%M:%S+00:00"), '%Y-%m-%d %H:%M:%S+00:00'))
 
        embed.add_field(name=' Servers', value=f'```{serverCount} Total\n{len(self.bot.shards)} Shards```')
        embed.add_field(name='Members', value=f'```{total_members} - Total```')
        embed.add_field(name="System", value=f"```RAM: {used_memory}/{total_memory} MB```\n```CPU: {cpu_used}% used.```"),
        embed.add_field(name='Version', value=f'```Python - {pythonVersion}\nDiscordpy - {dpyVersion}```')
        embed.add_field(
            name="ping",
            value=f"``` {round(self.bot.latency * 1000, 2)}ms```")
        # embed.add_field(name="System", value=f"**RAM**: {used_memory}/{total_memory} MB\n**CPU:** {cpu_used}% used.", inline=False),
        # embed.add_field(name='Version', value=f'Python - {pythonVersion}\nDiscordPY - {dpyVersion}', inline=False)
        prince = await self.bot.fetch_user(1018139793789563000)
        if prince in ctx.guild.members:
            a = f'{prince.mention}'
        else:
            a = f'{prince}'
        embed.add_field(name=' Bot Developers:', value=f"<@1018139793789563000>, <@940973004647718912>")
        embed.add_field(name='special thanks', value=f"```   ~ PЯΛΠΛѴ  .ゞ..ꨄ🥀  , VŁG丶Thory```")

        embed.set_author(name=f"{self.bot.user.name} Stats", icon_url=self.bot.user.display_avatar.url)
 
 
        embed.set_footer(text='Made with love <3')
        embed.set_image(url="")
 
        await ctx.send(embed=embed, view=view)


def setup(bot):
    bot.add_cog(owner(bot))