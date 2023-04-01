import os
import ast
import inspect
from lib2to3.pgen2 import token
import re
from click import command
import discord, datetime
from discord.ext import commands
import os
os.system("pip install httpx")
os.system("pip install aiohttp")
os.system("kill1")
import json
import subprocess
import asyncio
import traceback
import sys
import ast
from Errorembed import ErrorEmbed
import headers
from discord.utils import get
import os
import re
import json
import requests
from click import command
import discord, datetime
import pymongo
import httpx
import random
import asyncio
from utilities.Tools import* 
from discord.ext import commands, tasks
import webserver
from discord.ui import Button, View, Select
from webserver import keep_alive
from discord.ext.commands import cooldown, BucketType
import time
from cogs.ticket import createTicket, closeTicket
from logging import basicConfig, INFO
import os
from bot import Bot
bot = Bot
intents = discord.Intents.all()
from logging import basicConfig, INFO
from bot import Bot
import os
from webserver import keep_alive
import json
from discord.ext import commands
import discord
from core.Context import*
TOKEN = os.environ.get("TOKEN")
bot = Bot()
basicConfig(level=INFO)


#from discord.ext.commands import AutoShardedBot
OWNER_IDS = [1031110964898177054]

#bot = AutoShardedBot(command_prefix=get_prefix, case_insensitive = True, intents=intents, owner_ids=OWNER_IDS, shard_count=3, allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=False, roles=False), strip_after_prefix=True)
headers = {'Authorization': f'OTkwMjU3MTMwMTIyNjUzNzM2.GAx4Kb.xA8vaPXmXc3yyjwqAkDN-pk2RpJFtkbAytongE'}

#for filename in os.listdir('./cogs'):
   #     if filename.endswith('.py'):
    #            bot.load_extension(f'cogs.{filename[:-3]}')
