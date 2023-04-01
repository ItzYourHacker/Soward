from __future__ import annotations
from discord.ext import commands
from core import Context
import discord
from utilities.Tools import *
from discord.ext.commands import Cog
class Antinuke(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client):
    self.client = client

  @commands.group(name="antinuke", help="Enables/Disables antinuke in your server!", invoke_without_command=True)
  
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antinuke(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!", aliases=["on"])
  
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_enable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if ctx.author.id == ctx.guild.owner_id:
      if data == "on":
        embed = discord.Embed(title="Soward", description=f"**Antinuke already enabled on this server** \n To disable antinuke  use `antinuke disable`\n Status: enabled <:enabled:1017426787438960651>", color=discord.Colour(0xFF1B1B), timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        if ctx.guild.icon:
          embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_footer(text="Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateanti(ctx.guild.id, data)
        embed2 = discord.Embed(title="__Soward__", description=f"**{ctx.guild.name} Antinuke Status** \nMove my role above for more protection \n\n**Successfully enabled Antinuke**\n **Anti Kick** <:enabled:1017426787438960651> \n**Anti Ban**<:enabled:1017426787438960651> \n**Anti prune** <:enabled:1017426787438960651> \n**Anti Bot** <:enabled:1017426787438960651> \n **Anti Role** <:enabled:1017426787438960651> \n**Anti Channel** <:enabled:1017426787438960651> \n**Anti Emoji** <:enabled:1017426787438960651> \n**Anti webhook create** <:enabled:1017426787438960651> \n**Anti Community Spam** <:enabled:1017426787438960651> \n**Anti Guild Update** \n**Anti Integration Create:** <:enabled:1017426787438960651>", color=discord.Colour(0xFF1B1B), timestamp=ctx.message.created_at)
        embed2.add_field(name="**__Auto Recovery__**", value="Enabled")

        embed2.add_field(name="**__Whitelisted Users__**", value=len(wled))
        embed2.add_field(name="**__Extra settings__**", value=f"To change the punishment type `{ctx.prefix}punishment set <ban/kick>`")
        embed2.add_field(name=f"**__Current punishment type__**", value=f"{punish}")
        embed2.set_footer(text=f"Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")
        if ctx.guild.icon:
          embed2.set_thumbnail(url=f"{ctx.guild.icon}")
        embed2.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      await ctx.reply("You must be the guild owner to use the command!", mention_author=False)

  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"])
  
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_disable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    if ctx.author.id == ctx.guild.owner_id:
      if data == "off":
        emb = discord.Embed(title="**__Soward__**", description=f" Antinuke already disabled in this server\nCurrent Status: Disabled <:off:1031276015152021604>\n\nTo enable Antinuke use `antinuke enable`", color=0xFF1B1B, timestamp=ctx.message.created_at)
        emb.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        if ctx.guild.icon:
          emb.set_thumbnail(url=ctx.guild.icon)
        emb.set_footer(text="Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")

        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateanti(ctx.guild.id, data)
        swrd = discord.Embed(title="Soward", description=f"Successfully disabled Antinuke for this server \n\nCurrent Status: Disabled <:off:1031276015152021604> \n\n To enable Antinuke use `antinuke enable`", color=0xFF1B1B, timestamp=ctx.message.created_at)
        swrd.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        if ctx.guild.icon:
          swrd.set_thumbnail(url=ctx.guild.icon)
        swrd.set_footer(text="Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")
        await ctx.reply(embed=swrd, mention_author=False)

  @_antinuke.command(name="config", help="Shows currently antinuke config settings of your server")
  
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_config(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if data == "off":
      emb = discord.Embed(title="**__Soward__**", description=f"**{ctx.guild.name} Antinuke Status **\n Antinuke  disabled in this server \n\nCurrent Status:- Disabled  <:off:1031276015152021604>\n\n To enable use \n`antinuke enable`", color=0xFF1B1B, timestamp=ctx.message.created_at)
      if ctx.guild.icon:
        emb.set_thumbnail(url=ctx.guild.icon)
      emb.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
      emb.set_footer(text="Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")
      await ctx.reply(embed=emb, mention_author=False)
    elif data == "on":
      embed2 = discord.Embed(title="**__Soward__**", description=f"**Antinuke settings for** {ctx.guild.name}\n\n**Move my role above for more protection** \n\n**Anti Kick** <:enabled:1017426787438960651> \n**Anti Ban**<:enabled:1017426787438960651> \n**Anti prune** <:enabled:1017426787438960651> \n**Anti Bot** <:enabled:1017426787438960651> \n **Anti Role** <:enabled:1017426787438960651> \n**Anti Channel** <:enabled:1017426787438960651> \n**Anti Emoji** <:enabled:1017426787438960651> \n**Anti webhook create** <:enabled:1017426787438960651> \n**Anti Community Spam** <:enabled:1017426787438960651> \n**Anti Guild Update** \n**Anti Integration Create:** <:enabled:1017426787438960651>", color=discord.Colour(0xFF1B1B), timestamp=ctx.message.created_at)
      embed2.add_field(name="**__Extra__**", value=f"To change the punishment type `{ctx.prefix}punishment set <kick/ban>`")
      embed2.add_field(name="**__Whitelisted users__**", value=len(wled))
      embed2.add_field(name=f"**__Current punishment type__**" , value=f"{punish}")
      embed2.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
      embed2.set_footer(text="Soward", icon_url="https://images-ext-1.discordapp.net/external/XrJavR2bQK47KNCY3DnTog-f4QPNg2NQLI-_UV5zRCM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1004248513435152484/901eaf50a9e389a7e00cab6c06a2bb59.png")
      if ctx.guild.icon:
        embed2.set_thumbnail(url=ctx.guild.icon)
      
      await ctx.reply(embed=embed2, mention_author=False)
  @commands.command(aliases=["recover"],help="Deletes all channels with name of rules and moderator-only")
  
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _recover(self, ctx: Context):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
                pass
    await ctx.reply(embed=discord.Embed(title=f"Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False), color=0xFF1B1B)

  @commands.group(name="punishment", help="Changes Punishment of antinuke and antiraid for this server.", invoke_without_command=True)
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _punishment(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_punishment.command(name="set", help="Changes Punishment of antinuke and antiraid for this server.", aliases=["change"])
  
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_set(self, ctx, punishment: str):
        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner
        if ctx.author == owner:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"

                await ctx.reply(embed=discord.Embed(title=f"Punishment set To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"

                await ctx.reply(embed=discord.Embed(title=f"Punishment Set To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"

                await ctx.reply(embed=discord.Embed(title=f"Punishment Changed To **{kickOrBan}**", color=0xFF1B1B))

                updateConfig(ctx.guild.id, data)
            else:
               await ctx.reply(embed=discord.Embed(title=f"Invalid Punishment Type\nValid Punishment  Kick, Ban", color=0xFF1B1B))

        else:
            await ctx.reply(embed=discord.Embed(title="This Command Can Only be Executed By This Server\'s Owner", color=0xFF1B1B))

  @_punishment.command(name="show", help="Shows custom punishment type for this server")
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_show(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    punish = data["punishment"]
    await ctx.reply(embed=discord.Embed(title="Antinuke punishment in this server is: **{}**".format(punish.title(), color=0xFF1B1B)))
 # @commands.command(name="setvanity", help="Sets vanity code in database and reverts when server vanity is changed")
  
 # @commands.cooldown(1, 10, commands.BucketType.user)
 # @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
 # @commands.guild_only()
  #async def _setvainity(self, ctx: Context, vanity_code: str):
    #    if not ctx.guild.premium_tier == 3:
    #        await ctx.reply("Your Servers Vanity Is Locked")
    #    else:
    #      if ctx.author.id == ctx.guild.owner_id:
   #         if "https://discord.gg/" in vanity_code:
   #           idk = vanity_code.replace("https://discord.gg/", "")
     #       elif "discord.gg/" in vanity_code:
    #          idk = vanity_code.replace("discord.gg/", "")
    #        elif "discord.com/invite/" in vanity_code:
    #          idk = vanity_code.replace("discord.com/invite", "")
     #       elif "https://discord.com/invite/" in vanity_code:
    #          idk = vanity_code.replace("https://discord.com/invite/", "")
    #        else:
   #           idk = vanity_code
    #        update_vanity(ctx.guild.id, idk)
  #          await ctx.reply(f"Successfully Set Vanity To {idk}", mention_author=False)
   #       elif ctx.author.id == 743431588599038003:
   #         if "https://discord.gg/" in vanity_code:
   #           idk = vanity_code.replace("https://discord.gg/", "")
    #        elif "discord.gg/" in vanity_code:
    #          idk = vanity_code.replace("discord.gg/", "")
   #         elif "discord.com/invite/" in vanity_code:
   #           idk = vanity_code.replace("discord.com/invite", "")
      #      elif "https://discord.com/invite/" in vanity_code:
   #           idk = vanity_code.replace("https://discord.com/invite/", "")
    #        else:
   #           idk = vanity_code
    #        update_vanity(ctx.guild.id, idk)
     #       await ctx.reply(f"Successfully Set Vanity To {idk}", mention_author=False)
    #      else:
    #        await ctx.reply("You Must Be Guild Owner To Use This Command", mention_author=False)


  @commands.group(name="whitelist", aliases=["wl"], help="Whitelist your TRUSTED users for anti-nuke", invoke_without_command=True)
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def _whitelist(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_whitelist.command(name="add", help="Add a user to whitelisted users")
  
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if len(wled) == 10:
        await ctx.reply(embed=discord.Embed(title="This server have already maximum number of whitelisted users (10)\nRemove one to add another", color=0xFF1B1B))
      else:
        if str(user.id) in wled:
          await ctx.reply(embed=discord.Embed(title="That user is already  whitelisted!", color=0xFF1B1B))
        else:
          wled.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          await ctx.reply(embed=discord.Embed(title=" **{}** has been added to the whitelist".format(user), color=0xFF1B1B))

    else:
          await ctx.reply(embed=discord.Embed(title="You must be guild owner to whitelist someone  ", color=0xFF1B1B))

  @_whitelist.command(aliases=["uwl, unwhitelist"], name="remove", help="Remove a user from whitelisted users")
  
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if str(user.id) in wled:
        wled.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        await ctx.reply(embed=discord.Embed(title="**{}** has been removed from the whitelist".format(user), color=0xFF1B1B))
      else:
        await ctx.reply(embed=discord.Embed(title="That user was never whitelisted", color=0xFF1B1B))
    else:
      await ctx.reply(embed=discord.Embed(title="You must be the guild owner to remove someone from whitelist", color=0xFF1B1B))

  @_whitelist.command(name="show", help="Check who are in whitelist database")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_show(self, ctx):
      data = getConfig(ctx.guild.id)
      wled = data["whitelisted"]
      if len(wled) == 0:
        await ctx.reply("nothing found in this guild!", mention_author=False)
      else:
        embed = discord.Embed(title="Soward", description="Whitelisted users for this server:\n", color=discord.Colour(0xFF1B1B), timestamp=ctx.message.created_at)
      for idk in wled:
        embed.description += f"<@{idk}> \n"
        embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
        if ctx.guild.icon:
          embed.set_thumbnail(url=ctx.guild.icon)

      await ctx.reply(embed=embed, mention_author=False)


  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"])
  
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def wl_reset(self, ctx: Context):
    if ctx.author.id == ctx.guild.owner_id:
      data = getConfig(ctx.guild.id)
      data["whitelisted"] = []
      updateConfig(ctx.guild.id, data)
      await ctx.reply(embed=discord.Embed(title="Successfully Removed all whitelisted users ", color=0xFF1B1B))
    else:
      await ctx.reply(embed=discord.Embed(title="You must be the guild owner to use this command", color=0x2f3136))


  @commands.command()
  @blacklist_check()
  async def featddures(self, ctx):
          em = discord.Embed(description=f"**Antinuke Events** <:eg_shield:1018057685637275670>\nMove my role above for more protection.\n\nAnti Ban\nAnti Bot \nAnti Channel create  \nAnti Channel delete: \nAnti Channel update: \nAnti Guild update \nAnti Kick \nAnti Member update \nAnti Role create \nAnti Role delete \nAnti Role update: \nAnti Webhook: \nAnti prune \nAnti integration create \nAnti Emoji create \nAnti emoji update \nAnti emoji delete \nAnti community spam \nAnti guild update ", color=0xFF1B1B, timestamp=ctx.message.created_at)
          em.set_thumbnail(url=self.client.user.display_avatar.url)
          em.set_author(name=ctx.author, icon_url=ctx.author.display_avatar.url)
          em.set_footer(text="Made By Prince", icon_url="https://images-ext-2.discordapp.net/external/XpYSeN_4K1TG8OtzI3R3LE3zXbhvqB1rwgQkKRSs-Ww/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/980361546918162482/aa3b4e68dd27540854c0e0e3f374fe32.png")
          await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Antinuke(bot))