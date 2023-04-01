import discord
import os
import asyncio
from discord.ext import commands
import humanfriendly
import datetime
from discord.ext import commands
import aiohttp
#from cogs.utils.lister import lister
from io import BytesIO
from utilities.Tools import*

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []

    @commands.command(aliases=['sb'])
    @blacklist_check()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        """Soft bans a member from the server.
        A softban is basically banning the member from the server but
        then unbanning the member as well. This allows you to essentially
        kick the member while removing their messages.
        In order for this to work, the bot must have Ban Members permissions.
        To use this command, you must have Ban Members permission.
        """
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
        else:
            if reason is None:
                reason = f" No reason given.\nBanned by "
                await member.ban(reason=reason)
                await member.send(f"you have been bannef from {ctx.guild.name} for {reason} by {ctx.author} ")
                await member.unban(reason=reason)
                await ctx.send(embed=discord.Embed(title=f"<:eg_ban:1018057629114826792> | Sucessfully soft-banned {member}.", color=0xFF1B1B))

    @commands.command(aliases=['tb'])
    @commands.guild_only()
    @blacklist_check()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tempban(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
            await ctx.reply(embed=embed)
        else:
            guild = ctx.guild
            embed = discord.Embed(title="Temporarily banned", description=f" {member.mention} has been temporarily banned!", color=0xFF1B1B, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Reason: ", value=reason, inline=False)
            embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
            await ctx.reply(embed=embed)
            await member.send(f'you have been temp banned from {guild} for {reason} by {ctx.author}')
            await guild.ban(user=member)
        if d == "s":
            await asyncio.sleep(int(time))
            await guild.unban(user=member)
        if d == "m":
            await asyncio.sleep(int(time*60))
            await guild.unban(user=member)
        if d == "h":
            await asyncio.sleep(int(time*60*60))
            await guild.unban(user=member)
        if d == "d":
            await asyncio.sleep(time*60*60*24)
            await guild.unban(int(user=member))
            
    @commands.command()
    @blacklist_check()
   # @commands.has_permissions(m_messages=True)
    #@commands.bot_has_permissions(send_messages=True)
    async def vclist(self,ctx):
        ''' Get the list of members in vc you are connected to'''
        if not ctx.message.author.voice:
            await ctx.send(f" | You are not connected to any voice channels")
        else:
            member_list = ctx.message.author.voice.channel.members
            color = 0xFF1B1B
            await lister(ctx,your_list=member_list,color=color,title=f"List of members in {ctx.message.author.voice.channel.name}")
    @commands.group(invoke_without_command=True)
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx,amount:int=10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B))
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)-1} message", color=0xFF1B1B), delete_after=5)

    @purge.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embeddiscord.Emfbed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)}/{amount} message(s) which started with the given keyword", color=0xFF1B1B), delete_after=5)

    @purge.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)}/{amount} message(s) which ended with the given keyword", color=0xFF1B1B), delete_after=5)

    @purge.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)}/{amount} message(s) which contained the given keyword", color=0xFF1B1B), delete_after=5)

    @purge.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)}/{amount} message(s) which were sent by the mentioned user", color=0xFF1B1B), delete_after=5)

    @purge.command()
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send(embed=discord.Embed(title="Purge limit exceeded. Please provide an integer which is less than or equal to 1000.", color=0xFF1B1B), delete_after=5)
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Deleted {len(deleted)}/{amount} message(s) which contained invites", color=0xFF1B1B), delete_after=5)

