import discord
from discord.ext import commands
import requests
import random
import asyncio
import aiohttp
import io
import os 

#apikey = os.environ['APIKEY']


class Funop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    # I mostly use the API provided by https://some-random-api.ml/
    # This site provide numbers of free API that you can use
    
    @commands.command()
    async def duck(self, ctx): # Send a random duck image
      response = requests.get('https://random-d.uk/api/v1/random')
      data = response.json()
      embed = discord.Embed(
          title = 'Duck 🦆',
          description = 'This is a duck',
          color=random.randint(0, 0xFFFFFF)
          )
      embed.set_image(url=data['url'])            
      embed.set_footer(text="")
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

    @commands.command() 
    async def ball(self, ctx, *, question): # A ball command
      ballresponse = [
  "Yes", "No", "Take a wild guess...", "Very doubtful",
  "Sure", "Without a doubt", "Most likely", "Might be possible",
  "You'll be judged", "no... (╯°□°）╯︵ ┻━┻", "no... baka",
  "Please, Please no ;-;", "Who know?", "I don't care", "This tbh", "You too", 
  "Bruh", "(☞ﾟヮﾟ)☞", "ㄟ( ▔, ▔ )ㄏ", "¯\_(ツ)_/¯", "LOL", "lmao", "f*ck you"
] # You can add more comment though. Just remember to add "," after a command
      answer = random.choice(ballresponse) # This will choose a random comment from that ballresponse
      await ctx.channel.trigger_typing()
      await ctx.reply(f"🎱**Answer:** {answer}")

    @commands.command()
    async def coffee(self, ctx):
      response = requests.get('https://coffee.alexflipnote.dev/random.json')
      data = response.json()
      embed = discord.Embed(
          title = 'Coffee ☕',
          description = 'A random image of coffee',
          color=random.randint(0, 0xFFFFFF)
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text="")
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

 #   @commands.command()
  #  @commands.cooldown(1, 3, commands.BucketType.user)
   # async def meme(self, ctx):
   #   response1 = requests.get('https://some-random-api.ml/meme')
  #    data1 = response1.json()
    #  embed = discord.Embed(
   #       title = 'Meme 🤣',
    #      description = 'Here is a random meme I found',
     #     color = random.randint(0, 0xFFFFFF)
   #   )
    #  embed.set_image(url=data1['image'])
   #   embed.set_footer(text="")
     # await ctx.channel.trigger_typing()
    #  await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cat(self, ctx):
      response1 = requests.get('https://aws.random.cat/meow')
      response2 = requests.get('https://some-random-api.ml/facts/cat')
      data1 = response1.json()
      data2 = response2.json()
      embed = discord.Embed(
          title = 'Cat 🐈',
          description = 'This is a cat',
          color=random.randint(0, 0xFFFFFF)
          )
      embed.set_image(url=data1['file'])            
      embed.set_footer(text=data2['fact'])
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user) # A dog image and fact from the API
    async def dog(self, ctx):
      response1 = requests.get('https://some-random-api.ml/img/dog')
      response2 = requests.get('https://some-random-api.ml/facts/dog')
      data1 = response1.json()
      data2 = response2.json()
      embed = discord.Embed(
          title = 'Dog 🐕',
          description = 'This is a dog',
          color=random.randint(0, 0xFFFFFF)
      )
      embed.set_image(url=data1['link'])
      embed.set_footer(text=data2['fact'])
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)

    @commands.command() # A ship command. I just use the basic random on Python. You can rewrite it by using an API though.
    async def ship(self, ctx, name1=None, name2=None):
        shipnumber = int(random.randint(0, 100)) # This will choose a random number from 0 to 100
      
        if not name1:
          name1 = ctx.author.name
          name2 = random.choice(ctx.guild.members)
          name2 == name2.name
        if not name2:
          name2 = ctx.author.name
          name1 = name1
# You can add more answer if you want. I barely have time to think more :(
        if 0 <= shipnumber <= 30:
          comment = "Really low! {}".format(random.choice(
            ["Friendzone ;(", 
            'Just "friends"', 
            "There's barely any love ;(",
            "I sense a small bit of love!",
            "Still in that friendzone ;(",
            "No, just no!",
            "But there's a small sense of romance from one person!"]))
        elif 31 <= shipnumber <= 70:
          comment = "Moderate! {}".format(random.choice(
            ["Fair enough!",
            "A small bit of love is in the air...",
            "I feel like there's some romance progressing!",
            "I'm starting to feel some love!",
            "At least this is acceptable",
            "...",
            "I sense a bit of potential!",
            "But it's very one-sided OwO"]))
        elif 71 <= shipnumber <= 90:
          comment = "Almost perfect! {}".format(random.choice(
            ["I definitely can see that love is in the air",
            "I feel the love! There's a sign of a match!",
            "A few things can be imporved to make this a match made in heaven!",
            "I can definitely feel the love",
            "This has a big potential",
            "I can see the love is there! Somewhere..."]))
        elif 90 < shipnumber <= 100:
          comment = "True love! {}".format(random.choice(
            ["It's a match!", 
            "There's a match made in heaven!", 
            "It's definitely a match!", 
            "Love is truely in the air!", 
            "Love is most definitely in the air!"]))
        

        if shipnumber <= 40:
            shipColor = 0xE80303
        elif 41 < shipnumber < 80:
            shipColor = 0xff6600
        else:
            shipColor = 0x3be801

        emb = (discord.Embed(color=shipColor, \
                             title="Love test for:", \
                             description="**{0}** and **{1}** {2}".format(name1, name2, random.choice(
                               [
                                ":sparkling_heart:", 
                                ":heart_decoration:", 
                                ":heart_exclamation:", 
                                ":heartbeat:"]
                                                                                                      )
                                                                          )
                            )
              )
        emb.add_field(name="Results:", value=f"{shipnumber}%  {comment}", inline=True)
        emb.set_author(name="Shipping", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=emb)

    @commands.command() # A simple dice roll command
    async def roll(self, message):
      dice = ["1","2","3","4","5","6"]
      number = random.choice(dice)
      await message.channel.trigger_typing()
      message0 = await message.reply("I am rolling the dice now")
      await asyncio.sleep(3)
      await message0.edit(content=f"The number is {number}")

    @commands.command() # This will get a random joke sentence from the listed API
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def joke(self, ctx):
      response = requests.get('https://some-random-api.ml/joke') 
      data = response.json()
      joke = data['joke']
      embed = discord.Embed(
          title = 'Here is a joke',
          description = joke,
          color = 0xFF1B1B)
      await ctx.channel.trigger_typing()
      await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Funop(bot))