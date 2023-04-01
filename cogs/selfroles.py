import discord
from discord.ext import commands
import json
from utilities.Tools import *
class selfrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Game commands"""

  
    def help_custom(self):
		      emoji = '<a:bolt:1018057711251902494>'
		      label = "Autoroles"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def Autorole(self, ctx: commands.Context):
            embed=discord.Embed(title="**Autorole**",description="``` autorole-human-add ・ autorole-human-remove ・ autorole-bot-add ・ autorole-bot-remove ・ autoroles-config ・ verification <channel> <role>```",color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
       

def setup(bot):
    bot.add_cog(selfrole(bot))