import discord
from discord.ext import commands
import json
from utilities.Tools import*
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:utility:1017405604987404408>'
		      label = "utility"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def Utility(self, ctx: commands.Context):
            embed=discord.Embed(title="**Utility**", description="```ar-create • ar-edit • ar-delete • ar show • calculate ・ Suggestions<sg> ・ report ・ vcdeafen ・ vcundeafen ・ vcmute ・ vcunmute ・ emoji-add ・ emoji-delete ・ createrole<name> ・ deleterole <name> ・ rename <role> <new name> ・ color <role> <color> ・ cnuke ・ hackban ・ timer```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
  

def setup(bot):
    bot.add_cog(Utility(bot))