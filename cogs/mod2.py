import discord
from discord.ext import commands
import json
from utilities.Tools import*

class Moderation2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Moderation commands"""
  
    def help_custom(self):
		      emoji = '<a:moderation_animated:1017402486258151534>'
		      label  = "Moderation"
		      description = ""
		      return emoji, label, description  

#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    @blacklist_check()
    async def Moderation(self, ctx: commands.Context):
            embed=discord.Embed(title="**Moderation**", description="""``` hide ・ unhide ・ nuke ・ createchannel ・ deletechannel ・ lockserver ・ ban ・ unban ・unbanall ・ warn ・ timeout ・ mute ・ unmute ・ clear ・ lockall ・ unlockall ・ lock(run again this cmnd for unlock)・ hideall ・ unhideall ・ purge ・ purge contains ・ purge startswith ・ purge endswith ・ purge user ・ purge invites ・ clone ・ slowmode ・ snipe ・ nick ・ enlarge ・ giveallhumans ・ giveallbots ・ removeallhumans ・ removeallbots ・ jail ・ unjail ・ boosts ・ cleanup (Clears Bot Messages) ・ vcroles New ・ vcrole Config ・ Vcrole Delete ・ vcdeafen ・ vcundeafen ・ vcmute ・ vcunmute```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=self.bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Prince", icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Moderation2(bot))