import discord
from discord.ext import commands
import json
from utilities.Tools import *
class welcome2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<a:welcome:1017405722226610247>'
		      label = "Welcome"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def welcomes(self, ctx: commands.Context):
            embed=discord.Embed(title="**Autorole**",description="```greet <msg> (use $$MM$$ in greet msg for member mention) ・ stopgreet ・ welcome enable ・ welcome disable ・ welcome channel ・ welcome test ・ welcome message ・ welcome embed ・ welcome title ・ welcome description ・ welcome thumbnail ・ welcome footer\n\n Welcome variables ・ {user.name} ・ {user.mention} ・ {user.id} ・ {user.tag} ・ {server.name} ・ {server.membercount}```",color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_footer(text="Made By Abhi", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)


  

def setup(bot):
    bot.add_cog(welcome2(bot))