import discord
from discord.ext import commands
import json
#from utilities.Tools import *
from utilities.Tools import*
class games67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Game commands"""

  
    def help_custom(self):
		      emoji = '<a:sgames:1017404466833657918>'
		      label = "Games"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    @blacklist_check()
    async def Games(self, ctx: commands.Context):
            embed=discord.Embed(title="**Games**", description="""``` fight ・ Findimposter ・ Rps ・ Hangman ・ TicTacToe ・ blackjack ・ truth ・ dare ・ typerace```""",color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
       

def setup(bot):
    bot.add_cog(games67(bot))