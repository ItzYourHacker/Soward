#Made By Rao

from logging import basicConfig, INFO
from bot import Bot
import os
from webserver import keep_alive
import json
from discord.ext import commands
import discord
TOKEN = "MTAyOTAwOTk5MDY5MTg1MjMwOA.G6TeI8.JecmTbAHd9j-EQtDEi6DzGmEQhYkHxFvaOHGlM" #your bot's token here
bot = Bot()
basicConfig(level=INFO)
@bot.command(name="autorole-bot-add")
@commands.has_permissions(administrator=True)
async def botautoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    return
  if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You can't use roles with administrator in autoroles.", color=0xFF1B1B))
          return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['botautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is already set in autoroles.", color=0xFF1B1B))
      return
    else:
      ff[str(ctx.guild.id)]['botautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="successfully Added Bot autoroles.",color=0xFF1B1B))
            

keep_alive()
if __name__ == '__main__':
   bot.run(TOKEN, reconnect=True)