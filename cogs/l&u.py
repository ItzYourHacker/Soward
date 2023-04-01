
from utilities.Tools import*
import typing

import discord
from discord.ext import commands
import datetime
import io
from discord.ext.commands import BucketType, cooldown
import asyncio
import random
import re
import aiofiles


def convert(time: int, unit):
    unit = unit.lower()
    if unit == 's':
        return time
    elif unit == 'm':
        return time * 60
    elif unit == 'h':
        return (time * 60) * 60
    elif unit == 'd':
        return ((time * 60) * 60) * 24


class Moderation3(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

                                     

    
 

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    
    @commands.cooldown(1, 10, commands.BucketType.guild)
    @blacklist_check()
    async def nuke(self, ctx, channels: discord.TextChannel = None):
        channels = channels or ctx.channel

        await ctx.send('Are you sure you want to nuke {}!\nType in `yes`. To proceed'.format(channels.mention))

        def check(m):
            user = ctx.author
            return m.author.id == user.id and m.content.lower() == 'yes'

        position = channels.position

        await self.bot.wait_for('message', check=check)
        await ctx.channel.send('Theres no going back!\n**Are you sure.**')
        await self.bot.wait_for('message', check=check)
        try:
            new = await channels.clone()
            await channels.delete()
            await new.edit(positon=position)
        except discord.errors.Forbidden:
            return await ctx.send('**Nuke Failed. I am missing permissions!**')

     #   await new.send('https://media1.tenor.com/images/6c485efad8b910e5289fc7968ea1d22f/tenor.gif?itemid=5791468')
        await asyncio.sleep(2)
        await new.send(f" ``nuked by`` {ctx.author.mention}")

    @commands.command(aliases=['nick'])
    @commands.has_guild_permissions(manage_nicknames=True)
    @commands.bot_has_guild_permissions(manage_nicknames=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    async def nickname(self, ctx, member: discord.Member, *, new_nickname: str):
        if member == ctx.guild.owner:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(embed=discord.Embed(
                description='You cannot change the owners nickname!',
                color=0xFF1B1B
            ))
        else:
            try:
                old = member.display_name
                await member.edit(nick=new_nickname[:32])
            except discord.errors.Forbidden:
                return await ctx.send(embed=discord.Embed(
                    description='Cannot change **{}** nickname due to role hierarchy.'.format(
                        member),
                    colour=0xFF1B1B
                ))
            await ctx.send(embed=discord.Embed(
                description=' Successfully changed nick**{}** to **{}**.'.format(old,
                                                                                                          new_nickname[
                                                                                                          :32]),
                color=0xFF1B1B
            ))

    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.cooldown(1, 60, BucketType.user)
    @blacklist_check()
    async def slowmode(self, ctx, time='0', channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        try:
            time = int(time)
        except ValueError:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(embed=discord.Embed(
                description=' Slowmode delay must be a number!',
                color=0xFF1B1B
            ))
        if time < 0:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(embed=discord.Embed(
                description=' Slowmode delay must be a positive number!'
            ))
        if time > 21600:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(
                embed=discord.Embed(
                    description='Channel can only have a maximum slowmode of **21600** seconds (6 Hours).',
                    color=0xFF1B1B
                )
            )
        else:
            await channel.edit(slowmode_delay=time)
            await ctx.send(embed=discord.Embed(
                description='The channel {} now has a slowmode delay of **{}** seconds'.format(
                    channel.mention, time),
                color=0xFF1B1B
            ))

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @blacklist_check()
    async def lock(self, ctx, channel: discord.TextChannel = None, role: discord.Role = None):
        channel = channel or ctx.channel

        role = role or ctx.guild.default_role
        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.reply(embed=discord.Embed(
                description='<:ri8:1038487759750438912> {}. Successfully locked the channel'.format(channel.mention),
                color=0xFF1B1B
            ))
        elif channel.overwrites[role].send_messages or channel.overwrites[role].send_messages == None:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = False
            await channel.set_permissions(role, overwrite=overwrites)
            await ctx.reply(embed=discord.Embed(title=f"<:eg_lock:1018057640724660226> | {ctx.channel.mention} has been locked!", color=0xFF1B1B))
        else:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = True
            await channel.set_permissions(role, overwrite=overwrites)
            await ctx.reply(embed=discord.Embed(title=f"<:eg_unlock:1018057690154537051> | {ctx.channel.mention} has been unlocked!", color=0xFF1B1B))

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_nicknames=True)
    async def clearnick(self, ctx, member: discord.Member):
        await member.edit(nick="")
        await ctx.send(embed=discord.Embed(title="<:tick_right:1003345911067443241> | Successfully reset nickname", color=0xFF1B1B))








def setup(bot):
    bot.add_cog(Moderation3(bot))
