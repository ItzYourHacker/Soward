import discord
from discord.ext import commands
import json
from utilities.Tools import *

class av(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["av"])
    @blacklist_check()
    async def avatar(self, ctx, user: discord.Member = None):
      if user == None:
        user = ctx.author
      button = discord.ui.Button(label='User Avatar', style=discord.ButtonStyle.red)
      button2 = discord.ui.Button(label='Server Avatar', style=discord.ButtonStyle.green)
      view = discord.ui.View()
      view.add_item(button)
      view.add_item(button2)
      webp = user.avatar.replace(format='webp')
      jpg = user.avatar.replace(format='jpg')
      png = user.avatar.replace(format='png')
      avemb = discord.Embed(color=0xFF1B1B,title="", description="Click On Button Below!")
      await ctx.send(embed=avemb, view=view)
      async def button_callback(interaction: discord.Interaction):
          embed = discord.Embed(color=0xFF1B1B,title=f"{user}  Avatar",description=f"[[PNG]({png}) | [JPG]({jpg}) | [WEBP]({webp})]")
          embed.set_image(url=user.avatar.url)
          embed.set_footer(text=f"Requested by {ctx.author}")
          await interaction.response.edit_message(embed=embed)
      async def button2_callback(interaction: discord.Interaction):
          embed = discord.Embed(color=0xFF1B1B,title=f"{user} Server Avatar",description=f"[[PNG]({png}) | [JPG]({jpg}) | [WEBP]({webp})]")
          embed.set_image(url=user.display_avatar.url)
          embed.set_footer(text=f"Requested by {ctx.author}")
          await interaction.response.edit_message(embed=embed)
      button2.callback = button2_callback
      button.callback = button_callback
        
      

def setup(bot):
    bot.add_cog(av(bot))