import discord
from discord.ext import commands
import random
from utilities.Tools import* 
class Ranker(commands.Cog):
  def __init__(self, client):
    self.client = client

  def rateEmbed(self, method, method_2, percent):
    embed = discord.Embed(
      title = f"{method} machine",
      description = f"You are {percent}% {method_2}",
      color = 0xFF1B1B,
    )
    return embed

  @commands.command()
  @blacklist_check()
  async def gayrate(self, ctx):
      """get ur gayness per¢"""
      embed = self.rateEmbed("gayrate", "gay", random.randint(0, 100))
      await ctx.send(embed=embed)

  @commands.command(aliases=['simp'])
  @blacklist_check()
  async def simprate(self, ctx):
      """get ur simpness per¢"""
      embed = self.rateEmbed("simprate", "simp", random.randint(0, 100))
      await ctx.send(embed=embed)

  @commands.command(aliases=['lesbo'])
  @blacklist_check()
  async def lesbianrate(self, ctx):
      """get ur lesbianness per¢"""
      embed = self.rateEmbed("lesbianrate", "lesbian", random.randint(0, 100))
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def realgay(self, ctx, member : discord.Member = None):
    """Your author id has to be equal to 0, so in other words, no one will ever run this command."""
    if ctx.author.id == 0:
      if member != None:
        userIDSum = 1
        unfiltered = [i for i in str(member.id)]
        filtered = [i for i in unfiltered if i != "0"]
        for i in filtered:
            i = int(i)
            userIDSum += i
        await ctx.send(f"Unfortunately they will always be {userIDSum}% gay :|")

      else:
        userIDSum = 1
        unfiltered = [i for i in str(ctx.author.id)]
        filtered = [i for i in unfiltered if i != "0"]
        for i in filtered:
            i = int(i)
            userIDSum += i
        await ctx.send(f"Unfortunately you will always be {userIDSum}% gay :|")

def setup(client):
  client.add_cog(Ranker(client))

  