# TODO: add proper cooldowns to all the commands listed here
# TODO ability to 
#@commands.has_permissions(send_messages=True)
    @commands.command(aliases=('listbots','lbots','lbot','botlist','botslist'))
    @blacklist_check()
  #@commands.bot_has_permissions(send_messages=True)
    async def bots12s2(self,ctx):
        ''' Lists the bots in your server '''
        bots_list = []
        for m in ctx.guild.members:
            if m.bot:
                bots_list.append(m)
      #  color = await self.fetch_color(ctx)
        await lister(ctx,your_list=bots_list,title=f"List of bots in {ctx.guild.name}")
      
    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def muhaha(self, ctx: commands.Context, member: discord.Member, *, reason="No Reason Provided."):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        if ctx.author.top_role.position > member.top_role.position or ctx.author == guild.owner:
            await ctx.send(f" <:tick_right:1003345911067443241> | Successfully muted {member.display_name}")
            await member.add_roles(mutedRole, reason=reason)
            await member.send(f":exclamation: | You have been muted from: {guild.name} reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"<:wrong:1003345816326516756> | You cannot mute someone with a higher role than you!")

    @commands.command(aliases=['mutehoja'], usage=" <member> <time>")
    @commands.guild_only()
    @blacklist_check()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member, duration, *, reason=None):
        """
        Mutes or timeouts a member for specific time.
        Maximum duration of timeout: 28 days (API limitation)
        Use 5m for 5 mins, 1h for 1 hour etc...
        In order for this to work, the bot must have Moderate Members permissions.
        To use this command, you must have Moderate Members permission.
        """

        if reason is None:
            reason = f"Action done by {ctx.author}"

        humanly_duration = humanfriendly.parse_timespan(duration)

        await member.timeout(
            discord.utils.utcnow() + datetime.timedelta(seconds=humanly_duration),
            reason=reason
        )
        await member.send(f":exclamation: | You have been muted from: {ctx.guild.name} by {ctx.author.name}")
        await ctx.send(embed=discord.Embed(title=f" {member} has been timed out for {duration}.\nReason: {reason}", color=0xFF1B1B))

    @commands.command(aliases=['unm'])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def unmuteeee(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await ctx.send(f"<:tick_right:1003345911067443241>| {member.display_name} has been unmuted")
        await member.remove_roles(mutedRole)
        await member.send(f":exclamation: | You are have been unmuted from: {ctx.guild.name} by {ctx.author.name}")
        
        


    @commands.command(name='kick', help="Somebody is breaking rules again and again | ban him from the server as punishment", usage=" <member> <reason>")
    @blacklist_check()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
        else:
            if reason is None:
                reason = f"action done by {ctx.author}"
                await member.kick(reason=reason)
                await ctx.send(f"<:tick_right:1003345911067443241> | {member.display_name} has been kicked from this guild, for: {reason}")
                await member.send(f":exclamation: | You have been kicked from {ctx.guild.name} for: {reason} by {ctx.author.name}!")

        
 #   @commands.command(usage="<emoji>")
  #  @blacklist_check()
 #   async def enlarge(self, ctx, emoji: discord.Emoji):
  #      ''' Enlarge any emoji '''
       # url = emoji(self,format='png')
   #     url = emoji.url
   #     await ctx.send(url)
      
    @commands.command(usage=" <role/id>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def giveallhumans(self,ctx,role:discord.Role,reason=None):
        ''' Gives all the humans any role '''
        reason = f"responsible {ctx.author}"


        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Adding {role.name} to all humans!", color=0xFF1B1B))

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.add_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully given {role.name} to all members!", color=0xFF1B1B))
            
            


 

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def giveallbots(self,ctx,role:discord.Role, reason=None):
        ''' Give all bots any role '''
        reason = f"responsible {ctx.author}"

        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Adding {role.name} to all bots!", color=0xFF1B1B))

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.add_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully given {role.name} to all bots!", color=0xFF1B1B))

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def removeallhumans(self,ctx,role:discord.Role, reason=None):
        ''' Removes a role from all human members '''
        reason = f"responsible {ctx.author}"
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Removing {role.name} from all humans!", color=0xFF1B1B))

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.remove_roles(role, reason=reason)
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully removed {role.name} from all members!", color=0xFF1B1B))

    @commands.command(usage="<role/id>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def removeallbots(self,ctx,role:discord.Role, reason=None):
        ''' Removes a role from all the bots '''
        reason = f"responsible {ctx.author}"
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | Removing  {role.name} from all bots!", color=0xFF1B1B))

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.remove_roles(role, reason=reason)
        await ctx.send(embed= discord.Embed(title=f"<:tick_right:1003345911067443241> | Successfully removed {role.name} from all bots!", color=0xFF1B1B))

  
    @commands.command(aliases=['w'], usage="<member> <reason>")
    @blacklist_check()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, * , reason="No Reason Provided!"):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {member.display_name} has been warned for: {reason}", color=0xFF1B1B))
        await member.send(embed=discord.Embed(title=f":exclamation: | You have been warned in {ctx.guild.name} for: {reason}", color=0xFF1B1B))



                   


    @commands.command(usage="<member>")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcdeafen(self, ctx, user: discord.Member, * , reason=None):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {user.display_name} has been deafened, for: {reason}", color=0xFF1B1B))
        await user.edit(deafen = True)

    @commands.command(aliases=["vm"], usage="<member>")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcmute(self, ctx, member: discord.Member, * , reason=None):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {member.display_name} has been muted, for: {reason}", color=0xFF1B1B))
        await member.edit(mute = True)

    @commands.command(usage="<member>")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcunmute(self, ctx, member: discord.Member):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {member.display_name} has been unmuted.", color=0xFF1B1B))
        await member.edit(mute = False)

    @commands.command(usage="<member>")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcundeafen(self, ctx, member: discord.Member):
        await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {member.display_name} has been undeafened.", color=0xFF1B1B))
        await member.edit(deafen = False)

    @commands.command(usage="<emoji>")
    @blacklist_check()
    @commands.has_permissions(manage_emojis=True)
    async def delemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(embed=discord.Embed(title="<:tick_right:1003345911067443241> | emoji has been deleted.", color=0xFF1B1B))

    @commands.command()
    async def steal123(self, ctx, url:str, *, name = None):
        if name == None:
            name == "stolen-emoji"
        if url == discord.Emoji:
            url = discord.Emoji.url
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    imgOrGif = BytesIO(await r.read())
                    bValue = imgOrGif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=bValue, name=name)
                        await ctx.send(f"<:tick_right:1003345911067443241> | Sucessfully added Emoji `:{name}:`")
                        await ses.close()
                    else:
                        await ctx.send(f"<:wrong:1003345816326516756> | Something went wrong | {r.status}")
                except discord.HTTPException:
                    await ctx.send(f"<:wrong:1003345816326516756> | The file is too big.")


    @commands.command(name='ban', help="Somebody is breaking rules again and again | ban him from the server as punishment", usage="<member> <reason>")
    @blacklist_check()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
        else:
            if reason is None:
                reason = f"action done by {ctx.author}"
            await member.ban(reason=reason)
            await ctx.send(embed=discord.Embed(title=f"<:eg_ban:1018057629114826792> | {member.display_name} has been successfully banned", color=0xFF1B1B))
            await member.send(embed=discord.Embed(title=f"<:eg_ban:1018057629114826792> | You have been banned from {ctx.message.guild.name} for reason: {reason} by {ctx.author.name}", color=0xFF1B1B))
                
                

    @commands.command()
    @blacklist_check()
  	#@commands.has_permissions(kick_members=True)
    async def block(self, ctx, user):
        """
        Blocks a user from chatting in current channel.
           
        Similar to mute but instead of restricting access
        to all channels it restricts in current channel.
        """
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
                                
        await ctx.set_permissions(user, send_messages=False) # sets permissions for current channel
    
    @commands.command()
    @blacklist_check()
  	#@commands.has_permissions(kick_members=True)
    async def unblock(self, ctx, user):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
        
        await ctx.set_permissions(user, send_messages=True) # gives back send messages permissions


    
    
    @commands.command(usage="<id>")
    @blacklist_check()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        me = ctx.guild.me
        if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
            await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
        else:
            user = await self.bot.fetch_user(id)
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(title=f"<:tick_right:1003345911067443241> | {user.name} has been successfully unbanned", color=0xFF1B1B))

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: discord.TextChannel, reason=None):
            me = ctx.guild.me
            if me.top_role >= ctx.message.author.top_role and ctx.message.author.id != ctx.guild.owner_id:
                    await ctx.reply(embed=discord.Embed(title="You must have role above me to use this cmd.", color=0xFF1B1B))
            else:
                    reason = f"responsible {ctx.author}"
                    await channel.clone(reason=reason)
                    await ctx.send(f"<:tick_right:1003345911067443241> | {channel.name} has been successfully cloned")



               

def setup(bot):
    bot.add_cog(moderation(bot))