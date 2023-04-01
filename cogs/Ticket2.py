import discord
from discord.ext import commands
import json
from utilities.Tools import*
class invtracker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:tic:1017405527183065158>'
		      label = "Tickets"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def Ticket(self, ctx: commands.Context):
            embed=discord.Embed(title="**Ticket**", description=""""``` sendpanel ・ adduser ・ ticdelete ・ close```""",color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
  

def setup(bot):
    bot.add_cog(invtracker(bot))