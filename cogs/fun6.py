import discord
from discord.ext import commands
import os
import json
import urllib.request
from Errorembed import ErrorEmbed as ee
import datetime
from typing import Optional
from utilities.Tools import*
class Api(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.animal_facts = ['dog', 'cat', 'panda', 'fox', 'bird', 'koala', 'kangaroo', 'racoon', 'elephant', 'giraffe', 'whale']
    self.animal_images = ['dog', 'cat', 'panda', 'red_panda', 'fox', 'bird', 'koala', 'kangaroo', 'raccoon', 'whale', 'pikachu']

  @commands.command(aliases=['animalfact', 'af'])
  @blacklist_check()
  async def fact(self, ctx, *, animal = None):
    """Get a random fact about an animal."""
    if animal == None:
      embed = ee.error("Missing Command Arguments", "You need to specify an animal to get a fact about.  Currently you can get facts about a `dog`, `cat`, `panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `elephant`, `giraffe`, and `whale`.")
      await ctx.send(embed=embed)
    else:
      if animal.lower() not in self.animal_facts:
        embed = ee.error("Missing Command Arguments", "You need to specify an animal to get a fact about.  Currently you can get facts about a `dog`, `cat`, `panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `elephant`, `giraffe`, and `whale`.")
        await ctx.send(embed=embed)
      else:
        animal = animal.lower()
        url = f"https://some-random-api.ml/facts/{animal}"
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)

        embed = discord.Embed(
          title = f"Random {animal.title()} Fact",
          description = obj["fact"],
          color = 0xFF1B1B,
          timestamp = datetime.datetime.utcnow()
        )
        await ctx.send(embed=embed)

  @commands.command(aliases=['ai', 'animalimage', 'animimg'])
  @blacklist_check()
  async def image(self, ctx, *, animal = None):
    """Get a random animal image."""
    if animal == None:
      embed = ee.error("Missing Command Arguments", "You need to specify an animal to get an image for.  Currently you can get images for a `dog`, `cat`, `panda`, `red_panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `whale`, and `pikachu`.")
      await ctx.send(embed=embed)
    else:
      if animal.lower() not in self.animal_images:
        embed = ee.error("Missing Command Arguments", "You need to specify an animal to get an image for.  Currently you can get images for a `dog`, `cat`, `panda`, `red_panda`, `fox`, `bird`, `koala`, `kangaroo`, `racoon`, `whale`, and `pikachu`.")
        await ctx.send(embed=embed)
      else:
        animal = animal.lower()
        url = f"https://some-random-api.ml/img/{animal}"
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)

        embed = discord.Embed(
          title = f"Random {animal.title()} Image",
          description = obj["link"],
          color = 0xFF1B1B,
          timestamp = datetime.datetime.utcnow()
        )
        embed.set_image(url=obj["link"])
        await ctx.send(embed=embed)
  
  @commands.command(aliases=['winkgif'])
  @blacklist_check()
  async def wink(self, ctx):
    """Get a random winking gif."""
    url = "https://some-random-api.ml/animu/wink"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Winking Gif",
      description = obj["link"],
      color = 0xFF1B1B,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['patgif'])
  @blacklist_check()
  async def pakjht(self, ctx):
    """Get a random patting gif."""
    url = "https://some-random-api.ml/animu/pat"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Patting Gif",
      description = obj["link"],
      color = 0xFF1B1B,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['huggif'])
  @blacklist_check()
  async def hug(self, ctx):
    """Get a random hugging gif."""
    url = "https://some-random-api.ml/animu/hug"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = f"",
      description = obj["link"],
      color = 0xFF1B1B,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def gay(self, ctx, member:commands.MemberConverter=None):
      """Place gay colors over a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/gay?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/gay?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"

      embed = discord.Embed(
        title = f"{men}'s pfp being gayified",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def glass(self, ctx, member:commands.MemberConverter=None):
      """Place glass over a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/glass?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/glass?avatar={member.avatar}"
        men = member.display_name

      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp being glassed",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def wasted(self, ctx, member:commands.MemberConverter=None):
      """Place the GTA wasted over a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/wasted?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men} just got wasted",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command(aliases=['grey', 'greyscale'])
  @blacklist_check()
  async def grayscale(self, ctx, member:commands.MemberConverter=None):
      """Grayscale a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men} just got grayed out",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def invert(self, ctx, member:commands.MemberConverter=None):
      """Invert a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/invert?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/invert?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men} just got inverted",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command(aliases=['invertgreyscale', 'igs'])
  @blacklist_check()
  async def invertgrayscale(self, ctx, member:commands.MemberConverter=None):
      """Invert + Grayscale a user's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men} just got invertgreyscaled",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def threshold(self, ctx, member:commands.MemberConverter=None):
      """idk its a threshold recoloring lol.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/threshold?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/threshold?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men} just got thresholded",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def sepia(self, ctx, member:commands.MemberConverter=None):
      """Recolor a member's profile picture with sepia coloring.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/sepia?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/sepia?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp but more sepia",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def red(self, ctx, member:commands.MemberConverter=None):
      """Recolor a member's profile picture with red coloring.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/red?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/red?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp but more red",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def green(self, ctx, member:commands.MemberConverter=None):
      """Recolor a member's profile picture with green coloring.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/green?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/green?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp but more green",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def blue(self, ctx, member:commands.MemberConverter=None):
      """Recolor a member's profile picture with blue coloring.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/blue?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/blue?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp but more blue",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def blurple(self, ctx, member:commands.MemberConverter=None):
      """Recolor a member's profile picture with blurple coloring.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/blurple?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/blurple?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pfp but more blurple",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def blur(self, ctx, member : commands.MemberConverter = None):
      """Blur a member's profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/blur?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/blur?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s blurred pfp",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command()
  @blacklist_check()
  async def pixelate(self, ctx, member:commands.MemberConverter=None):
      """Pixelate a member's profile picture, but also lose 63/64 of the profile picture.  If the command doesn't send an image the first time just resend the command.  It is a little buggy."""
      if member == None:
        url = f"https://some-random-api.ml/canvas/pixelate?avatar={ctx.author.avatar}"
        men = ctx.author.display_name
      else:
        url = f"https://some-random-api.ml/canvas/pixelate?avatar={member.avatar}"
        men = member.display_name
      
      if (url[:-10].endswith(".webp")):
        url = url[:-14]
        url += "png?size=1024"
        
      embed = discord.Embed(
        title = f"{men}'s pixelated pfp",
        color = 0xFF1B1B,
        timestamp = datetime.datetime.utcnow()
      )
      embed.set_image(url=url)
      await ctx.send(embed=embed)

  @commands.command(aliases=['face-palm'])
  @blacklist_check()
  async def facepalm(self, ctx):
    """Get a random face palming gif."""
    url = "https://some-random-api.ml/animu/face-palm"
    response = urllib.request.urlopen(url).read().decode()
    obj = json.loads(response)
    embed = discord.Embed(
      title = "Random Face-Palming Gif",
      description = obj["link"],
      color = 0xFF1B1B,
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_image(url=obj["link"])
    await ctx.send(embed=embed)

  @commands.command(aliases=['pokedex', 'poke', 'pokesearch', 'searchpoke', 'pokefilter'])
  @blacklist_check()
  async def pokemoon(self, ctx, pokemon:str=None):
    """Search Pokedex for a pokemon and get all of it's stats."""
    if pokemon == None:
      embed = ee.error("Missing Command Arguments", "You need to specify a Pokémon to search for!")
      await ctx.send(embed=embed)
    else:
        url = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
        try:
          response = urllib.request.urlopen(url).read().decode()
        except:
          embed = ee.error("Pokemon Search Failed", "We coudn't find that pokemon!")
          await ctx.send(embed=embed)
          return
        response = urllib.request.urlopen(url).read().decode()
        obj = json.loads(response)
        embed = discord.Embed(
          title = obj["name"].title(),
          description = obj["description"],
          color = 0xFF1B1B,
          timestamp = datetime.datetime.utcnow()
        )
        embed.add_field(name="ID", value=obj["id"])
        embed.add_field(name="Type", value=", ".join(obj["type"]))
        embed.add_field(name="Species", value = ", ".join(obj["species"]))
        embed.add_field(name="Abilities", value=", ".join(obj["abilities"]))
        embed.add_field(name="Height", value=obj["height"], inline=False)
        embed.add_field(name="Weight", value=obj["weight"])
        embed.add_field(name="Base Experience", value=obj["base_experience"])
        embed.add_field(name="Gender", value = ", ".join(obj["gender"]))
        embed.add_field(name="Egg Groups", value=", ".join(obj["egg_groups"]), inline=False)
        embed.add_field(name="꧁༺ 𝓢𝓽𝓪𝓽𝓼 ༻꧂", value="◤✞ --------------- ✞◥", inline=False)
        embed.add_field(name="HP", value=obj["stats"]["hp"], inline=False)
        embed.add_field(name="Attack", value=obj["stats"]["attack"])
        embed.add_field(name="Defense", value=obj["stats"]["defense"])
        embed.add_field(name="Special Attack", value=obj["stats"]["sp_atk"])
        embed.add_field(name="Special Defense", value=obj["stats"]["sp_def"])
        embed.add_field(name="Speed", value=obj["stats"]["speed"])
        embed.add_field(name="꧁༺ 𝓕𝓪𝓶𝓲𝓵𝔂 ༻꧂", value="◤✞ ------------------- ✞◥", inline=False)
        embed.add_field(name="Evolution Stage", value=obj["family"]["evolutionStage"], inline=False)
        embed.add_field(name="Pokémon Evolutions", value = ", ".join(obj["family"]["evolutionLine"]) if obj["family"]["evolutionLine"] else None)
        embed.add_field(name="Generation", value=obj["generation"])
        embed.set_thumbnail(url=obj["sprites"]["normal"])
        embed.set_image(url=obj["sprites"]["animated"])
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name = f"Pokemon Information for {pokemon.title()}", icon_url = obj["sprites"]["normal"])
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Api(client))