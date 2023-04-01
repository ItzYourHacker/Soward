import discord
from typing import List
from discord.ext import commands

class LookingForButton(discord.ui.Button):
    sep = '\u2001'

    def __init__(self, disabled: bool = False, label: str = None):
        super().__init__(style=discord.ButtonStyle.blurple, label=(label or f'{self.sep*11}Join this game!{self.sep*11}'), disabled=disabled)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: LookingToPlay = self.view
        if interaction.user and interaction.user.id == view.ctx.author.id:
            return await interaction.response.send_message("You can't do that!", ephemeral=True)
        view.value = interaction.user
        view.stop()


class CancelGame(discord.ui.Button):
    def __init__(self, disabled : bool=False, label : str=None):
        sep = '\u2001'
        super().__init__(label="Cancel", style=discord.ButtonStyle.red, row=2, disabled=disabled)

    async def callback(self, interaction : discord.Interaction):
        assert self.view is not None
        view : LookingToPlay = self.view
        
        if interaction.user.id == view.ctx.author.id:
            view.value = None
            
            for item in view.children:
                item.disabled = True
                item.label = item.label.replace("Cancel", "Cancelled!").replace("Join this game!\u2001", "The game has ended!")
            await view.message.edit(view=view)
            view.stop()
            
        else:
            await interaction.response.send_message("Only the author of this game can do that!", ephemeral=True)


class LookingToPlay(discord.ui.View):
    def __init__(self, timeout : int=120, label : str=None):
        super().__init__(timeout=timeout)
        self.message : discord.Message = None
        self.value : discord.User = None
        self.ctx : commands.Context = None
        self.add_item(LookingForButton(label=label))
        self.add_item(CancelGame())

    async def on_timeout(self) -> None:
        for button in self.children:
            button.disabled = True
            button.label = button.label.replace("Join this game!\u2001", "The game has ended!")
        await self.message.edit(content=":alarm_clock: Timed out! The game has ended!", view=self)


class TicTacToeButton(discord.ui.Button['TicTacToe']):
    def __init__(self, x : int, y : int):
        super().__init__(label='  ', style=discord.ButtonStyle.secondary, row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction : discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.player1:
            self.style = discord.ButtonStyle.blurple
            self.label = '\U0001f1fd'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            
        else:
            self.style = discord.ButtonStyle.red
            self.label = '🅾'
            self.disabled = True
            view.board[self.y][self.x] = view.O

        winner = view.check_board_winner()
        if winner is not None:
            
            if winner == view.X:
                content = f"\U0001f1fd :tada: __**{view.current_player.mention} WON!!!**__ :tada:"
                
            elif winner == view.O:
                content = f"🅾 :tada: __**{view.current_player.mention} WON!!!**__ :tada:"
                
            else:
                content = f"\U0001f454 It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        else:
            
            if view.current_player == view.player1:
                view.current_player = view.player2
                content = f"🅾 It's {view.current_player.mention}'s turn"
                
            else:
                view.current_player = view.player1
                content = f"\U0001f1fd It's {view.current_player.mention}'s turn"

        await interaction.response.edit_message(content=content, view=view)


class TicTacToe(discord.ui.View):
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self, ctx, player1 : discord.Member, player2 : discord.Member, starter : discord.User):
        super().__init__()
        self.current_player = starter
        self.ctx : commands.Context = ctx
        self.player1 : discord.Member = player1
        self.player2 : discord.Member = player2
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

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

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user and interaction.user.id == self.current_player.id:
            return True
        
        elif interaction.user and interaction.user.id in (self.player1.id, self.player2.id):
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            
        elif interaction.user:
            await interaction.response.send_message("You aren't a part of this game!", ephemeral=True)
            
        return False
