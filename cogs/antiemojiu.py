import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
#from core import Soward
import threading
import datetime
import logging
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
from utilities.Tools import *
from discord.ext.commands import Cog
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antiemojiu(Cog):
    def __init__(self, client):
        self.client = client      
        self.headers = {"Authorization": f"Bot MTAwNDI0ODUxMzQzNTE1MjQ4NA.Gn9shC.zvlZHy1KrvCKB0m4WXjBBB9XvGmBzHBN3Tvcy4"}
        print("Cog Loaded: Antiemojiu")
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after) -> None:
      try:
        data = getConfig(guild.id)
        anti = getanti(guild.id)
        punishment = data["punishment"]
        wled = data["whitelisted"]
        reason = "Soward | Updating Emojis Not Whitelisted"
        async for entry in guild.audit_logs(limit=1):
            user = entry.user.id
        api = random.randint(8,9)
        if user == 980361546918162482:
          pass
        elif entry.user == guild.owner:
          pass
        elif str(entry.user.id) in wled or anti == "off":
            pass
        else:
         if entry.action == discord.AuditLogAction.emoji_update:
           async with aiohttp.ClientSession(headers=self.headers) as session:
            if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    if r.status in (200, 201, 204):
                      logging.info("Successfully banned %s" % (user))
            elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if r2.status in (200, 201, 204):
                               logging.info("Successfully kicked %s" % (user))
            elif punishment == "none":
              mem = guild.get_member(entry.user.id)
              await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
            else:
                       return
      except Exception as error:
            if isinstance(error, discord.Forbidden):
              return
def setup(bot):
    bot.add_cog(antiemojiu(bot))