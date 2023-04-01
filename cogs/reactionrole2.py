import discord
from discord.ext import commands
import json

class reactionrole67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """ReactionRoles commands"""  

    def help_custom(self):
		      emoji = '<a:roles:1017403323487371344>'
		      label = "Reaction Roles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def ReactionRoole(self, ctx: commands.Context):
        """``` reactions ・ reaction <emote> <role> <channel> <title> ・ reactions```"""


def setup(bot):
    bot.add_cog(reactionrole67(bot))