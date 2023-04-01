from discord.ext import commands
from utilities.Tools import *
import discord, psutil, pathlib, shutil, os, sys
from discord.ui import View, Button
from typing import Optional
from discord.ext.commands import Cog
import asyncio
def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def get_ram_total():
    return int(psutil.virtual_memory().total)


class Extra(Cog):
  """Some extra commands which can't be listed in Moderation group are listed here."""
  def __init__(self, client):
    self.client = client




    
  @commands.command(aliases=['shard', 'bi'], help="Check information about bot")
  @blacklist_check()
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _info(self, ctx):
    author = ctx.message.author
    shards_guilds = {i: {"guilds": 0, "users": 0} for i in range(len(self.client.shards))}
    for guild in self.client.guilds:
            shards_guilds[guild.shard_id]["guilds"] += 1
            shards_guilds[guild.shard_id]["users"] += guild.member_count

    p = pathlib.Path('./')
    imp = cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
            if str(f).startswith("venv"):
                continue
            fc += 1
            with f.open() as of:
                for l in of.readlines():
                    l = l.strip()
                    if l.startswith('class'):
                        cl += 1
                    if l.startswith('def'):
                        fn += 1
                    if l.startswith('import'):
                        imp += 1
                    if l.startswith("from"):
                        imp += 1
                    if l.startswith('async def'):
                        cr += 1
                    if '#' in l:
                        cm += 1
                    ls += 1

    total, used, free = shutil.disk_usage("/")

    embed=discord.Embed(title="**Soward Stats**",color=0xFF1B1B, timestamp=ctx.message.created_at)
    embed.add_field(name=f"Basic Information", value=f"""```
guilds: {len(self.client.guilds):,}
users: {len(self.client.users):,}
Commands: {len(set(self.client.walk_commands()))}
Shards: {len(self.client.shards)}```""", inline=True)
    embed.add_field(name=f"**System**", value=f"""```
PID: {os.getpid()}
CPU: {round(psutil.cpu_percent())}%/100%
RAM: {int((psutil.virtual_memory().total - psutil.virtual_memory().available)
 / 1024 / 1024)}MB/{int((psutil.virtual_memory().total) / 1024 / 1024)}MB
Disk: {used // (2 ** 30)}GB/{total // (2 ** 30)}GB
Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}```""", inline=True)

    for shard_id, shard in self.client.shards.items():
            embed.add_field(name=f"**Shard id #{shard_id}**", value=f"""```
Latency: {round(shard.latency * 1000)}ms{' ' * (9 - len(str(round(shard.latency * 1000, 3))))}
Guilds: {shards_guilds[shard_id]['guilds']:,}
Users: {shards_guilds[shard_id]['users']:,}
            ```""", inline=True)
            embed.set_author(name=ctx.author, icon_url=author.display_avatar.url)
            embed.set_thumbnail(url=self.client.user.avatar)
            embed.set_footer(text=f"Requested by{ctx.author}",icon_url=ctx.author.display_avatar.url)
            b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=1004248513435152484&permissions=8&scope=bot')
            b2 = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/zenox-5355/upvote#goog_rewarded')
            b3 = Button(label='support', style=discord.ButtonStyle.link,url='https://discord.gg/q8es72uZ7X')
            view = View()
            view.add_item(b)
            view.add_item(b2)
            view.add_item(b3)

    await ctx.channel.trigger_typing()
    await asyncio.sleep(3)
    await ctx.send(embed=embed, view=view)
  
  



def setup(bot):
    bot.add_cog(Extra(bot))