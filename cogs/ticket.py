import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio
from cogs.utils.config import *
from utilities.Tools import*
class close(Button):
    def __init__(self):
        super().__init__(label=f'Close', emoji='<a:bx_aPepeExit:1017725711273955338>', style=discord.ButtonStyle.red, custom_id="close")
        self.callback = self.button_callback
    
    async def button_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Closing this ticketing in 5 seconds.', ephemeral=True)
        await asyncio.sleep(5)
        await interaction.channel.delete()

class closeTicket(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(close())

class create(Button):
    def __init__(self):
        super().__init__(label='Create ticket', emoji='<:Ticket:1017405493477638205>',  style=discord.ButtonStyle.green, custom_id=f'create')
        self.callback = self.button_callback
    
    async def button_callback(self, interaction: discord.Interaction):
        categ = discord.utils.get(interaction.guild.categories, name='Ticket-category')
        
        for ch in categ.channels:
            if ch.topic == str(interaction.user):
                await interaction.response.send_message("You already have a ticket open.", ephemeral=True)
                return
        overwrites = {
                    interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    interaction.user: discord.PermissionOverwrite(read_messages=True),
                }
        channel = await categ.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites, topic=f'{interaction.user}')
        await interaction.response.send_message(f">>> Your ticket has been created at {channel.mention}", ephemeral=True)
        embed = discord.Embed(
                    title=f'Ticket',
                    description=f'Thanks for reaching out!\nThe support Team will be here shortly\nPlease be patient.\n\nClick <a:bx_aPepeExit:1017725711273955338> to close the ticket.',
                    color = 0xFF1B1B
                )
        await channel.send(f'{interaction.user.mention} Welcome ', embed=embed, view=closeTicket())

class createTicket(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(create())

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


  
    @commands.group(name="Tickett", description="Ticket Setup")
    async def tickett(self, ctx: commands.Context):
        ...
    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_guild=True)
    async def sendpanel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        embed = discord.Embed(title=f'Ticket', description=f'>>> To create a ticket click the <:Ticket:1017405493477638205> button.', color=0xFF1B1B)
        embed.set_thumbnail(url=self.bot.user.avatar)
        embed.set_footer(text=' - Ticket Tool')
        guild = ctx.guild       
        await guild.create_category_channel(name="Ticket-category")
        await channel.send(embed=embed, view= createTicket())


def setup(bot):
    bot.add_cog(TicketCog(bot))