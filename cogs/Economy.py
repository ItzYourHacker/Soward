import discord
from discord.ext import commands
import json
from utilities.Tools import*
class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:cash:1017403803726778409>'
		      label = "Economy"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def economy(self, ctx: commands.Context):
            embed=discord.Embed(title="**economy**", description="""```Bal ・ dep ・ with ・ Rob ・ Slots ・ Shop ・ Buy ・ Sell ・ Beg ・ Work ・ Rich ・ Send ```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
  
  

def setup(bot):
    bot.add_cog(economy(bot))