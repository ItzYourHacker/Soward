import discord
import datetime
import time
import asyncio
import aiohttp
import json
import re
#from core.Soward import Soward
from simpcalc import simpcalc
from discord.ext import commands, tasks
from discord.utils import escape_markdown

from discord.ui import Button, View



class InteractiveView(discord.ui.View):
    def __init__(self, ctx: commands.Context):
        super().__init__(timeout=None)
        self.expr = ""
        self.calc = simpcalc.Calculate()
        self.ctx = ctx

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="1", row=0)
    async def one(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "1"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="2", row=0)
    async def two(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "2"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="3", row=0)
    async def three(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "3"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="➕", row=0)
    async def plus(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "+"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="4", row=1)
    async def last(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "4"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="5", row=1)
    async def five(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "5"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="6", row=1)
    async def six(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "6"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="➗", row=1)
    async def divide(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "/"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="7", row=2)
    async def seven(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "7"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="8", row=2)
    async def eight(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "8"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="9", row=2)
    async def nine(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "9"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="✖️", row=2)
    async def multiply(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "*"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label=".", row=3)
    async def dot(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "."
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.blurple, label="0", row=3)
    async def zero(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "0"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="=", row=3)
    async def equal(self, button: discord.ui.Button, interaction: discord.Interaction):
        try:
            self.expr = await self.calc.calculate(self.expr)
        except errors.BadArgument:
            return await interaction.response.send_message("Um, looks like you provided a wrong expression....")
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="-", row=3)
    async def minus(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "-"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label="(", row=4)
    async def left_bracket(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += "("
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.green, label=")", row=4)
    async def right_bracket(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr += ")"
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.red, label="AC", row=4)
    async def clear(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr = ""
        await interaction.response.edit_message(content=f"\n> {self.expr}\n")

    @discord.ui.button(style=discord.ButtonStyle.red, label="BACK", row=4)
    async def back(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.expr = self.expr[:-1]
        await interaction.response.edit_message(content=f"\n{self.expr}\n")

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
    
        if interaction.user.id == self.ctx.author.id:
             return True
        await interaction.response.send_message(f"This is {self.ctx.author.mention} calculator's not yours", ephemeral=True)
        return False


class lodu(commands.Cog, description="Commands that make your Discord experience nicer!"):
    def __init__(self, client):
        self.client = client
     #   self.reminding.start()
        self.regex = re.compile(r"(\w*)\s*(?:```)(\w*)?([\s\S]*)(?:```$)")




    @commands.cooldown(3, 40, commands.BucketType.user)
    @commands.command(help="calculate what you want!", aliases = ['calc', 'math', 'maths'])
    async def calculate(self, ctx: commands.Context):
         view = InteractiveView(ctx)
         await ctx.send("\n" , view=view)



def setup(client):
    client.add_cog(lodu(client))

 