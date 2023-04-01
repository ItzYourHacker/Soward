import json
import discord
from discord.ext import commands
from ext.var import Var
import json


class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, ctx):
        channel = self.bot.get_channel(Var.command_logger.value)

        embed = discord.Embed(
            title=f"Command Executed!",
            colour=0x2f3136,
            description=f"**Command:** {ctx.command.name}"
            f"```{ctx.message.content}```\n"
            f"in {ctx.channel.mention} of \n"
            f"**{ctx.guild.name}** : {ctx.guild.id}",
        )

        embed.set_author(
            name=f"{ctx.author} | {ctx.author.id}", icon_url=ctx.author.display_avatar
        )
        await channel.send(embed=embed)

    @commands.Cog.listener() 
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.bot.user:
                return
        try:
            if message is not None:
                with open("autoresponse.json", "r") as f:
                    autoresponse = json.load(f)
                if str(message.guild.id) in autoresponse:
                    ans = autoresponse[str(message.guild.id)][message.content.lower()]
                    
                    return await message.channel.send(ans)
        except:
            pass

def setup(bot):
    bot.add_cog(EventHandler(bot))
