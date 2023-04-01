import discord
from discord.ext import commands
import random
import asyncio
from cogs.game import hangman
#from cogs.game import tictactoe
from typing import List
from utilities.Tools import*
def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

from typing import List
from discord.ext import commands
import discord

# Defines a custom button that contains the logic of the game.
# The ['TicTacToe'] bit is for type hinting purposes to tell your IDE or linter
# what the type of `self.view` is. It is not required.
class TicTacToeButton(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X won!'
            elif winner == view.O:
                content = 'O won!'
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @blacklist_check()
    async def findimposter(self, ctx):
        """Impostors can sabotage the reactor, 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win."""


            # determining
        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down!" , color=discord.Colour.default())
            
            # fields
        embed1.add_field(name = 'Red' , value= ':red_circle:' , inline=False)
        embed1.add_field(name = 'Blue' , value= ':blue_circle:' , inline=False)
        embed1.add_field(name = 'Lime' , value= ':green_circle:' , inline=False)
        embed1.add_field(name = 'White' , value= ':white_circle:' , inline=False)
            
            # sending the message
        msg = await ctx.send(embed=embed1)
            
            # emojis
        emojis = {
                'red': '🔴',
                'blue': '🔵',
                'lime': '🟢',
                'white': '⚪'
            }
            
            # who is the imposter?
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
            
            # for testing...
        print(emojis[imposter])
            
            # adding choices
        for emoji in emojis.values():
            await msg.add_reaction("🔴")
            await msg.add_reaction("🔵")
            await msg.add_reaction("🟢")
            await msg.add_reaction("⚪")
            
            # a simple check, whether reacted emoji is in given choises.
        def check(reaction, user):
            ctx.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

            # waiting for the reaction to proceed
        try: 
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            
        except TimeoutError:
                # reactor meltdown - defeat
            description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
            embed = get_embed("Defeat", description, discord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory
            if str(ctx.reacted) == emojis[imposter]:
                description = "**{0}** was the imposter...".format(imposter)
                embed = get_embed("Victory", description, discord.Color.blue())
                await ctx.send(embed=embed)

                # defeat
            else:
                for key, value in emojis.items(): 
                    if value == str(ctx.reacted):
                        description = "**{0}** was not the imposter...".format(key)
                        embed = get_embed("Defeat", description, color=0xFF1B1B)
                        await ctx.send(embed=embed)
                        break

    @commands.command(name='rps', aliases=['rockpaperscissors'])
    @blacklist_check()
    async def rps(self, ctx):
        """Play Rock, Paper, Scissors game"""
        def check_win(p, b):
            if p=='🌑':
                return False if b=='📄' else True
            if p=='📄':
                return False if b=='✂' else True
            # p=='✂'
            return False if b=='🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**:man_in_tuxedo_tone1:\t{reaction.emoji}\n:robot:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win :sparkles:**")
            else:
                await ctx.send("**I win :robot:**")
    
    @commands.command()
    @blacklist_check()
    async def hangman(self, ctx):
        await hangman.play(self.bot, ctx)

    #@commands.command(name='tictactoe', aliases=['t-t-t'])
  #  @blacklist_check()
  #  async def tt_t(self, ctx: commands.Context):
    #    await ctx.send(f'Tic Tac Toe: `X` goes first.', view=TicTacToe())

    @commands.command(name='quiz', aliases=['trivia'])
    @blacklist_check()
    async def quiz(self, ctx):
        """Start an interactive quiz game"""
        try:
            async with ctx.typing():
                question = await self.tclient.fetch_questions(
                    amount=1
                    # difficulty=aiopentdb.Difficulty.easy
                )
                question = question[0]
                if question.type.value == 'boolean':
                    options = ['True', 'False']
                else:
                    options = [question.correct_answer]
                    options.extend(question.incorrect_answers)
                    options = random.sample(options, len(options)) # Shuffle
                answer = options.index(question.correct_answer)

                if len(options) == 2 and options[0] == 'True' and options[1] == 'False':
                    reactions = ['✅', '❌']
                else:
                    reactions = ['1⃣', '2⃣', '3⃣', '4⃣']

                description = []
                for x, option in enumerate(options):
                    description += '\n {} {}'.format(reactions[x], option)

                embed = discord.Embed(title=question.content, description=''.join(description), color=discord.Colour(0xFF1B1B))
                embed.set_footer(text='Answer using the reactions below⬇')
                quiz_message = await ctx.send(embed=embed)
                for reaction in reactions:
                    await quiz_message.add_reaction(reaction)

            def check(reaction, user):
                return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '1️⃣' or '2️⃣' or '3️⃣' or '4️⃣' or '✅' or '❌')

            try:
                reaction, _ = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(f"Time's Up! :stopwatch:\nAnswer is **{options[answer]}**")
            else:
                if str(reaction.emoji) == reactions[answer]:
                    await ctx.send("Correct answer:sparkles:")
                else:
                    await ctx.send(f"Wrong Answer :no_entry_sign:\nAnswer is **{options[answer]}**")
        except:
            return await ctx.send('Failed to start quiz :x:')

def setup(bot):
    bot.add_cog(games(bot))