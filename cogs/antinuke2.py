import discord
from discord.ext import commands
import json
from utilities.Tools import *
class antinuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:security:1017403300972331108>'
		      label = "Antinuke"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def antihe(self, ctx: commands.Context):
    embed=discord.Embed(title="Antinuke", description="""```Antinuke enable/disable ・ Antinuke config ・ features ・ whitelist add・ whitelist remove・ whitelist show ・ whitelist reset ・ channelclean ・ roleclean ・ recover ・ punishment set ・ punishment show```""", color=0xFF1B1B)
    embed.set_thumbnail(url=self.bot.user.avatar)
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
        await ctx.reply(embed=embed)
  

def setup(bot):
    bot.add_cog(antinuke(bot))