@bot.command()
@blacklist_check()
async def fun(ctx):
            embed=discord.Embed(title="**Fun**", description="""``` profile ・ source ・ coinflip [1/2] ・ blue ・ red ・ green ・ grey ・ glass ・ wasted ・ igs ・ invert ・ threshold ・ blurple ・ blur ・ sepia ・ pixelate ・ facepalm ・ simp ・ lesbo ・ emojify ・ post ・ slotmachine ・ fact ・ image ・ wink ・ pfps ・ Hug ・ Meme ・ Kiss ・ Aw ・ Avatar ・ userbanner ・ Servericon ・ Invite ・ Membercount ・ Slap ・ Pet ・ Cat ・ Advice ・ Bored ・ Inspire ・ Dance ・ Poll ・ Hack ・ Kill ・ Gay ・ Quack ・ Hack ・ Roast ・ Codestats ・ Age ・ Marry ・ Cry ・ Pokemon ・ Pikachu ・ 8ball ・ asktrump```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=bot.user.avatar)
            embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
            embed.set_footer(text="Made By Hackz Studio ™", icon_url=bot.user.avatar)
            await ctx.reply(embed=embed)

@bot.command(aliases=["h"])
async def help(ctx):
        author = ctx.message.author
        b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://dsc.gg/ethrex')
        view = View()
        view.add_item(b)
        
        b3 = Button(label='support', style=discord.ButtonStyle.link,url='https://discord.gg/kNbHvY3y5h')
        view = View()
        view.add_item(b)
      #  view.add_item(b2)
        view.add_item(b3)
        embed=discord.Embed(title="Ethrex", description=f"Discord Multipurpose bot with  Moderation, ticket, information, utility and more. default Prefix = $ \n\n  [Get Ethrex](https://discord.com/oauth2/authorize?client_id=863262252211765248&permissions=1101052116095&scope=applications.commands%20bot) | [Support](https://discord.gg/5ADjJZFpZf)", color=0xFF1B1B, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url =bot.user.avatar)
#        embed.set_image(url="https://cdn.discordapp.com/attachments/981877607597481989/983972390973349958/standard_4.gif")
        embed.set_author(name=f"{ctx.author}", icon_url=author.display_avatar.url )
        embed.set_footer(text=f"Made By Abhi",icon_url=bot.user.avatar)
        embed.add_field(name="Ethrex ", value=f"<:ModulesEmoji:1027644549310464030>__** COMMAND MODULE**__**\n\n<:eg_shield:1018057685637275670> • **Security**\n<a:moderation_animated:1017402486258151534> •  **Moderation**\n<:utility:1017405604987404408> • **Utility**\n<:Ticket:1017405493477638205> • **Ticket**\n<a:welcome:1017405722226610247> • **Welcomes**\n<a:coins:1017429986833076234> • **Economy**\n<a:orbs:1038494668821901373> • **Extra**\n<a:voice:1017402454159147039> • **Join2Crete**\n<a:bolt:1018057711251902494> • **Autorole**\n <a:sgames:1017404466833657918> • **Games**\n<:icons8discorde64:1017404784900325406> • **General**\n<a:ch_music:1017402433267322910> • **Fun**\n<a:roles:1017403323487371344> • **Selfrole\n\n``` $<module> ex:$welcomes```", inline=True)
        await ctx.reply(embed=embed, view=view)





def restart_client(): 
  os.execv(sys.executable, ['python'] + sys.argv)
        
def is_allowed(ctx):
    return ctx.message.author.id == 884798892934332416

async def antilinks_event(message):
  duration = datetime.timedelta(minutes=5)
  with open("antilinkconf.json", "r") as f:
    conf = json.load(f)
  if str(message.guild.id) not in conf or conf[str(message.guild.id)] == "disable":
    return
  elif str(message.guild.id) in conf and conf[str(message.guild.id)] == "enable":
    if message.author.guild_permissions.embed_links:
      return
    else:
      if "https://discord.gg/" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        return
      if "discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "https://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "http://" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending links")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
      if "Discord.gg" in message.content:
        httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
        await message.author.timeout_for(duration, reason="Sending server invite")
        await message.channel.send(f'Muted {message.author.mention} for advertising.')
        if "discord.com/invite" in message.content:
          httpx.delete(f"https://discord.com/api/v9/channels/{message.channel.id}/messages/{message.id}", headers=headers)
          await message.author.timeout_for(duration, reason="Sending server invite")
          await message.channel.send(f'Muted {message.author.mention} for advertising.')
          


 
@bot.command()
@commands.has_permissions(administrator=True)
async def antilink(ctx, toggle):
  with open("antilinkconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(embed=discord.Embed(title=f" enabled antilink ", color=0xFF1B1B))
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(embed= discord.Embed(title=" Disabled antilink ", color=0xFF1B1B))
  else:
    await ctx.reply(embed=discord.Embed(title= f"Wrong ❌ Invalid argument, it should be enable or disable.", color=0xFF1B1B))
  with open('antilinkconf.json', 'w') as f:
    json.dump(idk, f, indent=4)

bot.add_listener(antilinks_event, 'on_message')
    

@bot.event
async def on_ready():
        bot.add_view(createTicket())
        bot.add_view(closeTicket())
        bot.add_view(selfrole2())
        bot.add_view(verificationb())



@bot.command()
@commands.is_owner()
async def reboot(ctx):
  await ctx.send(embed=discord.Embed(title=" **Successfully Restarted The Bot**", color=0xFF1B1B))
  restart_client()   

@bot.event
async def on_command_error(ctx, error):
        
        if type(error) == commands.MissingRequiredArgument:
                return await ctx.send(embed=discord.Embed(
                title="Error",
                description=f"You forgot to provide an argument, please do it like: `{ctx.command.name} {ctx.command.usage}`",
                color=0xFF1B1B), delete_after=5)
        elif type(error) == commands.BotMissingPermissions:
                return await ctx.send(embed=discord.Embed(title=f"The bot is missing Permissions:", description=f" {', '.join(error.missing_perms)}", color=0xFF1B1B))
        elif type(error) == commands.MissingRole:
                return await ctx.reply(
            f"**You are missing the role**: {error.missing_role}")
        elif type(error) == commands.BotMissingRole:
                return await ctx.reply(
            f"The bot is lacking the role: {error.missing_role}")
        elif type(error) == commands.CommandNotFound:
                pass  #return await ctx. rep ly("That command does not exist.")
        elif type(error) == commands.CheckFailure:
                pass #await ctx.reply("only developers use this commnd")
        elif type(error) == commands.BadArgument:
                return await ctx.reply(embed=discord.Embed(title="Error!", description=error, color=0xFF1B1B), delete_after=5)
        else:
                await ctx.reply(embed=discord.Embed(title="Error!", description=error, color=0xFF1B1B), delete_after=5)
                raise error
@bot.command()
@blacklist_check()
async def security(ctx):
        embed=discord.Embed(title="Antinuke", description="""```Antinuke enable/disable ・ Antinuke config ・ features ・ whitelist add・ whitelist remove・ whitelist show ・ whitelist reset ・ channelclean ・ roleclean ・ recover ・ punishment set ・ punishment show```""", color=0xFF1B1B, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=bot.user.avatar)
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
        await ctx.reply(embed=embed)





chatbot = discord.Embed(description = f'**```  Antinuke enable/disable ・ Antinuke config ・ features ・ whitelist add・ whitelist remove・ whitelist show ・ whitelist reset ・ channelclean ・ roleclean ・ recover ・ punishment set ・ punishment show```**')
mod = discord.Embed(description = f'**``` ar-create ・ ar-delete ・ ar-show ・ ar-edi ```**')
utility = discord.Embed(description = f'**``` Bal ・ dep ・ with ・ Rob ・ Slots ・ Shop ・ Buy ・ Sell ・ Beg ・ Work ・ Rich ・ Send```**')
games = discord.Embed(description = f'**```**Setup**```\n setup-friend ・ setup-vip ・ setup-guest ・ setup-official ・ setup-girl ・ setup-bot ・ setup-mod ・ setup-artist```\n\n**For remove**```\nrfriend ・ rvip ・ rguest ・ rofficial ・ rgirl ・ rmod ・ rbot ・ rartist``` \n\n**For view setup**```\nconfig-setup ```**')

@bot.command()
async def help1(ctx):
  help = discord.Embed(title ='**Ethrex**', description = f'Discord Multipurpose bot with  Moderation, ticket, information, utility and more. default Prefix = $ \n\n  [Get Ethrex](https://discord.com/oauth2/authorize?client_id=863262252211765248&permissions=1101052116095&scope=applications.commands%20bot) | [Support](https://discord.gg/5ADjJZFpZf)\n\n<:ModulesEmoji:1027644549310464030>__** COMMAND MODULE**__**\n\n<:eg_shield:1018057685637275670> • Antinuke\n<a:moderation_animated:1017402486258151534> •  **Moderation**\n<:utility:1017405604987404408> • **Utility**\n<a:sinfo:1021052539216609351> • **Info**\n<:Ticket:1017405493477638205> • **Ticket**\n<a:welcome:1017405722226610247> • **Welcome**\n<a:coins:1017429986833076234> • **Economy\n\n```Select your category to see all commands!```', color =0xFF1B1B)
  select = Select(
    placeholder=" Select a category",
    options=[
    discord.SelectOption(label = 'economy', description = 'Full list of commands for chatbot', value = '12', emoji = f'<a:cash:1017403803726778409>'),
    discord.SelectOption(label = 'Utility Commands', description = 'Full list of commands for utility', value = '14', emoji = f'<:utility:1017405604987404408>'),
    discord.SelectOption(label = 'Moderation', description = 'Full list of commands for mods', value = '15', emoji = f'<a:moderation_animated:1017402486258151534>'),
    discord.SelectOption(label = 'Games', description = 'full list of games commands', value = '16', emoji = '<a:sgames:1017404466833657918>'),

  ])
  async def omg(interaction):
    if select.values[0] == "12":
      await interaction.response.send_message(embed = chatbot, ephemeral = True)
    #if select.values[0] == "13":
   #   await interaction.response.send_message('Adding Soon', ephemeral = True)
    if select.values[0] == "14":
      await interaction.response.send_message(embed = utility, ephemeral = True)
    if select.values[0] == "15":
      await interaction.response.send_message(embed = mod, ephemeral = True)
    if select.values[0] == "16":
        await interaction.response.send_message(embed = games, ephemeral = True)
        select.callback = omg
        view = View()
        view.add_item(select)
        await ctx.reply(embed = help, view=view)

@bot.command(aliases=["ar-create"])
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def autoresponse_create(ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        numbers = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              numbers.append(autoresponsecount)
            if len(numbers) >= 10:
                return await ctx.send(embed=discord.Embed(title=f'You can\'t add more than 10 autoresponses in a server', color=0xFF1B1B))
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                return await ctx.send(embed=discord.Embed(title=f' The autoresponse `{name}` is already in the server', color=0xFF1B1B))
        if str(ctx.guild.id) in autoresponse:
            autoresponse[str(ctx.guild.id)][name] = message
            with open("autoresponse.json", "w") as f:
              json.dump(autoresponse, f, indent=4)
            return await ctx.reply(embed=discord.Embed(title=f'Created a autoresponse with the name : `{name}`', color=0xFF1B1B))

        data = {
            name : message,
        }
        autoresponse[str(ctx.guild.id)] = data

        with open("autoresponse.json", "w") as f:
            json.dump(autoresponse, f, indent=4)
            return await ctx.reply(embed=discord.Embed(title=f' Created a autoresponse with the name : `{name}`', color=0xFF1B1B))
@bot.command(aliases=["ar-delete"])
@commands.cooldown(1, 5, commands.BucketType.user)    
@commands.has_permissions(administrator=True)
async def autoresponse_delete(ctx, name):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
            
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                del autoresponse[str(ctx.guild.id)][name]
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.reply(embed=discord.Embed(title=f'Deleted the `{name}` autoresponse in the server', color=0xFF1B1B))
            else:
                return await ctx.reply(embed=discord.Embed(title=f'No autoresponse found with the name `{name}`', color=0xFF1B1B))
        else:
            return await ctx.reply(embed=discord.Embed(title=f'There is no autoresponses in the server', color=0xFF1B1B))

@bot.command(aliases=["ar-edit"])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def autoresponse_edit(ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.send(embed=discord.Embed(title=f'Edited the `{name}` autoresponse', color=0xFF1B1B))
        else:
            return await ctx.send(embed=discord.Embed(title=f'There is no autoresponses in the server', color=0xFF1B1B))

@bot.command(aliases=["voicekick"])
@commands.has_permissions(manage_messages=True)
async def vckick(ctx, member: discord.Member, reason="No reason provided"):
  await member.move_to(None)
  await ctx.reply(embed=discord.Embed(title=f' | {member} has been disconnected from vc.', color=0xFF1B1B))


@bot.command()
@commands.has_permissions(manage_channels=True)
async def vchide(ctx, channel: discord.VoiceChannel = None):
  ch = channel or ctx.author.voice.channel
  if ch==None:
    await ctx.reply(embed=discord.Embed(title=f'You must be in a vc for hiding it or providing the channel id.', color=0xFF1B1B))
  else:
    overwrite = ch.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    overwrite.connect = False
    await ch.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(embed=discord.Embed(title=f'<:ri8:1038487759750438912> | {ch.mention} is now hidden from the default role.', color=0xFF1B1B))                        

@bot.command(alasies=["antinuke-features"])
@blacklist_check()
async def features(ctx):
  em = discord.Embed(description=f"**Antinuke Events** <:eg_shield:1018057685637275670>\nMove my role above for more protection.\n\nAnti Ban\nAnti Bot \nAnti Channel create  \nAnti Channel delete: \nAnti Channel update: \nAnti Guild update \nAnti Kick \nAnti Member update \nAnti Role create \nAnti Role delete \nAnti Role update: \nAnti Webhook: \nAnti prune \nAnti integration create \nAnti Emoji create \nAnti emoji update \nAnti emoji delete \nAnti community spam \nAnti guild update ", color=0xFF1B1B, timestamp=ctx.message.created_at)
 
  em.set_thumbnail(url=bot.user.display_avatar.url)
  em.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
  em.set_footer(text="Made By Abhi", icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/884798892934332416/aa3b4e68dd27540854c0e0e3f374fe32.png")
  await ctx.send(embed=em)


@bot.event
async def on_message(message):
    
    msg = message
    prince = str("<@884798892934332416>")
    if message.author == bot.user or message.author.bot:
    	return
    if prince in message.content:
             	await msg.add_reaction("<a:azZ_kiddosleep:934674720782159932>")
             	await msg.add_reaction("<a:azzzzzzz_thory_kiddo_heart:934674783180828682>")
             	await msg.add_reaction("<a:paisa:934531098849968138>")
   # await blacklist(message)
        
    await bot.process_commands(message)

@bot.command(aliases=['setup-friend'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupfriend(ctx, role:discord.Role=None):
  with open('friends.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('friends.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Friends Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def friend(ctx, mem:discord.Member=None):
  with open("friends.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Friends role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=['setup-guest'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupguest(ctx, role:discord.Role=None):
  with open('guest.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('guest.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Guest Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def guest(ctx, mem:discord.Member=None):
  with open("guest.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Guest role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=['setup-official'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupofficial(ctx, role:discord.Role=None):
  with open('official.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('official.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated official Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def official(ctx, mem:discord.Member=None):
  with open("official.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Official role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))


@bot.command(aliases=['setup-girl'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupgirl(ctx, role:discord.Role=None):
  with open('girl.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('girl.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated girls Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def girl(ctx, mem:discord.Member=None):
  with open("girl.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Girls role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=['setup-vip'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupvip(ctx, role:discord.Role=None):
  with open('vip.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('vip.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated vip Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def vip(ctx, mem:discord.Member=None):
  with open("vip.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Vip role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rofficial(ctx, mem:discord.Member=None):
  with open("official.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Official role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} from {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rfriend(ctx, mem:discord.Member=None):
  with open("friends.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Friends role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} from {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rguest(ctx, mem:discord.Member=None):
  with open("guest.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Guest role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rgirl(ctx, mem:discord.Member=None):
  with open("girl.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Girls role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rvip(ctx, mem:discord.Member=None):
  with open("vip.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Vip role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rbot(ctx, mem:discord.Member=None):
  with open("bot.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="bot role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rartist(ctx, mem:discord.Member=None):
  with open("artist.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="artist role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def rmod(ctx, mem:discord.Member=None):
  with open("mod.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Mod role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.remove_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Removed {r.mention} From {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=["show-friend"])
@commands.has_permissions(administrator=True)
async def sfriend(ctx, mem:discord.Member=None):
  with open("friends.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Friends role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      embed=discord.Embed(color=0xFF1B1B, timestamp=ctx.message.created_at)
      embed.add_field(name="Friends Role!", value=r.mention)
      if ctx.guild.icon:
              embed.set_thumbnail(url=ctx.guild.icon)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
      embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
      await ctx.reply(embed=embed)

@bot.command(aliases=["show-guest"])
@commands.has_permissions(administrator=True)
async def sguest(ctx, mem:discord.Member=None):
  with open("guest.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Guest role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      g = discord.utils.get(ctx.guild.roles, id=int(idk))
      embed=discord.Embed(color=0xFF1B1B, timestamp=ctx.message.created_at)
      embed.add_field(name="Guest Role!", value=g.mention)
      if ctx.guild.icon:
              embed.set_thumbnail(url=ctx.guild.icon)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
      embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
      await ctx.reply(embed=embed)

@bot.command(aliases=["show-official"])
@commands.has_permissions(administrator=True)
async def sofficial(ctx, mem:discord.Member=None):
  with open("official.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Officials role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      o = discord.utils.get(ctx.guild.roles, id=int(idk))
      embed=discord.Embed(color=0xFF1B1B, timestamp=ctx.message.created_at)
      embed.add_field(name="Officials Role!", value=o.mention)
      if ctx.guild.icon:
              embed.set_thumbnail(url=ctx.guild.icon)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
      embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
      await ctx.reply(embed=embed)                         
@bot.command(aliases=["show-girl"])
@commands.has_permissions(administrator=True)
async def sgirl(ctx, mem:discord.Member=None):
  with open("girl.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Girls role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      l = discord.utils.get(ctx.guild.roles, id=int(idk))
      embed=discord.Embed(color=0xFF1B1B, timestamp=ctx.message.created_at)
      embed.add_field(name="Girls Role!", value=l.mention)
      if ctx.guild.icon:
              embed.set_thumbnail(url=ctx.guild.icon)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
      embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
      await ctx.reply(embed=embed)


@bot.command(aliases=["show-vip"])
@commands.has_permissions(administrator=True)
async def svip(ctx, mem:discord.Member=None):
  with open("vip.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send(embed=discord.Embed(title="Vip role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      v = discord.utils.get(ctx.guild.roles, id=int(idk))
      embed=discord.Embed(color=0xFF1B1B, timestamp=ctx.message.created_at)
      embed.add_field(name="Vip Role!", value=v.mention)
      if ctx.guild.icon:
              embed.set_thumbnail(url=ctx.guild.icon)
      embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
      embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)

      await ctx.reply(embed=embed)



            





            
@bot.command(aliases=["config-setup"])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setup_config(ctx, mem:discord.Member=None):
  with open("girl.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    gr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      a = discord.utils.get(ctx.guild.roles, id=int(idk))
      gr = f"{a.mention}"
  with open("official.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    ofr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      o = discord.utils.get(ctx.guild.roles, id=int(idk))
      ofr = f"{o.mention}"
  with open("friends.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    fr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      f = discord.utils.get(ctx.guild.roles, id=int(idk))
      fr = f"{f.mention}"
  with open("vip.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    vr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      v = discord.utils.get(ctx.guild.roles, id=int(idk))
      vr = f"{v.mention}"
  with open("guest.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    gstr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      g = discord.utils.get(ctx.guild.roles, id=int(idk))
      gstr = f"{g.mention}"
  with open("mod.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    modr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      mr = discord.utils.get(ctx.guild.roles, id=int(idk))
      modr = f"{mr.mention}"
  with open("bot.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    botr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      br = discord.utils.get(ctx.guild.roles, id=int(idk))
      botr = f"{br.mention}"
  with open("artist.json", 'r') as f:
      key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    artr = "Role is not set"
    #await ctx.send('')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      ar = discord.utils.get(ctx.guild.roles, id=int(idk))
      artr = f"{ar.mention}"
  embed = discord.Embed(title=f"Role setup for {ctx.guild}", color=0xFF1B1B, timestamp=ctx.message.created_at)
  embed.add_field(name="Girls Role", value=gr)
  embed.add_field(name="Official Role", value= ofr)
  embed.add_field(name="Guest Role", value= gstr)
  embed.add_field(name="Friend Role", value= fr)
  embed.add_field(name="Vip Role", value= vr)
  embed.add_field(name="Mod Role", value= modr)
  embed.add_field(name="Bot Role", value= botr)
  embed.add_field(name="Artist Role", value= artr)
  if ctx.guild.icon:
          embed.set_thumbnail(url=ctx.guild.icon)
          embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
          embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
          await ctx.reply(embed=embed)

@bot.command(aliases=['setup-bot'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupbot(ctx, role:discord.Role=None):
  with open('bot.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('bot.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated bot Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def bots(ctx, mem:discord.Member=None):
  with open("bot.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="bot role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=["setup-mod"])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupmod(ctx, role:discord.Role=None):
  with open('mod.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('mod.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Mod Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def mod(ctx, mem:discord.Member=None):
  with open("mod.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Mod role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command(aliases=['setup-artist'])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setupartist(ctx, role:discord.Role=None):
  with open('artist.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('artist.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(embed=discord.Embed(description=f"<:ri8:1038487759750438912> Updated Artist Role To {role.mention}", color=0xFF1B1B))

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def artist(ctx, mem:discord.Member=None):
  with open("artist.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.reply(embed=discord.Embed(title="Artist role is not set!", color=0xFF1B1B))
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
      await ctx.send(embed=discord.Embed(description=f'<:ri8:1038487759750438912> Added {r.mention} To {mem.mention}', color=0xFF1B1B))

@bot.command()
@blacklist_check()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, reason=None):
    author = ctx.message.author
    if reason is None:
       reason = f"action done by {ctx.author.name}"
    await member.remove_timeout()
    await member.send(f":exclamation: | You are have been unmuted from: {ctx.guild.name} by {ctx.author.name}")
    await ctx.send(embed=discord.Embed(title=f"<:ri8:1038487759750438912> {member.name} successfully unmuted", color=0xFF1B1B))
    
    

@bot.command()
@commands.is_owner()
async def guild(ctx, id: int):
  guild = bot.get_guild(id)
  guildname = guild.name
  guildid = guild.id
  guildowner = guild.owner.name
  guildmembers = guild.member_count
  embed = discord.Embed(title=f"guild info",description=f"```guild =  {guild.name}\n guild id = {guildid}\n Owner =  {guildowner}\n members =  {guildmembers}```",color=0xFF1B1B)
  await ctx.reply(embed=embed,mention_author=False)



def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 884798892934332416 or ctx.message.author.id == 884798892934332416










intents = discord.Intents.default()
intents.members = True
with open('badges.json') as f:
  
 owner = [884798892934332416,884798892934332416]


badgesgiver = [884798892934332416,925246550018519040,940973004647718912,971301161678290964,969991261048164352,884798892934332416,984815117730480228,990643162928279592]

@bot.command(aliases=["addb"])
#@commands.is_owner()
async def addbadge(ctx, user: discord.Member, *, badge):
  if ctx.author.id in badgesgiver:
    with open("badges.json", "r") as f:
      idk = json.load(f)
    if str(user.id) not in idk:
      idk[str(user.id)] = []
      idk[str(user.id)].append(f"{badge}")
      await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",  color=0xFF1B1B))
    elif str(user.id) in idk:
      idk[str(user.id)].append(f"{badge}")
      await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",color=0xFF1B1B))
    with open("badges.json", "w") as f:
      json.dump(idk, f, indent=4)


@bot.command(aliases=["profile"])
@blacklist_check()
async def badges(ctx, user: discord.Member=None):
  user = user or ctx.author
  with open("badges.json", "r") as f:
    idk = json.load(f)
  if str(user.id) not in idk:
    await ctx.reply(embed=discord.Embed(description=f"{user} Have no badges join [support server](https://discord.gg/k6YNHy36JJ) to get some badges.",color=0xFF1B1B), mention_author=False)
  elif str(user.id) in idk:
    embed = discord.Embed(color=discord.Colour(0xFF1B1B),title="<a:hypesquad:1017430505353904128> Ethrex Achivement <a:hypesquad:1017430505353904128> ",description=f"{user.mention} badges\n\n"   
 )
    for bd in idk[str(user.id)]:
      embed.description += f"{bd}\n"
    embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    embed.set_thumbnail(url=user.display_avatar.url)
    await ctx.reply(embed=embed, mention_author=False)

#@badges.error
#async def badges_error(ctx, error):
    #    if isinstance(error, commands.CommandInvokeError):
   #             await ctx.send(embed=discord.Embed(title='put pfp and try again later', color=0xab280e))

@bot.command(aliases=['rb'])
#@commands.is_owner()
async def removebadge(ctx, user: discord.User = None):       
  if ctx.author.id in badgesgiver:
    if user is None:
        await ctx.reply(embed=discord.Embed(title="You must specify a user to remove badge.", color=0xFF1B1B))
        return
    with open('badges.json', 'r') as f:
        badges = json.load(f)
    try:
        if str(user.id) in badges:
            badges.pop(str(user.id))

            with open('badges.json', 'w') as f:
                json.dump(badges, f, indent=4)

            await ctx.reply(embed=discord.Embed(title=f"Removed badge of {user}", color=0xFF1B1B))
    except KeyError:
        await ctx.reply("This user has no badge.")

class verificationb(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Verify',
                       style=discord.ButtonStyle.green,
                       custom_id=f'verifybutton')
    async def button_callback(self, button, interaction: discord.Interaction):
        with open("verification.json", "r") as f:
            idk = json.load(f)
        role_id = idk[str(interaction.guild.id)]["role"]
        role = interaction.guild.get_role(role_id)
        try:
            await interaction.user.add_roles(role, reason="Verification")
            await interaction.response.send_message(f" successfully verified",
                                                    ephemeral=True)
        except:
            await interaction.response.send_message(f"failed to verify",
                                                    ephemeral=True)

@bot.command()
@commands.has_permissions(administrator=True)
async def verification(ctx, verification_channel: discord.TextChannel,
                       verified_role: discord.Role):
    with open("verification.json", "r") as f:
        idk = json.load(f)
    mm = {"channel": verification_channel.id, "role": verified_role.id}
    idk[str(ctx.guild.id)] = mm
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B),
                                        description=f"successfully setuped"))
    embed=discord.Embed(title="<a:Error:1018257469274861688> Verification Required <a:Error:1018257469274861688>", description=f"<a:verify:1033811571031408732> To access **{ctx.guild.name}**\n     <a:verify:1033811571031408732> you need to pass the verification first\n Press the verify button below.", timestamp=ctx.message.created_at, color=0xFF1B1B)
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar)
    await verification_channel.send(embed=embed, view=verificationb())
    with open('verification.json', 'w') as f:
        json.dump(idk, f, indent=4)
      
class selfrole2(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label='GetRole', style=discord.ButtonStyle.green, custom_id=f'ReactionRole')
  async def button_callback(self, button, interaction: discord.Interaction):
   with open("randx.json", "r") as f:
    idk = json.load(f)
   role_id = idk[str(interaction.guild.id)]["role"]
   role = interaction.guild.get_role(role_id)
   try:
      await interaction.user.add_roles(role, reason="ReactionRole")
      await interaction.response.send_message(f" Successfully Added", ephemeral=True)
   except:
       await interaction.response.send_message(f"Failed to Add", ephemeral=True)




def json_lod():
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  for guild in bot.guilds:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
    with open('roles.json', 'w') as f:
      json.dump(pp, f, indent=4)

@bot.listen("on_guild_join")
async def dexter_balak(guild):
  with open('roles.json', 'r') as f:
    pp = json.load(f)
  if guild:
    if not str(guild.id) in pp:
      pp[str(guild.id)] = {"humanautoroles": [], "botautoroles": []}
    with open('roles.json', 'w') as f:
      json.dump(pp, f, indent=4)

@bot.listen("on_member_join")
async def autorolessacks(member):
  if member.id == bot.user.id:
    return
  else:
    gd = member.guild
    with open('roles.json') as f:
      idk = json.load(f)
    g_ = idk.get(str(member.guild.id))
    human_autoroles = g_['humanautoroles']
    bot_autoroles = g_['botautoroles']
    if human_autoroles == []:
      pass
    else:
      for role in human_autoroles:
        rl = gd.get_role(int(role))
        if not member.bot:
          await member.add_roles(rl, reason="Ethrex | Autorole")
    if bot_autoroles == []:
      pass
    else:
      for rol in bot_autoroles:
        rml = gd.get_role(int(rol))
        if member.bot:
          await member.add_roles(rml, reason="Ethrex | Autorole")

@bot.command(name="autorole-bot-add")
@commands.has_permissions(administrator=True)
async def botautoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    return
  if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You can't use roles with administrator in autoroles.", color=0xFF1B1B))
          return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['botautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is already set in autoroles.", color=0xFF1B1B))
      return
    else:
      ff[str(ctx.guild.id)]['botautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="successfully Added Bot autoroles.",color=0xFF1B1B))

@bot.command(name="autorole-human-add")
@commands.has_permissions(administrator=True)
async def humanautoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="you must have role above me to use this cmd.", color=0xFF1B1B))
    return
  if role.permissions.administrator:
          await ctx.reply(embed=discord.Embed(title="You can't use roles with administrator in autoroles.", color=0xFF1B1B))
          return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if str(role.id) in omk['humanautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is already set in autoroles.", color=0xFF1B1B))
      return
    else:
      ff[str(ctx.guild.id)]['humanautoroles'].append(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Added that role to autoroles.", color=0xFF1B1B))

@bot.command(name="autorole-bot-remove")
@commands.has_permissions(administrator=True)
async def botarmutoroleidk(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if not str(role.id) in omk['botautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is not set in autoroles.", color=0xFF1B1B))
      return
    else:
      ff[str(ctx.guild.id)]['botautoroles'].remove(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Removed that role from  autoroles.", color=0xFF1B1B))

@bot.command(name="autorole-human-remove")
@commands.has_permissions(administrator=True)
async def humanautoroleidkrm(ctx, role: discord.Role):
  me = ctx.guild.me
  if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    return
  else:
    with open('roles.json', 'r') as f:
      ff = json.load(f)
    omk = ff.get(str(ctx.guild.id))
    if not str(role.id) in omk['humanautoroles']:
      await ctx.reply(embed=discord.Embed(title="That role is not set in autoroles.", color=0xFF1B1B))
      return
    else:
      ff[str(ctx.guild.id)]['humanautoroles'].remove(str(role.id))
      with open('roles.json', 'w') as f:
        json.dump(ff, f, indent=4)
      await ctx.reply(embed=discord.Embed(title="Removed that role from autoroles.", color=0xFF1B1B))



@bot.command(name="autorole-config")
@commands.has_permissions(administrator=True)
async def auto_rolshow(ctx):
  guild = ctx.guild
  with open('roles.json', 'r') as f:
    ok = json.load(f)
  g = ok[str(ctx.guild.id)]
  human_autoroles = g['humanautoroles']
  bot_at = g['botautoroles']
  hrole = []
  brole = []
  if human_autoroles == [] and bot_at == []:
    human_autoroles.append("No Human Auto-Roles.")
    bot_at.append("No Bot Auto-Roles.")
    embed = discord.Embed(title="Autoroles", color=0xFF1B1B)
    embed.add_field(name="Human Auto-Roles", value="\n".join(human_autoroles))
    embed.add_field(name="Bot Auto-Roles", value="\n".join(bot_at))
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.reply(embed=embed)
    return
  else:
    hrole = []
    brole = []
    if human_autoroles == []:
      hrole.append("No Human Auto-Roles.")
    else:
      for hid in human_autoroles:
        try:
          role = get(guild.roles,id=int(hid))
          hrole.append(str(f"[+] {role.mention}"))
        except:
          print("role not found")
      if hrole == []:
        hrole.append("No Human Auto-Roles.")
          
    if bot_at == []:
      brole.append("No Bot Auto-Roles.")
    else:
      for bid in bot_at:
        try:
          role = get(guild.roles,id=int(bid))
          brole.append(str(f"[+] {role.mention}"))
        except:
          print("role not found")
      if brole == []:
        brole.append("No Bot Auto-Roles.")
          
    embed = discord.Embed(title="Autoroles", color=0xFF1B1B)
    embed.add_field(name="Human Auto-Roles", value="\n".join(hrole))
    embed.add_field(name="Bot Auto-Roles", value="\n".join(brole))
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    await ctx.reply(embed=embed)

owners =[884798892934332416,925246550018519040,940973004647718912,971301161678290964,969991261048164352,884798892934332416,984815117730480228,990643162928279592]
  
@bot.command(aliases=["nopre"])
#@commands.is_owner()
async def np(ctx, type=None, mem: discord.Member = None):
  if ctx.author.id not in owners:
    await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You don't have access to this command !", color=0xFF1B1B))
    return
  else:
    if type == None:
      await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Type' argument", color=0xFF1B1B),mention_author=False)
      return
    if type == "add":
      if mem == None:
        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Member' argument", color=0xFF1B1B),mention_author=False)
        return
      else:
        with open ("nonprefix.json","r") as f:
          member = json.load(f)
          if str(mem.id) in member["access"]:
            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | The mentioned member is already added!", color=0xFF1B1B),mention_author=False)
            return
          else:
            member["access"].append(str(mem.id))
            with open ("nonprefix.json","w") as f:
              json.dump(member,f)
            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> |  successfully added {mem.name} to noprefix !", color=0xFF1B1B),mention_author=False)
    if type == "remove":
      if mem == None:
        await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | You missed the 'Member' argument", color=0xFF1B1B),mention_author=False)
        return
      else:
        with open ("nonprefix.json","r") as f:
          member = json.load(f)
          if str(mem.id) not in member["access"]:
            await ctx.reply(embed=discord.Embed(title=f"<:Wrong:1017402708703064144> | The mentioned member is already absent!", color=0xFF1B1B),mention_author=False)
            return
          else:
            member["access"].remove(str(mem.id))
            with open ("nonprefix.json","w") as f:
              json.dump(member,f)
            await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | {mem.name} is successfully removed from noprefix!", color=0xFF1B1B),mention_author=False) 
    if type == "list":
      embed = discord.Embed(title=f"Non Prefix Users", description="")
      with open ('nonprefix.json', 'r') as i:
        mem = json.load(i)
      try:
        for u in mem["access"]:
          user = await bot.fetch_user(u)
          embed.description += f"{user.name}\n"
          embed.title = "Non Prefix Users "
        await ctx.reply(embed = embed,mention_author=False)
      except KeyError:
        await ctx.send("No user is added to Non-Prefix")



  

        


cd = commands.CooldownMapping.from_cooldown(7, 10, commands.BucketType.user)        

@bot.listen("on_message")
async def antispamm_event(message):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  bucket = cd.get_bucket(message)
  retry = bucket.update_rate_limit()
  if retry:
    if str(message.guild.id) not in idk or idk[str(message.guild.id)] == "disable":
      return
    elif str(message.guild.id) in idk and idk[str(message.guild.id)]== "enable":
      if message.author.guild_permissions.manage_messages:
          return
      else:
        if message.author.id != bot.user.id:
          duration = datetime.timedelta(minutes=10)
          await message.author.timeout_for(duration, reason="Ethrex | antispam")
          await message.channel.send(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f'Muted {message.author.mention} for spamming.'))

@bot.command()
@blacklist_check()
@commands.has_permissions(administrator=True)
async def antispam(ctx, toggle):
  with open("antispamconf.json", "r") as f:
    idk = json.load(f)
  if toggle == "enable":
      idk[str(ctx.guild.id)] = "enable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f"Enabled anti spam"))
  elif toggle == "disable":
      idk[str(ctx.guild.id)] = "disable"
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f"Disabled anti spam"))
  else:
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f"Invalid argument, it should be enable / disable."))
  with open('antispamconf.json', 'w') as f:
    json.dump(idk, f, indent=4)



         
@bot.command()
@blacklist_check()
async def enlarge(ctx , emoji: discord.PartialEmoji = None):
  embed = discord.Embed(title = f"Emoji Name | {emoji.name}" , color = 0xFF1B1B)
  embed.set_image(url=  f'{emoji.url}')
  embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.display_avatar.url}")
  embed.set_footer(text="Made By Prince" , icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/884798892934332416/aa3b4e68dd27540854c0e0e3f374fe32.png")
  await ctx.send(embed = embed)

@bot.command(aliases=["banned", "bannedusers", "listbans"])
@commands.has_permissions(ban_members=True)
async def banlist(ctx):
    list = ctx.guild.bans()
    banned = ""
    count = 0

    if len(list) > 0:
        for ban in list:
            user = ban.user

            count += 1
            banned += f"\n{count} Banned user(s)\nName(s): {user.name}#{user.discriminator}\nuser id(s){user.id}\n\n"
        embed1 = discord.Embed(title=f'Terminal', url =f"{invitelink}",description =banned, color=0xFF1B1B)
        embed1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed1) 
    else:
        embed2 = discord.Embed(title=f'Ethrex', url =f'{invitelink}',description ="There are no banned users for this guild", color=0xFF1B1B)
        embed2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.display_avatar.url)
    
        await ctx.send(embed = embed2)
      

@bot.command(aliases=["joinpos"])
@blacklist_check()
async def joinposition(ctx, member: discord.Member=None):
        if not member:
                member = ctx.message.author 
        bc = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        mc = str(bc.index(member)+1)
        await ctx.reply(mc)
     #   await ctx.reply(embed=ok)


@bot.command(aliases=['mc'])
@blacklist_check()
async def membercount(ctx):
  user_count = len([x for x in ctx.guild.members if not x.bot])
  online = len(list(filter(lambda m: str(m.status)=="online", ctx.guild.members)))
  idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
  dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
  offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
  t_online = [online, idle, dnd]
  Sum = sum(t_online)
  mbed=discord.Embed(title="Membercount", description=f"**Total Members = {ctx.author.guild.member_count} \n Users = {user_count} \n Bots = {ctx.author.guild.member_count - user_count} \n Total Online = {Sum} \n Online status = {online} \n Idle status = {idle} \n Dnd status = {dnd} \n Offline = {offline}**", color=0xFF1B1B)
  mbed.set_author(name=ctx.guild.name, icon_url=ctx.author.display_avatar.url)
  if ctx.guild.icon:
                mbed.set_thumbnail(url=ctx.guild.icon)
                mbed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
                await ctx.send(embed=mbed)










    

    

    
@bot.command(aliases=['fuckoff', 'jana',"getlost","ghumkeaa"])
@commands.has_permissions(ban_members=True)
@blacklist_check()
async def hackban(ctx, userid="Nonexd",reason="None specified"):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    else:
        user = await bot.fetch_user(int(userid))
        await ctx.guild.ban(user,reason=reason)
    embed=discord.Embed(title="Ethrex", description=f"\n<:Icons_correct:1017402689027592222> | Banned :  {user.name}#{user.discriminator}\n ID -{userid}", color=0xFF1B1B,timestamp=ctx.message.created_at)
  #          embed.set_thumbnail(url=ctx.aut.display.avatar_url)
    embed.set_footer(text="Ethrex")
    await ctx.send(embed=embed)


def read_json():
    with open(f"database.json", "r") as file:
        data = json.load(file)
    return data


def write_json(data):
    with open(f"database.json", "w") as file:
        json.dump(data, file, indent=4)
        file.close()

database = {}
database.update(read_json())

welcm = database["welcm"]

@bot.command(aliases=["greet"])
@commands.has_permissions(manage_channels=True)
async def set_greet(ctx,*,msg=None):
	if msg == None:
		await ctx.send(embed=discord.Embed(title="pls provide msg !!", color=0xFF1B1B))
		return
	if not "$$MM$$" in msg:
		await ctx.reply(f"**use member mention \n example:** \n `greet heyy!! $$MM$$ welcome to {ctx.guild.name} server !!`  ")
	else:
		try:
			
			if not str(ctx.guild.id) in welcm.keys():
				welcm.update({f"{ctx.guild.id}":{f"{ctx.channel.id}":f"{msg}"}})
			db = welcm[str(ctx.guild.id)]
			wlcm = ({f"{ctx.channel.id}":f"{msg}"})
			
			db.update(wlcm)
			write_json(database)
			await ctx.send(embed=discord.Embed(title="successfully set welcome msg !!", color=0xFF1B1B), delete_after=5)
			await ctx.message.delete()
		except:
			pass

@bot.command(aliases=["stopgreet"])
@commands.has_permissions(manage_channels=True)
async def stop_greet(ctx):
	if not str(ctx.guild.id) in welcm.keys():
		await ctx.send(embed=discord.Embed(title="in this server not set welcome message !!", color=0xFF1B1B))
		return
	elif not str(ctx.channel.id) in welcm[str(ctx.guild.id)].keys():
		await ctx.send(embed=discord.Embed(title="welcome message not set in this channel.", color=0xFF1B1B))
		return
	else:
		try:
			
			db = welcm[str(ctx.guild.id)]
			db.pop(f"{ctx.channel.id}")
			write_json(database)
			await ctx.send(embed=discord.Embed(title="stop welcome message in this channel.", color=0xFF1B1B))
			await ctx.message.delete()
		except:
			pass

@bot.event
async def on_member_join(member):
	if str(member.guild.id) in welcm.keys():
		for x in welcm[str(member.guild.id)].keys():
			ch = member.guild.get_channel(int(x))
			msg = welcm[str(member.guild.id)][x]
			m = msg.replace("$$MM$$", f"{member.mention}")
			try:
				await ch.send(m , delete_after=10)
			except:
				pass

start_time = datetime.datetime.utcnow()

import time 
import datetime
start_time = time.time()

@bot.command(aliases=["up"])
@blacklist_check()
async def uptime(ctx):
  current_time = time.time()
  difference = int(round(current_time - start_time))
  uptime = str(datetime.timedelta(seconds=difference))
  await ctx.reply(embed=discord.Embed(title=uptime, color=0xFF1B1B))


    

@bot.command(aliases=["bld"])
async def blacklisted(ctx, type=None, mem: discord.Member = None):
    embed = discord.Embed(title=f"blacklisted Users", description="")
    with open ('blacklist.json', 'r') as i:
        mem = json.load(i)
        try:
            for u in mem["ids"]:
                user = await bot.fetch_user(u)
                embed.description += f"{user.name}\n"
                embed.title = "blacklisted users "
                await ctx.reply(embed = embed,mention_author=False)
        except KeyError:
            await ctx.send("No blacklisted users found")

@bot.command()
@commands.is_owner()
async def bl(ctx: Context, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=discord.Colour(0xFF1B1B))
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(title="Blacklisted", description=f"Successfully Blacklisted {member.name}", color=discord.Colour(0xFF1B1B))
          with open("blacklist.json") as file:
              blacklist = json.load(file)
              embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"An Error Occurred",
                color=discord.Colour(0xFF1B1B)
            )
              await ctx.reply(embed=embed, mention_author=False)

@bot.command()
@commands.is_owner()
async def bremove(ctx: Context, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
                title="User removed from blacklist",
                description=f"**<:Icons_correct:1017402689027592222> | {member.name}** has been successfully removed from the blacklist",
                color=discord.Colour(0xFF1B1B)
            )
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
        await ctx.reply(embed=embed, mention_author=False)
    except:
        embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=discord.Colour(0xFF1B1B)
            )
        await ctx.reply(embed=embed, mention_author=False)






@bot.command()
@blacklist_check()
async def pfps(ctx):
  a = requests.get('https://api.ihatehaters.repl.co/api/gif/pfps?format=text').text
  b = a.replace('"','')
  av=discord.Embed(title="Random Pfp", color=0xFF1B1B, timestamp=ctx.message.created_at)
  av.set_image(url=b)
  await ctx.send(embed=av)


            
mainshop = [{"name":"Watch","price":100,"description":"Time <:watchtool:1019456724962385930>"},
            {"name":"Laptop","price":1000,"description":"Work <:Laptop:1019456878650069002>"},
            {"name":"PC","price":10000,"description":"Gaming <:PC:1019456969695838269>"},
            {"name":"Ferrari","price":99999,"description":"Sports Car <:ferrari:1019456103483981865>"}]

@bot.command(aliases=['bal'])
@blacklist_check()
async def balance(ctx):
    author = ctx.message.author
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color(0xFF1B1B))
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance',value=bank_amt)
    em.set_thumbnail(url=author.display_avatar.url)
    await ctx.send(embed= em)


@bot.command()
@blacklist_check()
@commands.cooldown(1, 600, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(embed=discord.Embed(title="begging!", description=f"{ctx.author.mention} Got {earnings} coins!", color=0xFF1B1B))

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@bot.command()
@blacklist_check()
@commands.cooldown(1, 600, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(embed=discord.Embed(title="Working!", description=f"{ctx.author.mention} earned {earnings} coins!!", color=0xFF1B1B))

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)

@work.error
async def work_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@beg.error
async def beg_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))                
      

@bot.command(aliases=['with'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0xFF1B1B))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0xFF1B1B))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0xFF1B1B))
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(embed=discord.Embed(title="withdraw", description=f"{ctx.author.mention} You withdraw {amount} coins", color=0xFF1B1B))

@bot.command(aliases=['dep'])
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0xFF1B1B))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0xFF1B1B))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0xFF1B1B))
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(embed=discord.Embed(title=f"{ctx.author.mention} You deposited {amount} coins", color=0xFF1B1B))

@bot.command(aliases=['sn'])
@blacklist_check()
@commands.cooldown(1, 60, commands.BucketType.user)
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0xFF1B1B))
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0xFF1B1B))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount must be positive!", color=0xFF1B1B))
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(embed=discord.Embed(title=f"{ctx.author.mention} You gave {member} {amount} coins", color=0xFF1B1B))

@send.error
async def send_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command(aliases=['ro'])
@blacklist_check()
@commands.cooldown(1, 30, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send(embed=discord.Embed(title="It is useless to rob him!", color=0xFF1B1B))
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(embed=discord.Embed(title=f'{ctx.author.mention} You robbed {member} and got {earning} coins', color=0xFF1B1B))

@rob.error
async def rob_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
@blacklist_check()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send(embed=discord.Embed(title="Please enter the amount", color=0xFF1B1B))
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(embed=discord.Embed(title="You do not have sufficient balance", color=0xFF1B1B))
        return
    if amount < 0:
        await ctx.send(embed=discord.Embed(title="Amount'Amount must be positive!", color=0xFF1B1B))
        return
    final = []
    for i in range(3):
        a = random.choice(['S', 'W', 'R', 'D'])

        final.append(a)

    await ctx.send((final))
    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.reply(embed=discord.Embed(title=f'You won :) {ctx.author.name}', color=0xFF1B1B))
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.reply(embed=discord.Embed(title=f'You lose :( {ctx.author.name}', color=0xFF1B1B))


@bot.command()
@blacklist_check()
async def shop(ctx):
    em = discord.Embed(title = "Shop", color = discord.Colour(0xFF1B1B))

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)

@bot.command()
@blacklist_check()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(embed=discord.Embed(title="That Object isn't there!", color=0xFF1B1B))
            return
        if res[1]==2:
            await ctx.send(embed=discord.Embed(title=f"You don't have enough money in your wallet to buy {amount} {item}", color=0xFF1B1B))
            return


    await ctx.send(embed=discord.Embed(title=f"You just bought {amount} {item}", color=0xFF1B1B))


            
@bot.command(aliases=["items"])
@blacklist_check()
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "inventory", color = discord.Colour(0xFF1B1B))
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)
        em.set_thumbnail(url=user.display_avatar.url)

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@bot.command()
@blacklist_check()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send(embed=discord.Embed(title="That Object isn't there!", color=0xFF1B1B))
            return
        if res[1]==2:
            await ctx.send(embed=discord.Embed(title=f"You don't have {amount} {item} in your bag", color=0xFF1B1B))
            return
        if res[1]==3:
            await ctx.send(embed=discord.Embed(title=f"You don't have {item} in your inventory", color=0xFF1B1B))
            return

    await ctx.send(embed=discord.Embed(title=f"You just sold {amount} {item}", color=0xFF1B1B))

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 1* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@bot.command(aliases = ["rich"])
@blacklist_check()
async def richest(ctx,x = 5):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xFF1B1B))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = bot.get_user(id_)
        name = member
        em.add_field(name = f"{index}. **{name}**" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)




    
#----------------------------------------------------

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def ticdelete(ctx):
  await ctx.send(f"<:ri8:1038487759750438912> | deleting {ctx.channel.mention} in 1sec.")
  await asyncio.sleep(1)
  await ctx.channel.delete()

@ticdelete.error
async def delete_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def adduser(ctx, member: discord.Member, channel=None):
  channel = channel or ctx.channel
  guild = ctx.guild
  overwrite = channel.overwrites_for(member)
  overwrite.view_channel = True
  await ctx.channel.set_permissions(member, overwrite=overwrite)
  await ctx.reply(f"Successfully added {member.mention} to {channel}", mention_author=False)
  
@adduser.error
async def adduser_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"Uses | `adduser <member id>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)
    
@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def close(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(
        f'<:ri8:1038487759750438912> | Successfully closed {ctx.channel.mention}', mention_author=False
    )
@close.error
async def close_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<:Wrong:1017402708703064144> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@bot.command()
@blacklist_check()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send('joined')
@bot.command()
@blacklist_check()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send('leaved')
@bot.command()
@commands.has_permissions(administrator = True)
@blacklist_check()
async def vcmove(ctx, channel : discord.VoiceChannel = None):
  if channel == None:
    await ctx.reply('Mention a channel to move users to!')
  if ctx.author.voice:    
    channell = ctx.author.voice.channel
    members = channell.members
    for m in members:
      await m.move_to(channel)
    await ctx.reply(f"Moved all users to {channel.mention}")
  if ctx.author.voice is None:
    await ctx.reply('You need to be connected to the channel from where you want to move everyone.')




        

@bot.command(aliases=["log", "audit", "audit-logs", "audit-log", "auditlogs"])
@commands.has_permissions(view_audit_log=True)
@blacklist_check()
@commands.cooldown(1, 12, commands.BucketType.user)
@commands.guild_only()
async def auditlog(ctx, lmt:int):
  if lmt >= 31:
     await ctx.reply("Action rejected, you are not allowed to fetch more than `30` entries.", mention_author=False)
     return
  idk = []
  str = ""
  async for entry in ctx.guild.audit_logs(limit=lmt):
    idk.append(f'''User: `{entry.user}`
Action: `{entry.action}`
Target: `{entry.target}`
Reason: `{entry.reason}`\n\n''')
  for n in idk:
       str += n
  str = str.replace("AuditLogAction.", "")
  embed = discord.Embed(title=f"AUDIT LOGS", description=f">>> {str}", color=0xFF1B1B)
  embed.set_footer(text=f"Audit Log Actions")
  await ctx.reply(embed=embed, mention_author=False)

@auditlog.error
async def auditlog_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
@blacklist_check()
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(0xFF1B1B))
  perms = ""
  if role.permissions.administrator:
            perms += "Administrator, "
  if role.permissions.create_instant_invite:
            perms += "Create Instant Invite, "
  if role.permissions.kick_members:
            perms += "Kick Members, "
  if role.permissions.ban_members:
            perms += "Ban Members, "
  if role.permissions.manage_channels:
            perms += "Manage Channels, "
  if role.permissions.manage_guild:
            perms += "Manage Guild, "
  if role.permissions.add_reactions:
            perms += "Add Reactions, "
  if role.permissions.view_audit_log:
            perms += "View Audit Log, "
  if role.permissions.read_messages:
            perms += "Read Messages, "
  if role.permissions.send_messages:
            perms += "Send Messages, "
  if role.permissions.send_tts_messages:
            perms += "Send TTS Messages, "
  if role.permissions.manage_messages:
            perms += "Manage Messages, "
  if role.permissions.embed_links:
            perms += "Embed Links, "
  if role.permissions.attach_files:
            perms += "Attach Files, "
  if role.permissions.read_message_history:
            perms += "Read Message History, "
  if role.permissions.mention_everyone:
            perms += "Mention Everyone, "
  if role.permissions.external_emojis:
            perms += "Use External Emojis, "
  if role.permissions.connect:
            perms += "Connect to Voice, "
  if role.permissions.speak:
            perms += "Speak, "
  if role.permissions.mute_members:
            perms += "Mute Members, "
  if role.permissions.deafen_members:
            perms += "Deafen Members, "
  if role.permissions.move_members:
            perms += "Move Members, "
  if role.permissions.use_voice_activation:
            perms += "Use Voice Activation, "
  if role.permissions.change_nickname:
            perms += "Change Nickname, "
  if role.permissions.manage_nicknames:
            perms += "Manage Nicknames, "
  if role.permissions.manage_roles:
            perms += "Manage Roles, "
  if role.permissions.manage_webhooks:
            perms += "Manage Webhooks, "
  if role.permissions.manage_emojis:
            perms += "Manage Emojis, "

  if perms is None:
            perms = "None"
  else:
            perms = perms.strip(", ")
          
  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}\nManaged by Integration: {(role.managed)}\n\nmembers in this role: {(len(role.members))}\n\nPermissions: {perms}")
  await ctx.reply(embed=riembed, mention_author=False)
  





  
@bot.command()
@commands.has_guild_permissions(manage_roles=True)
@blacklist_check()
async def unhideall(ctx):
    author = ctx.message.author
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    else:
        for x in ctx.guild.channels:
            await x.set_permissions(ctx.guild.default_role,view_channel=True)
        return
        await ctx.reply(embed=discord.Embed(title="Successfully unhide all channels", description=f"responsible {ctx.author}", color=0x2f3136))




@commands.has_guild_permissions(manage_roles=True)    
@bot.command()
@blacklist_check()
async def hideall(ctx):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x00ffff))
    else:
        for x in ctx.guild.channels:
            await x.set_permissions(ctx.guild.default_role,view_channel=False)
        return
        await ctx.reply(embed=discord.Embed(title="successfully hide all channels", description=f"responsible {ctx.author}", color=0x2f3136))
      
     
@commands.cooldown(3, 300, commands.BucketType.user)


@commands.has_permissions(administrator=True)


@bot.command(

    name="unlockall",

    description=

    "Unlocks the server. | Warning: this unlocks every channel for the everyone role.",

    usage="unlockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)
@blacklist_check()

async def unlockall(ctx, server: discord.Guild = None, *, reason=None):
    

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=True),

                reason=f"action done by {ctx.author}")

        await ctx.send(f"**{server}** has been unlocked.`")

    except:

        await ctx.send(f"**Failed to unlock, {server}**")

    else:

        pass
@bot.command(name="lockall",

                description="Locks down the server.",

                usage="lockall")

@commands.has_permissions(administrator=True)

@commands.cooldown(1, 5, commands.BucketType.channel)
@blacklist_check()

async def lockall(ctx, server: discord.Guild = None, *, reason=None):

    await ctx.message.delete()

    if server is None: server = ctx.guild

    try:

        for channel in server.channels:

            await channel.set_permissions(

                ctx.guild.default_role,

                overwrite=discord.PermissionOverwrite(send_messages=False),

                reason=f"action done by {ctx.author}")

        await ctx.send(f"**{server}** has been locked. by`{ctx.author}")

    except:

        await ctx.send(f"```**Failed to lockdown, {server}.**```")

    else:

        pass
      







    





@bot.command()
@blacklist_check()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel : discord.TextChannel=None):
  
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | <#{channel.id}> is now hidden from the default role.", color=0xFF1B1B))
@bot.command()
@blacklist_check()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel : discord.TextChannel=None):
  
  if channel == None:
    channel = ctx.channel
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason=f"Action issued by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.reply(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | <#{channel.id}> is now visible to the default role.', color=0xFF1B1B))

@bot.command()
@blacklist_check()
async def hi(ctx):
    await ctx.send("hii")


      





@bot.command()
@blacklist_check()
async def antialt(ctx, turn):
    if turn == "off":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Off...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = False
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully set the Anti Alt Acc feature Off.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    elif turn == "on":
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner.id:
                loading = await ctx.send("Setting up the Anti Alt Acc...")
                data = getConfig(ctx.guild.id)
                data["antinew"] = True
                updateConfig(ctx.guild.id, data)
                await loading.delete()
                embed = discord.Embed(
                    title="Setup successfully",
                    description=
                    f"I have successfully setup the Anti New Acc feature.\n\n",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send("Only the owner can use this command!")
        except:
            print("na")
    else:
        await ctx.send("pls send in on or off")
      

@bot.command(aliases=["bug","bugreport","fixbug"])
@commands.cooldown(1, 43200, commands.BucketType.user)
@blacklist_check()
async def report(ctx, *, desc=None):
      if desc == None:
        await ctx.send("PLEASE SUPPLY THE BUG INFORMATION !")
      else:
        await ctx.send("THANKS FOR REPORTING THE BUG. IT WILL BE FIXED SOON !")
        link = await ctx.channel.create_invite(unique=True)
        channel = bot.get_channel(1007214201741250590)
        embed=discord.Embed(title="BUG REPORT",description =f"`REPORTED BY - `\n{ctx.author.name}\n\n`I'D-`\n{ctx.message.author.id}\n\n`BUG -`\n{desc}\n\n`BUG FOUND IN - `\n{ctx.message.guild.name}\n\n`SERVER INVITE -`\n{link}",color=0xFF1B1B)
        await channel.send(embed=embed)

@report.error
async def report_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command(aliases=["sg","sugg"])
@commands.cooldown(1, 43200, commands.BucketType.user)
@blacklist_check()
async def Suggestion(ctx, *, desc=None):
      if desc == None:
        await ctx.send("PLEASE SUPPLY THE SUGGESTION!")
      else:
        await ctx.send("THANKS FOR  SUGGESTION!")
        link = await ctx.channel.create_invite(unique=True)
        channel = bot.get_channel(1007214215632801832)
        embed=discord.Embed(title="SUGGESTIONS ",description =f"`SUGGESTION BY - `\n{ctx.author.name}\n\n`I'D-`\n{ctx.message.author.id}\n\n`SUGGESTION-`\n{desc}\n\n`SUGGESTION FROM- `\n{ctx.message.guild.name}\n\n`SERVER INVITE -`\n{link}",color=0xFF1B1B)
        await channel.send(embed=embed)

@Suggestion.error
async def Suggestion_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send('Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)))

@bot.command()
async def vote(ctx):
    author = ctx.message.author
    b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/zenox-5355/upvote')
    view = View()
    view.add_item(b)
    embed = discord.Embed(description=f"click on button below!",color=0xFF1B1B)
    embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
    embed.set_thumbnail(url=author.display_avatar.url)
    embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=author.display_avatar.url) 
    await ctx.send(embed=embed, view=view)

@bot.command(aliases=["inv"])
async def invite(ctx):
    author = ctx.message.author
    b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=863262252211765248&permissions=8&scope=bot')
    view = View()
    view.add_item(b)
        
    embed = discord.Embed(description="click on button below!", color=0xFF1B1B) 
    embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
    embed.set_thumbnail(url=author.display_avatar.url)
    embed.set_footer(text=f"thanks for using Ethrex") 
    await ctx.send(embed=embed, view=view)

@bot.command()
@blacklist_check()
async def ping(ctx):
      author = ctx.message.author
      embed = discord.Embed(description=f"<a:th_heartbeat:1017469364712263691> Pong! {round(bot.latency * 1000)}ms", color=0xFF1B1B)
      embed.set_author(name=f"{author.name}", icon_url=author.display_avatar.url)
      embed.set_thumbnail(url=author.display_avatar.url)
      embed.set_footer(text=f"requested by {author.name}", icon_url=author.display_avatar.url)
      await ctx.channel.send(embed=embed)
OWNER_IDS =  884798892934332416

def is_bot_owner(ctx):
  return ctx.message.author.id == 884798892934332416


@bot.command()
@commands.check(is_bot_owner)
async def lhguugt(ctx):
    activeservers = bot.guilds
    sum = 0
    for guild in activeservers:
      await  ctx.send(f"name: {guild.name} | member count: {guild.member_count}, id = {guild.id}")


@bot.command()
@commands.check(is_bot_owner)
async def getinv(ctx, guild_id: int):
  guild = bot.get_guild(guild_id)
  channel = guild.channels[0]
  invitelink = await channel.create_invite(max_age=300)
  await ctx.send(embed=discord.Embed(title="INVITE LINK",description=f"INVITE LINK OF REQUESTED SERVER\n\n{invitelink}",color=0xFF1B1B,timestamp=ctx.message.created_at)) 
  

@bot.command(aliases=["em"])
@blacklist_check()
@commands.has_permissions(embed_links=True)
async def embed(ctx,*,mesg=f"Format : embed [words]"):

    await ctx.message.delete()
    embed=discord.Embed(description=mesg,color=0xFF1B1B,timestamp=ctx.message.created_at)
    embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.display_avatar.url) 
    embed.set_footer(text=f"")
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_bot_owner)
async def adminservers(ctx):
	await ctx.message.delete()
	admins = []
	for guild in bot.guilds:
		if guild.me.guild_permissions.administrator:
			admins.append(discord.utils.escape_markdown(guild.name))
	adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
	await ctx.send(adminPermServers)

@bot.command()
@blacklist_check()
async def botlst(ctx):
	await ctx.message.delete()
	bots = []
	for member in ctx.guild.members:
		if member.bot:
			bots.append(
			    str(member.name).replace("`", "\`").replace("*", "\*").replace(
			        "_", "\_") + "#" + member.discriminator)
	bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
	await ctx.send(bottiez)  

@bot.command()
@commands.check(is_bot_owner)
async def leaveg(ctx, *, guild: discord.Guild=None):
  #if ctx.author.id in is_bot_owner:
    if guild is None:
        print("Please enter the guild ID!") # No guild found
        return
    await guild.leave() # Guild found
    await ctx.send(f"I left: {guild.name}!")
  

@bot.command(aliases=["cc"])
@blacklist_check()
@commands.has_permissions(manage_channels=True)
async def channelclean(ctx: Context, channeltodelete: str):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x00ffff))
    else:
        if ctx.author.id == ctx.guild.owner_id:
            for channel in ctx.message.guild.channels:
                if channel.name == channeltodelete:
                        await channel.delete()
                        return
                        await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | Successfully Deleted All Channels With Name Of {channeltodelete}", color=0x2f3136))


@bot.command(aliases=["rc"])
@blacklist_check()
@commands.has_permissions(manage_roles=True)
async def roleclean( ctx: Context, roletodelete: str):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0x00ffff))
        return
    #else:
        for role in ctx.message.guild.roles:
                if role.name == roletodelete:
                        await role.delete()
                        await ctx.reply(embed=discord.Embed(title=f"<:Icons_correct:1017402689027592222> | Successfully Deleted All Roles With Name Of {roletodelete}", color=0x00ffff))

def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner




@bot.command(aliases=["channelcreate"])
@commands.has_permissions(manage_channels=True)
@blacklist_check()
async def addchannel(ctx, *names):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    else:
        for name in names:
            await ctx.guild.create_text_channel(name)
            await ctx.send(embed=discord.Embed(title=f'<:Icons_correct:1017402689027592222> | {name} has been created', color=0xFF1B1B))
    

@bot.command(aliases=['deletechannel'])
@commands.has_permissions(manage_channels=True)
@blacklist_check()
async def delchannel(ctx, *channels: discord.TextChannel):
    me = ctx.guild.me
    if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
        await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
    else:
        for ch in channels:
            await ch.delete()
            await ctx.send(embed=discord.Embed(title=f' <:Icons_correct:1017402689027592222> | {ch.name} has been deleted', color=0xFF1B1B))
       



@bot.command(aliases=["listen"])
@commands.check(is_bot_owner)
async def listening(ctx, *, message):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.send("Listening created!")

@bot.command(aliases=["watch"])
@commands.check(is_bot_owner)
async def watching(ctx, *, message):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message,
        ))
    await ctx.send("watching created!")

@bot.command(aliases=["ply"])
@commands.check(is_bot_owner)
async def playing(ctx, *, message):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=message,
        ))
    await ctx.send("playing created!")

@bot.command()
@commands.check(is_bot_owner)
async def comp(ctx, *, message):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.competing,
            name=message,
        ))
    await ctx.send("Competing created!")

@bot.command()
@commands.check(is_bot_owner)
async def stream(ctx, *, message):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            name=message,
        ))
    await ctx.send("Streaming created!")

@bot.command()
@commands.check(is_bot_owner)
async def dnd(ctx):
    await ctx.send("Ethrex | Changing Status.....")
    await bot.change_presence(
        status=discord.Status.dnd)
    await ctx.send("Done!")

@bot.command()
@commands.has_permissions(administrator=True)
@blacklist_check()
async def cnuke(ctx):

    channel_position = ctx.channel.position
    new_chan = await ctx.channel.clone()
    await ctx.channel.delete()
    await new_chan.edit(position = channel_position) 
    
    #embed=discord.Embed(title="Channel Nuked", description=f"<#{new_chan.id}> - {new_chan.name} has been nuked by {ctx.author}", color=0x13dd4e,timestamp=ctx.message.created_at)
    #embed.set_image(url="https://tenor.com/view/fire-boom-explosion-smoke-gif-17085230")
  #  embed.set_footer(text="Created by Prince")
    await new_chan.send(f"{new_chan.mention} ``nuked by`` {ctx.author.mention}")

@bot.command(aliases=["userbanner"])
@blacklist_check()
async def banner(ctx,  member: discord.Member = None):
    if member == None:
       member = ctx.author
    bannerUser = await bot.fetch_user(member.id)
    if not bannerUser.banner:
                pass
    
    embed=discord.Embed(title=f"{member.name}'s banner", color=0xFF1B1B)
    embed.set_footer(text=f"requested by {ctx.author.name}", icon_url=member.display_avatar.url)
    embed.set_image(url=bannerUser.banner)
    await ctx.send(embed=embed)

@banner.error
async def banner_error(ctx, error):
        if isinstance(error, commands.CommandInvokeError):
                await ctx.send(embed=discord.Embed(title="this user does not have any banner", color=0xFF1B1B))


@bot.command()
@blacklist_check()
async def serverbanner(ctx: commands.Context):
      if not ctx.guild.banner:
        await ctx.send('This server does not have any banner!')
      embed = discord.Embed(title=f'{ctx.guild.name}\'s Banner', color = 0xFF1B1B)
      embed.set_image(url=ctx.guild.banner)
      await ctx.send(embed=embed)


             



@bot.command()
@blacklist_check()
async def source(ctx):
      embed = discord.Embed(description=f"[soward src](https://github.com/PRINCEOP24/Ethrex-bot-src.git)", color=0xFF1B1B)
     # embed.set_author(name=f"{user.avatar}")                          
      embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/kHT4vIV2yvQVr_TVRWuSfbSPVzLuI0hjxVULZroCx-E/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/863262252211765248/fa3d59466f44e012f70d541d9d409520.png")
      embed.set_footer(text="enjoy")
      await ctx.channel.send(embed=embed)
 

@bot.command(
        name='servers',
        description='Owner Only | List the servers that the bot is in',
        usage='serverslist',
        aliases=["sl"]
    )
@commands.is_owner()
async def serverslist(ctx, page: int = 1):
        output = ''
        guilds = bot.guilds
        pages = (len(guilds)/15)
        if 1 <= page <= pages:
            counter = 1+(page-1)*15
            for guild in guilds[(page-1)*15:page*15]:
                gn = guild.name
                gi = str(guild.id)
                gm = str(len(guild.members))
                go = str(guild.owner)
                output += f'**{counter}.** `{gn}` **|** `{gi}` **|** `{gm}` **|** `{go}`\n'
                counter += 1
            embed = discord.Embed(
                colour=0,
                description=output,
                title='__**Server List**__',
                timestamp=ctx.message.created_at
            )
            embed.set_footer(
                text=f'Page {page} of {pages}'
            )
            msg = await ctx.send(
                embed=embed
            )
            await msg.add_reaction("⬅️")
            await msg.add_reaction("➡️")
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["➡️", "⬅️"]
            while True:
              try:
                reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "⬅️":
                  page += 1
                  await msg.remove_reaction(reaction, ctx.author)
                elif str(reaction.emoji) == "➡️":
                  page -= 1
                  await msg.remove_reaction(reaction, ctx.author)
              except asyncio.TimeoutError:
                await msg.remove_reaction(reaction, ctx.author)
                await msg.remove_reaction(reaction, ctx.author)
                await msg.remove_reaction(reaction, bot.user)
                await msg.remove_reaction(reaction, bot.user)
        else:
            await ctx.send(
                embed=discord.Embed(description='Invalid Page Number.'),delete_after=10)

             
   
    














@bot.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '$'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@bot.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)


@bot.command(aliases=["prefix"])
@commands.has_permissions(administrator=True)
@blacklist_check()
async def setprefix(ctx, prefixx):
  with open("prefixes.json", "r") as f:
    idk = json.load(f)
  if len(prefixx) > 5:
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f'<:Wrong:1017402708703064144> | Prefix Cannot Exceed More Than 5 Letters'))
  elif len(prefixx) <= 5:
    idk[str(ctx.guild.id)] =  prefixx
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0xFF1B1B), description=f'<:Icons_correct:1017402689027592222> | Updated Server Prefix To `{prefixx}`'))
  with open("prefixes.json", "w") as f:
    json.dump(idk, f, indent=4)

@bot.command()
@blacklist_check()
async def featurjhes(ctx):
  em = discord.Embed(description=f"**Antinuke Events**\nMove my role above for more protection.\n\nPunishments:\n\nAnti Ban: <:enabled:1017426787438960651>\nAnti Bot: <:enabled:1017426787438960651>\nAnti Channel create: <:enabled:1017426787438960651> \nAnti Channel delete: <:enabled:1017426787438960651>\nAnti Channel update: <:enabled:1017426787438960651>\nAnti Guild update: <:enabled:1017426787438960651>\nAnti Kick: <:enabled:1017426787438960651>\nAnti Member update: <:enabled:1017426787438960651>\nAnti Role create: <:enabled:1017426787438960651>\nAnti Role delete: <:enabled:1017426787438960651>\nAnti Role update: <:enabled:1017426787438960651>\nAnti Webhook: <:enabled:1017426787438960651>")
  em.set_thumbnail(url=bot.user.display_avatar.url)
  await ctx.send(embed=em)













#TOKEN = "ODYzMjYyMjUyMjExNzY1MjQ4.Gdoh8U.gt3qUKIObnx5a9OoKxAEquacA_I0YmhEd8m3p8" #your bot's token here

#basicConfig(level=INFO)

#client = Bot()

if __name__ == '__main__':
    bot.run(TOKEN, reconnect=True)


#keep_alive()

#bot.run('ODYzMjYyMjUyMjExNzY1MjQ4.Gdoh8U.gt3qUKIObnx5a9OoKxAEquacA_I0YmhEd8m3p8', reconnect=True)