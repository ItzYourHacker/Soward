import random
import asyncio
import discord

from discord.ext import commands
from helpers.context import CustomContext
from helpers.ttt import LookingToPlay, TicTacToe
from helpers.helpers import generate_youtube_bar as bar
from helpers import context 


    


class Games(commands.Cog):
    """Commands used to play games when you're bored!"""

    def __init__(self, client):
        self.bot = client
        self.select_emoji = "<:video_game:899622306148675594>"
        self.select_brief = "Commands used to play games when you're bored!"



    @commands.command(
        help="Starts a Tic-Tac-Toe game",
        aliases=['ttt', 'tic'])
    async def tictactoe(self, ctx: CustomContext):
        embed = discord.Embed(description=f"🔎 {ctx.author.name} is looking to play Tic-Tac-Toe!", color=0xFF1B1B)

        player1 = ctx.author
        view = LookingToPlay(timeout=120)
        view.ctx = ctx
        view.message = await ctx.send(embed=embed, view=view)
        await view.wait()
        player2 = view.value

        if player2:
            starter = random.choice([player1, player2])
            ttt = TicTacToe(ctx, player1, player2, starter=starter)
            ttt.message = await view.message.edit(content=f'#️⃣ {starter.mention} goes first', view=ttt, embed=None)
            await ttt.wait()

    
        
            
def setup(client):
    client.add_cog(Games(client))