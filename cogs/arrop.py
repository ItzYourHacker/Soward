import discord
from discord.ext import commands
import json


class autoresponse(commands.Cog):
  def __init__(self, client):
    self.client = client

  

  @commands.group(description='show the help menu of autoresponse')
  async def ar(self, ctx):
        ...        
   
  
  @ar.command(description='count all autoresponses of server')
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(administrator=True)
  async def show(self, ctx):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0x2f3136)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                    st += f"*( {'0' + str(count) if count < 10 else count} )* Name -> {autoresponse}\n"
                    test = count
                    count += 1
            embed.title = f"Total autoresponses - {test}"
        embed.description = st
        await ctx.send(embed=embed) 
    
def setup(client):
    client.add_cog(autoresponse(client))