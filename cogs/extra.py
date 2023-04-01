import discord
from discord.ext import commands
import json

class lamaoded1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:orbs:1038494668821901373>'
		      label = "Extra"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    async def extra(self, ctx: commands.Context):
            embed=discord.Embed(title="**Extra**", description="""**Setup**```\n setup-friend ・ setup-vip ・ setup-guest ・ setup-official ・ setup-girl ・ setup-bot ・ setup-mod ・ setup-artist```\n\n**For remove**```\nrfriend ・ rvip ・ rguest ・ rofficial ・ rgirl ・ rmod ・ rbot ・ rartist``` \n\n**For view setup**```\nconfig-setup```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
  
  

def setup(bot):
    bot.add_cog(lamaoded1(bot))