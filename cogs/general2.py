import discord
from discord.ext import commands
import json
from utilities.Tools import*

class general67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""  

    def help_custom(self):
		      emoji = '<:icons8discorde64:1017404784900325406>'
		      label = "General"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.command()
    @blacklist_check()
    async def General(self, ctx: commands.Context):
            embed=discord.Embed(title="**General**""", description="```steal ・ afk ・ nick ・ clearnick ・ crembed ・ colors ・ vote ・ invite ・ embed ・ botlst  ・ userinfo ・ serverinfo ・ role ・ channel ・ stats ・ emoji-add ・ emoji-delete ・ enlarge ・ boosts ・ give <user> <role> ・ temp <role> <time> <user> ・ remove <user> <role> ・ deleterole <role> ・ createrole <name> ・ rename <role> <new name> ・ color <role> <color> ・ roleinfo <role> ・ revokeall ・ revokeinvites```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
       

def setup(bot):
    bot.add_cog(general67(bot))