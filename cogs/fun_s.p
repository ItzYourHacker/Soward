import discord
from discord.ext import commands, tasks
from discord.commands import ( 
    slash_command,
    Option
)
import json
import requests
import aiohttp
import psutil
from psutil import Process, virtual_memory
from typing import Union, Optional
import random
import asyncio
import time
import datetime
from .utils.config import *
import math
#from afks import afks
from discord.utils import get
import numpy as np
import re

class ButtonView(discord.ui.View):
  def __init__(self):
    super().__init__()
  
    button = discord.ui.Button(label='Claim', style=discord.enums.ButtonStyle.green)
  
    self.add_item(button)

kisses = ['https://cdn.nekos.life/kiss/kiss_138.gif', 'https://cdn.nekos.life/kiss/kiss_106.gif', 'https://cdn.nekos.life/kiss/kiss_128.gif', 'https://cdn.nekos.life/kiss/kiss_139.gif', 'https://cdn.nekos.life/kiss/kiss_061.gif']
loves = ['']
cuteim = ['https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218764136337469/868354099043794944.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218760332083200/856799753815326760.png', 'https://cdn.discordapp.com/attachments/889397337976360960/891218722293944320/859358963429408768.png', 'https://i.redd.it/o1g3su199hp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/g09y1v5iugp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/siju18xd2jp71.jpg', 'https://i.redd.it/hai3526j6hp71.jpg', 'https://i.redd.it/91p1yme33ip71.jpg', 'https://i.redd.it/6lvfdsdp6hp71.jpg', 'https://i.redd.it/5arz0zh57hp71.jpg', 'https://i.redd.it/nxukbymljjp71.jpg', 'https://i.imgur.com/mPgwExY.gifv', 'https://i.redd.it/w544woii9gp71.jpg', 'https://i.redd.it/6bqrmkzpjgp71.jpg']
slaps = ['https://cdn.weeb.sh/images/B1fnQyKDW.gif', 'https://cdn.weeb.sh/images/ByTR7kFwW.gif', 'https://cdn.weeb.sh/images/HyV5mJtDb.gif', 'https://cdn.weeb.sh/images/SkNimyKvZ.gif', 'https://cdn.weeb.sh/images/HkK2mkYPZ.gif', 'https://cdn.weeb.sh/images/SkSCyl5yz.gif', 'https://cdn.weeb.sh/images/SJx7M0Ft-.gif']
pats = ['https://cdn.nekos.life/pat/pat_035.gif', 'https://cdn.nekos.life/pat/pat_074.gif', 'https://cdn.nekos.life/pat/pat_028.gif', 'https://cdn.nekos.life/pat/pat_022.gif']
jokes = ['']
cats = ['']
password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
advices = ['Respect your elders', 'Speak always truth', 'be honest', 'Think About your future.', 'Think positive.', 'Work hard not going for smart work.', 'Always remember your culture.', 'Trust on god.', 'Never give up.', 'be cool be calm', 'Listen carefully.', 'Remember Your responseblity.', 'Never forget your past.']
margya = ['']
boreds = ['']
gayr = ['1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '68%', '69%', '70%', '71%', '72%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%','100%']
quacks = ['']
carry = ['I\'d slap you, but that will be animal abuse.', 'You must have born on a highway cos\' that\'s where most accidents happen.', 'I would roast you but momma says i\'m ain\'t allowed to burn trash.', 'English maybe I don\'t speak idiot.', 'If I wanted a bitch i would buy a dog.', 'Boys only bully girls If they fancy them.', 'Oh sorry was i supposed to be offnded?', 'Maybe if you ate some of your makeup , You would on pretty the inside.', 'I could argue back but i would be in the wrong too.', 'Go make a hate page if you don\'t like me.', 'If your name is not google stop , acting like you know everything.', 'If you ran like your mouth , you would be in good shape.']
battles = ['']
typeracer = ['Happiness is the reward we get for living to the highest right we know.', 'Babur was the first Mughal emperor in india.', 'Nobody followed up on that email.', 'Gopal pays no attention on his health.', 'Mikesh is unable to follow instructions.', 'Shall we go on a Goa trip?']
dances = ['']
cuddles = ['']
koalas = ['']
pandas = ['']
tickles = ['']
ages = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
truths = ["Are you a hard-working student?",
"Are you into any sports?",
"Are you scared of any animals?",
"Are you scared of dying? Why?",
"Are you scared of ghosts?",
"Are you still a virgin?",
"Can you lick your elbow?",
"Can you see yourself being married to the creepiest kid a your school someday?",
"Can you speak a different language?",
"Can you touch your tongue to your nose?",
"Can you use a pogo stick?",
"Could you go a week without junk food?",
"Could you go two months without talking to your friends?",
"Describe the weirdest dream you've ever had?",
"Describe the weirdest dream you’ve ever had?",
"Describe your most recent dream that you recall.",
"Describe your most recent romantic encounter.",
"Describe your worst kiss ever.",
"Do you believe in love at all?",
"Do you believe in love at first sight?",
"Do you ever talk to yourself in the mirror?",
"Do you have a hidden talent? What is it?",
"Do you have a job? If so, what is your favourite thing about it?",
"Do you have an imaginary friend?",
"Do you have any phobias?",
"Do you have any unusual talents?",
"Do you know how to cook?",
"Do you know how to dance?",
"Do you like doing chores?",
"Do you like to exercise?",
"Do you message people during your classes?",
"Do you prefer apple or android?",
"Do you sing in the shower? What song did you sing the last time?",
"Do you think you will marry your bf/gf? If not, why not?",
"Explain to the person you like least in this group why you like them the least.",
"Have you been in any fights while in school?",
"Have you ever been kissed yet? If so, who was your best kiss?",
"Have you ever bitten a toenail?",
"Have you ever blamed a fart on an animal?",
"Have you ever blamed something that you have done on one of your siblings?",
"Have you ever cheated on a test?",
"Have you ever cheated or been cheated on?",
"Have you ever climbed a tree?",
"Have you ever crapped your pants since you were a child?",
"Have you ever eaten food that you've dropped on the ground? If so, how long was it on the ground?",
"Have you ever fallen asleep during a class?",
"Have you ever had a crush on a teacher?",
"Have you ever had a crush on someone that your best friend has dated?",
"Have you ever had someone write an assignment or a work for you?",
"Have you ever kissed an animal?",
"Have you ever let someone take the blame for something you did?",
"Have you ever lied to your best friend?",
"Have you ever lied to your parents about if you were in classes or not?",
"Have you ever lied to your parents about what you were doing after school?",
"Have you ever peed in a pool?",
"Have you ever picked your nose in public?",
"Have you ever posted something on the internet/social media that you regret?",
"Have you ever pulled a prank on one of your teachers?",
"Have you ever received a love letter?",
"Have you ever ridden the bus without paying the fare?",
"Have you ever stolen something of value worth more than $10?",
"Have you ever stolen something?",
"Have you ever taken money from your roommate?",
"Have you ever taken money that didn't belong to you?",
"Have you ever thrown a party at your house?",
"Have you ever told a lie during a game of Truth or Dare? What was it and why?",
"Have you ever told one of your best friend's secrets, even if you said you wouldn't?",
"Have you ever used someone else's password?",
"Have you ever watched an adult film without your parents knowing?",
"Have you ever worn the same clothes for more than three days?",
"How do you feel about end pieces of a loaf of bread?",
"How do you feel about social media?",
"How far would you go to land the guy or girl of your dreams?",
"How many boyfriends (or girlfriends) have you had?",
"How many days could you go without your partner?",
"How many kids would you like to have?",
"How many siblings do you have?",
"How many times have you skipped class for no reason?",
"How old were you when your parents sat you down for 'the talk' and what did they say (or not say) about 'the birds and the bees'?",
"How soon did you realize that you were in love with your partner?",
"How soon did/do you want start a family?",
"How was your first kiss?",
"If there was no such thing as money, what would you do with your life?",
"If you could be a superhero; what would your power be?",
"If you could be any animal, which one would you be?",
"If you could be any dinosaur; which would it be?",
"If you could be any super villain; who would you be?",
"If you could change one thing on your body, what would it be?",
"If you could dye your hair any colour, what colour would you pick?",
"If you could erase one past experience, what would it be?",
"If you could go anywhere in the world, where would you go?",
"If you could make one wish right this second, what would it be?",
"If you could only hear one song for the rest of your life, what would it be?",
"If you could own your own business one day, what would it be?",
"If you could own your own business one day; what would it be?",
"If you could switch lives with any celebrity for a day, who would it be?",
"If you could take away one bad thing in the world, what would it be?",
"If you could, what would you change about your life?",
"If you had never met your partner, where do you think you would be?",
"If you had the choice to live on your own right now, would you do it?",
"If you have ever cheated, why did you do it?",
"If you suddenly had a million dollars; what would you do with all of your money?",
"If you were a billionaire, what would you spend your time doing?",
"If you were rescuing everyone here from a burning building, but you had to leave one behind, who would it be?",
"If you were to be stuck on a deserted island, which friend would you want with you?",
"If you were to be trapped on an island for 3 days, what would you take with you?"]
dares = ["Act like a monkey and record a video of it.",
"Act like you do not understand human language until your next turn (come up with your own language).",
"Act like your favourite Disney character for the rest of the game.",
"Close your eyes and send a blind text to a random person.",
"Compose a poem on the spot based on something the group comes up with.",
"Everything you say for the next 5 minutes has to rhyme.",
"Everything you say for the next 5 minutes must not contain the words: 'but', 'a', 'the', 'or'",
"Make a freestyle rap song about each person in the group",
"Make a poem using the words 'orange' and 'moose'.",
"Make a poem using the words 'pineapple' and 'apple'.",
"Make a poem using the words 'goose' and 'peanuts'.",
"Make up a poem about the colour blue.",
"Make up a story about a random person in the group.",
"Post 'I love English!' on a social media.",
"Record a video of you dancing, but without music.",
"Record a video of you playing the air drums to a song of your choice.",
"Record a video of you playing the air guitar to a song of your choice.",
"Record an impression of your favourite celebrity.",
"Record an impression of your favourite animal.",
"Record your best evil laugh; as loud as you can.",
"Record your best president impression.",
"Record yourself saying the alphabet backwards.",
"Record yourself singing 'Twinkle Twinkle, Little Star' while beat boxing.",
"Record yourself singing the alphabet without moving your mouth.",
"Record yourself talking about your favourite food in a russian accent.",
"Say 'ya heard meh' after everything you say for the next 5 minutes.",
"Say 'you know what am sayin' after everything you say for the next 5 minutes.",
"Text someone asking them if they believe in aliens, send a screenshot of the conversation.",
"Send an email to one of your teachers, telling them about how your day is going and take a screenshot.",
"Send an unsolicited text message to one of your friends, telling them about how your day is going and take a screenshot.",
"Send the last photo you took with your phone camera.",
"Send the last screenshot you took on your phone.",
"Send the most embarrassing photo on your phone.",
"Send the oldest selfie on your phone.",
"Send a screenshot of your most recent google search history.",
"Send a selfie of you making a funny face.",
"Set your phone language to Chinese for the next 10 minutes.",
"Show the last three people you texted and what the messages said.",
"Text your crush and tell them how much you like them.",
"Use the letters of the name of another player to describe them (ex. SAM : S = Silly ; A = Attractive ; M = Merry)",
"Yell out the first word that comes to your mind, and record it."]
shaadi = ['']
cries = ['']
feeds = ['']
khush = ['']
sharam = ['']
chases = ['']
confuse = ['']
laughes = ['']
cheers = ['']
hugs = ['']
EIGHT_BALL_ANSWERS = [
            "Yeah", "Yes", "Ofcourse", "Ofc", "Ah Yes", "I see in the Prophecy: TRUE!"
            "Nah", "No", 'Nope', 'Never', "I don't think so",
            "idk", "Maybe", "ig", "I'm bored", "You're annoying"
        ]
birthdayfile = './data/databases/bdays.txt'

def sub(self, x: float, y: float):
  return x - y

def add(self, x: float, y: float):
  return x + y

def div(self, x: float, y: float):
  return x / y


def sqrt(self, x: float):
  return math.sqrt(x)

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

def advantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    highRoll = max(a)
    ind = np.argmax(a)
    highRollMath = b[ind]
    return str(highRoll), highRollMath

def disadvantageRoll(times, sides, add):
    a = []
    b = []
    for i in range(2):
        total = 0
        calcNum = ""
        for x in range(times):
            sideNum = random.randint(1, sides)
            total = total + sideNum
            if calcNum == "":
                sideNum = str(sideNum)
                calcNum = f"{sideNum}"
            else:
                sideNum = str(sideNum)
                calcNum = f"{calcNum} + {sideNum}"
        calcNum = f"{calcNum} + ({add})"
        total = total + add
        a.append(total)
        b.append(calcNum)
    lowRoll = min(a)
    ind = np.argmin(a)
    lowRollMath = b[ind]
    return str(lowRoll), lowRollMath


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


class fun_s(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
  

    @slash_command(name = "meme")
    async def m_eme(self, ctx):
        embed = discord.Embed(title="Here is a meme for you!", color = DEFAULT_COLOR)
        embed.set_footer(text="Requested by {}".format(ctx.author.name))

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=h ot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.respond(embed=embed)
  
  
    @slash_command(name = "hug")
    async def h_ug(self, ctx,
                 member: discord.Member):
      random_link = random.choice(hugs)
      embed = discord.Embed(title=f"{ctx.author.name} hugs {member.display_name}!", color = DEFAULT_COLOR);
      embed.set_image(url=f"{random_link}");
      await ctx.respond(embed=embed);

    #@slash_command(name = "heckur")
    #async def ufff(self, ctx,
                   #channel: discord.TextChannel,
                   #* , s):
      #if channel == None:
        #channel = ctx.channel
      #if s == "@everyone":
       # return await ctx.respond("You can't ping everyone!")
      #if s == "@here":
        #return await ctx.respond("You can't ping everyone!")
      #else:
        #await channel.send(f"{s}")

    @slash_command(name = "kiss")
    async def ki_ss(self, ctx,
                  member: discord.Member):
        embedkiss = discord.Embed(title=f"{ctx.author.name} kisses {member.display_name}", color = DEFAULT_COLOR)

        random_link = random.choice(kisses)
        embedkiss.set_image(url=random_link)

        await ctx.respond(embed=embedkiss)

    @slash_command(name = "love")
    async def lo_ve(self, ctx,
                  member: discord.Member):
        embedlove = discord.Embed(title=f"{ctx.author.name} loves {member.display_name}", color =  DEFAULT_COLOR)

        random_link = random.choice(loves)
        embedlove.set_image(url = random_link)
        
        await ctx.respond(embed=embedlove)

    @slash_command(name = "aw")
    async def a_w(self, ctx):
        embedaw = discord.Embed(title=f"awww", color =  DEFAULT_COLOR)

        random_link = random.choice(cuteim)
        embedaw.set_image(url = random_link)

        await ctx.respond(embed=embedaw)

    @slash_command(name = "embed")
    async def em_bed(self, ctx,
                   channel: discord.TextChannel,
                   * , em):
      if channel == None:
        channel = ctx.channel
        embedem = discord.Embed(title=f"{em}", color =  DEFAULT_COLOR)
        await channel.respond(embed=embedem)

    @slash_command(name = "userinfo")
    async def info(self, ctx: commands.Context,
                      member: discord.Member = None):
      button = discord.ui.Button(label=f'Badges', style=discord.ButtonStyle.grey)
      if member == None:
        member = ctx.author
      async def button_callback(interaction: discord.Interaction):
        badges = ""
        if ctx.author.public_flags.hypesquad:
          badges = "Hypesquad"
        elif ctx.author.public_flags.hypesquad_balance:
          badges = "Hypesquad Balance"
        elif ctx.author.public_flags.hypesquad_bravery:
          badges = "Hypesquad Bravery"
        elif ctx.author.public_flags.hypesquad_brilliance:
          badges = "Hypesquad Brilliance"
        elif ctx.author.public_flags.early_supporter:
          badges = "Early Supporter"
        elif ctx.author.public_flags.verified_bot_developer:
          badges = "Verified Bot Developer"
        elif ctx.author.public_flags.partner:
          badges = "Partner"
        elif ctx.author.public_flags.bug_hunter:
          badges = "Bug Hunter"
        for i in badges:
          embed1 = discord.Embed(title='Badges', color = DEFAULT_COLOR)
          embed1.set_author(name=f'{member}', icon_url=f'{member.avatar}')
          await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(color = member.color)
      bannerUser = await self.bot.fetch_user(member.id)
      embed.add_field(name=f"__**General Information**__", value=f"**Name:** {member.name}#{member.discriminator}\n **ID**: {member.id}\n **Account Created:** <t:{int(member.created_at.timestamp())}:D>\n **Joined Server On:** <t:{int(member.joined_at.timestamp())}:D>\n **Highest Role:** {member.top_role.mention}")
      embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
      embed.set_thumbnail(url=member.avatar)
      if not bannerUser.banner:
        pass
      else:
        embed.set_image(url=bannerUser.banner) 
      await ctx.respond(embed=embed)

    @slash_command(name = "av")
    async def ava_tar(self, ctx,                  user: discord.Member = None):
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        avemb = discord.Embed(
            color=DEFAULT_COLOR,
            title=f"{user}'s Avatar",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not user.avatar.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({user.avatar.replace(format='gif')})"
        )
        avemb.set_image(url=user.avatar.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.respond(embed=avemb)


    @slash_command(name = "membercount")
    async def membercount(self, ctx):
        embedmem = discord.Embed(title=f"**Members**", description=f"{ctx.guild.member_count}", color = DEFAULT_COLOR)
        embedmem.set_footer(text=f"{ctx.guild.name}")
        await ctx.respond(embed=embedmem)

    @slash_command(name= "invite")
    async def inv_ite(self, ctx: commands.Context):
      embed = discord.Embed(title=f"**Invite Link:**", description = f" • [Click here to get {self.bot.user.name}](https://discord.com/oauth2/authorize?client_id=1004248513435152484&permissions=1101052116095&scope=bot%20applications.commands)", color =  DEFAULT_COLOR)
      embed.set_footer(text=f"Made by prince")
      embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
      await ctx.respond(embed=embed)

    @slash_command(name= "servericon")
    async def server_icon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=000000,
            title=f"{server}'s Icon",description=f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp})"
            if not server.icon.is_animated()
            else f"[**png**]({png}) | [**jpg**]({jpg}) | [**webp**]({webp}) | [**gif**]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.respond(embed=avemb)

    @slash_command(name=  "serverinfo")
    async def server_info(self, ctx: commands.Context):
      nsfw_level = ''
      button = discord.ui.Button(label=f'Server icon', style=discord.ButtonStyle.url, url=f'{ctx.guild.icon}')
      button2 = discord.ui.Button(label=f'Roles', style=discord.ButtonStyle.grey)
      view = discord.ui.View()
      view.add_item(button)
      view.add_item(button2)
      if ctx.guild.nsfw_level.name == 'default':
        nsfw_level = '**Default**'
      if ctx.guild.nsfw_level.name == 'explicit':
        nsfw_level = '**Explicit**'
      if ctx.guild.nsfw_level.name == 'safe':
        nsfw_level = '**Safe**'
      if ctx.guild.nsfw_level.name == 'age_restricted':
        nsfw_level = '**Age Restricted**'
      async def button2_callback(interaction: discord.Interaction):
        roles = ""
        for i in ctx.guild.roles:
          roles += "• " + str(i.mention) + "\n"
        embed1 = discord.Embed(title=f'{ctx.guild.name}', description=f'{roles}', color=000000)
        await interaction.response.send_message(embed=embed1, ephemeral=True)
      embed = discord.Embed(title=f'{ctx.guild.name} | {ctx.guild.id}', color = 000000)
      embed.add_field(name=f'**__General Information__**', value=f'**Owner:** {ctx.guild.owner.mention} | {ctx.guild.owner.name}\n**Members:**: {ctx.guild.member_count}\n**Created**:____{ctx.guild.created_at.month}/{ctx.guild.created_at.day}/{ctx.guild.created_at.year}__\n**Server Channels**: {len(ctx.guild.channels)}')
      embed.add_field(name=f'**__Additional__**', value=f'NSFW level: **{nsfw_level}**\nVerification level: **{ctx.guild.verification_level.name}**\nExplicit Content Filter: **{ctx.guild.explicit_content_filter.name}**\n**Boost Teir**: {ctx.guild.premium_tier}\nMax Talk Bitrate: **{int(ctx.guild.bitrate_limit)}** kbps\nEmojis: {len(ctx.guild.emojis)}\nStickers: {len(ctx.guild.stickers)}\nBoost count: {ctx.guild.premium_subscription_count}')
      button2.callback = button2_callback
      await ctx.respond(embed=embed, view=view)


    @slash_command(name=  "tru_th")
    async def tr_uth(self, ctx):
      random_msg = random.choice(truths)
      await ctx.respond(f"{random_msg}")

    @slash_command(name= "da_re")
    async def da_re(self, ctx):
      random_msg = random.choice(dares)
      await ctx.respond(f"{random_msg}")


    

   # @slash_command(name= "ping")
   # async def pi_ng(ctx):
   #  embed =  discord.Embed(description=f"<a:network:1006289110765408346> Pong! {round(bot.latency * 1000)}ms", color=0x010101)
  #  embed.set_author(name=f"{ctx.author}")
  #  embed.set_thumbnail(ctx.user.avatar_url)
  #  embed.set_footer(text=f"Zenox")
  # await ctx.channel.respond(embed=embed)

def setup(bot):
    bot.add_cog(fun_s(bot))