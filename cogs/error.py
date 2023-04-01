import discord
import json
from discord.ext import commands
from discord.ui import Button, View
from .utils.config import *
#from core.Soward import Soward
from core import Context
class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

      


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      with open('blacklist.json', 'r') as f:
        data = json.load(f)
      if isinstance(error, commands.MissingPermissions):
        missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
        ]
        if len(missing) > 2:
                      fmt = "{}, and {}".format(", ".join(missing[:-1]), missing[-1])
        else:
                      fmt = " and ".join(missing)
        #              await ctx.reply(f"You don't have `{fmt}` permission(s) to run `{ctx.command.name}` command!")
      elif isinstance(error, commands.BotMissingPermissions):
              missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
        ]
              if len(missing) > 2:
                      fmt = "{}, and {}".format(", ".join(missing[:-1]), missing[-1])
              else:
                      fmt = " and ".join(missing)
                      await ctx.reply(f"i don't have `{fmt}` permission(s) to run `{ctx.command.name}` command!")  
      elif isinstance(error, commands.CheckFailure):
       if str(ctx.author.id) in data["ids"]:
        embed = discord.Embed(title="<a:Error:1018257469274861688>", description="you Are blacklisted from using my commands!", color=discord.Colour(0x2f3136))
        await ctx.reply(embed=embed, mention_author=False)
    #  if ctx.command.name.lower() in ['Rb', 'leaveg', 'removebadge', 'addb', 'bremove', 'bl']:
     #   await ctx.reply(embed=discord.Embed(title="you do not own this bot", color=0x2f3136))

    @commands.Cog.listener()
    async def on_message(self, message):
    
      with open("prefixes.json", "r") as f:
       idk = json.load(f)
      if str(message.guild.id) in idk:
          idkprefix = idk[str(message.guild.id)]
      if str("<@1004248513435152484>") in message.content:

          b2 = Button(label='support', style=discord.ButtonStyle.link, url='https://dsc.gg/meta-development')
          view = View()
        #  view.add_item(b)
          view.add_item(b2)
          author = message.author
          embed = discord.Embed(title='**Soward**', description=f'**If you like Soward, Consider [voting](https://discordbotlist.com/bots/zenox-5355/upvote) or [inviting](https://dsc.gg/soward) it to your server! Thank you for using Soward, we hope you enjoy it, as we always look forward to improve the bot\n\n   To view my commands user `{idkprefix}help` You can change my prefix using `{idkprefix}setprefix <new prefix>**', color=0x2f3136)
          embed.set_thumbnail(url=author.display_avatar.url)
          await message.channel.send(embed=embed, view=view)

             
        

def setup(bot):
    bot.add_cog(errors(bot))