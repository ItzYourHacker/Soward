import discord
from discord.ext import commands
import random
from Errorembed import ErrorEmbed
import datetime
from typing import Optional
from utilities.Tools import*

class Random(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.choice = ['Heads', 'Tails']

  @commands.command(aliases=['cf'])
  @blacklist_check()
  async def coinflip(self, ctx, bet:str=None):
    """Flip a coin."""
    if bet == None:
      embed = ErrorEmbed.error("Missing Command Arguments", "Please specify the side you want to flip! (1 for heads and 2 for tails)")
      await ctx.send(embed=embed)
    else:
      try:
        bet = int(bet)
      except:
        embed = ErrorEmbed.error("Invalid Command Arguments", "The command couldn't run because your bet is invalid.")
        await ctx.send(embed=embed)
        return
      
      if bet == 1 or bet == 2:
        if bet == 1:
          choice = random.choice(self.choice)
          if choice == "Heads" and bet == 2:
            color = 0xff0000
          elif choice == "Tails" and bet == 1:
            color = 0xff0000
          else:
            color = 0x00ff00

          embed = discord.Embed(
            title = "You bet Heads :coin:",
            description = f"The result was {choice}",
            color = color,
            timestamp = datetime.datetime.utcnow()
          )
          await ctx.send(embed=embed)

        elif bet == 2:
          choice = random.choice(self.choice)
          if choice == "Heads" and bet == 2:
            color = 0xff0000
          elif choice == "Tails" and bet == 1:
            color = 0xff0000
          else:
            color = 0x00ff00

          embed = discord.Embed(
            title = "You bet Tails :crocodile:",
            description = f"The result was {choice}",
            color = color,
            timestamp = datetime.datetime.utcnow()
          )
          await ctx.send(embed=embed)
      else:
        embed = ErrorEmbed.error("Invalid Command Arguments", "The command couldn't run because your bet is invalid. :|")
        await ctx.send(embed=embed)   

def setup(client):
  client.add_cog(Random(client))