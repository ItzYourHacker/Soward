import discord
from discord.ext import commands
import json
from utilities.Tools import *
class j2c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:voice:1017402454159147039>'
		      label = "Join to create"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def Join2create(self, ctx: commands.Context):
            embed=discord.Embed(title="Join2Create", description="""``` voice setupj2c ・ voice claim ・ voice lock ・ voice unlock ・ voice permit <user> ・ voice reject <user> ・ voice name <name> ・ voice limit ( ex. 1-2-3)```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
  

def setup(bot):
    bot.add_cog(j2c(bot))