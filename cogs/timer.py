import discord
from discord.ext import commands
import asyncio
from termcolor import colored
from utilities.Tools import*
class timer(commands.Cog):

    def __init__(self, bot):
        self.bot= bot

        self.switch = False

        print("System - Timer Cog         "+colored('Running', 'green'))


    @commands.command(aliases=['tstart'],
    brief=" | Start a timer")
    @blacklist_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def timer(self, ctx, timeInput, *, title='Timer'):
        try:
            try:
                time = int(timeInput)
            except:
                convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
                time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]
            if time > 86400:
                await ctx.send("I can\'t do timers over a day long")
                return
            if time <= 0:
                await ctx.send("Timers don\'t go into negatives :/")
                return
            if time >= 3600:
                embed = discord.Embed(
                    title=f'{title}',
                    description=f"**{time//3600}** hours, **{time%3600//60}** minutes, **{time%60}** seconds",
                    color=0xFF1B1B
                )
                embed.set_footer(text='Soward')
                message = await ctx.send(embed=embed)
                await message.add_reaction('👍')
            elif time >= 60:
                embed = discord.Embed(
                    title=f'{title}',
                    description=f"**{time//60}** minutes, **{time%60}** seconds",
                    color=0xFF1B1B
                )
                embed.set_footer(text='Soward')
                message = await ctx.send(embed=embed)
                await message.add_reaction('👍')
            elif time < 60:
                embed = discord.Embed(
                    title=f'{title}',
                    description=f'**{time}** seconds',
                    color=0xFF1B1B
                )
                embed.set_footer(text='Soward')
                message = await ctx.send(embed=embed)
                await message.add_reaction('👍')
            while True:
                try:
                    await asyncio.sleep(6)
                    time -= 6
                    if time >= 3600:
                        embed = discord.Embed(
                            title=f'{title}',
                            description=f"**{time//3600}** hours, **{time%3600//60}** minutes, **{time%60}** seconds",
                            color=0xFF1B1B
                        )
                        embed.set_footer(text='Soward')
                        await message.edit(embed=embed)
                    elif time >= 60:
                        embed = discord.Embed(
                            title=f'{title}',
                            description=f"**{time//60}** minutes, **{time%60}** seconds",
                            color=0xFF1B1B
                        )
                        embed.set_footer(text='Soward')
                        await message.edit(embed=embed)
                    elif time < 60:
                        embed = discord.Embed(
                            title=f'{title}',
                            description=f"**{time}** seconds",
                            color=0xFF1B1B
                        )
                        embed.set_footer(text='Soward')
                        await message.edit(embed=embed)
                    if time <= 0:
                        embed = discord.Embed(
                            title=f'{title}',
                            description='Time\'s up!',
                            color=0xFF1B1B
                        )
                        await message.edit(embed=embed)
                        m = await ctx.channel.fetch_message(message.id)
                        list_thingy = []
                        output_list_thingy = []
                        reactants = await m.reactions[0].users().flatten()
                        reactants.pop(reactants.index(self.client.user))
                        for user in reactants:
                            list_thingy.append(user.id)
                            x = '<@!' + str(user.id) + '>' 
                            output_list_thingy.append(x)
                        if output_list_thingy != []:
                            final = ', '.join(map(str, output_list_thingy))
                            return await ctx.send(f'The timer for **{title}** has ended!\n{final}')
                        else:
                            return await ctx.send(f'The timer for **{title}** has ended!')
                except:
                    break
        except:
            await ctx.send(f"Alright, first you gotta let me know how I\'m gonna time **{timeInput}**....")

    @timer.error
    async def timer_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Take a breather...", description = "You have to wait **{:.2f} seconds**\nThe cooldown for this command is `30s`".format(error.retry_after), color = discord.Color(0xFF1B1B))
        await ctx.send(embed=embed, delete_after=30)



def setup(bot):
    bot.add_cog(timer(bot))