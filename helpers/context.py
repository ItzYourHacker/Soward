import re
import typing
import random
import pygit2
import discord
import datetime
import itertools

from discord import Interaction
from discord.ext import commands
from asyncdagpi import Client, ImageFeatures

target_type = typing.Union[discord.Member, discord.User, discord.PartialEmoji, discord.Guild, discord.Invite]

class ConfirmButton(discord.ui.Button):
    def __init__(self, label: str, emoji: str, button_style: discord.ButtonStyle):
        super().__init__(style=button_style, label=label, emoji=emoji, )

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: Confirm = self.view
        view.value = True
        view.stop()


class CancelButton(discord.ui.Button):
    def __init__(self, label: str, emoji: str, button_style: discord.ButtonStyle):
        super().__init__(style=button_style, label=label, emoji=emoji)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: Confirm = self.view
        view.value = False
        view.stop()


class Confirm(discord.ui.View):
    def __init__(self, buttons: typing.Tuple[typing.Tuple[str]], timeout: int = 30):
        super().__init__(timeout=timeout)
        self.message = None
        self.value = None
        self.ctx: CustomContext = None
        self.add_item(ConfirmButton(emoji=buttons[0][0],
                                    label=buttons[0][1],
                                    button_style=(
                                            buttons[0][2] or discord.ButtonStyle.green
                                    )))
        self.add_item(CancelButton(emoji=buttons[1][0],
                                   label=buttons[1][1],
                                   button_style=(
                                           buttons[1][2] or discord.ButtonStyle.red
                                   )))

    async def interaction_check(self, interaction: Interaction) -> bool:
        if interaction.user and interaction.user.id in (self.ctx.bot.owner_id, self.ctx.author.id):
            return True
        messages = [
            "Oh no you can't do that! This belongs to **{user}**",
            'This is **{user}**\'s confirmation, sorry! 💢',
            '😒 Does this look yours? **No**. This is **{user}**\'s confirmation button',
            f'STOP IT GET SOME HELP',
            'HEYYYY!!!!! this is **{user}**\'s menu.',
            'Sorry but you can\'t mess with **{user}**\' menu :(',
            'No. just no. This is **{user}**\'s menu.',
            'Stop.',
            'You don\'t look like {user} do you...',
            '🤨 That\'s not yours! That\'s **{user}**\'s menu',
            '🧐 Whomst! you\'re not **{user}**',
            '_out!_ 👋'
        ]
        await interaction.response.send_message(random.choice(messages).format(user=self.ctx.author.display_name),
                                                ephemeral=True)

        return False


class CustomContext(commands.Context):

    @staticmethod
    def tick(option: bool, text: str = None):
        ticks = {
            True: '<:greenTick:895688440690147370>',
            False: '<:redTick:895688440568508518>',
            None: '<:greyTick:895688440690114560>'}

        emoji = ticks.get(option, "<:redTick:596576672149667840>")

        if text:
            return f"{emoji} {text}"

        return emoji

    @staticmethod
    def toggle(option: bool):
        ticks = {
            True: '<:toggle_on:896743740285263892>',
            False: '<:toggle_off:896743704323309588>',
            None: '<:toggle_off:896743704323309588>'}

        emoji = ticks.get(option, "<:toggle_off:896743704323309588>")
        return emoji

    @staticmethod
    def time(days: int, hours: int, minutes: int, seconds: int):
        def remove_s(string):
            if re.match(r"\d+", string).group() == "1":
                return string[:-1]
            return string

        days = remove_s(f"{days} days")
        hours = remove_s(f"{hours} hours")
        minutes = remove_s(f"{minutes} minutes")
        seconds = remove_s(f"{seconds} seconds")

        return " and ".join(", ".join(filter(lambda i: int(i[0]), (days, hours, minutes, seconds))).rsplit(", ", 1))

    @staticmethod
    def short_time(days: int, hours: int, minutes: int, seconds: int):
        def remove_s(string):
            if re.match(r"\d+", string).group() == "1":
                return string[:-1]
            return string

        days = remove_s(f"{days}d")
        hours = remove_s(f"{hours}h")
        minutes = remove_s(f"{minutes}m")
        seconds = remove_s(f"{seconds}s")

        return " and ".join(", ".join(filter(lambda i: int(i[0]), (days, hours, minutes, seconds))).rsplit(", ", 1))

    @staticmethod
    def uptime(bot):
        delta_uptime = discord.utils.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        def remove_s(string):
            if re.match(r"\d+", string).group() == "1":
                return string[:-1]
            return string

        days = remove_s(f"{days}d")
        hours = remove_s(f"{hours}h")
        minutes = remove_s(f"{minutes}m")
        seconds = remove_s(f"{seconds}s")

        return " and ".join(", ".join(filter(lambda i: int(i[0]), (days, hours, minutes, seconds))).rsplit(", ", 1))

    @staticmethod
    def get_last_commits(count=3):
        def format_commit(commit):
            short, _, _ = commit.message.partition('\n')
            short_sha2 = commit.hex[0:6]
            commit_tz = datetime.timezone(datetime.timedelta(minutes=commit.commit_time_offset))
            commit_time = datetime.datetime.fromtimestamp(commit.commit_time).astimezone(commit_tz)

            offset = discord.utils.format_dt(commit_time.astimezone(datetime.timezone.utc), 'R')
            return f'[`{short_sha2}`](https://github.com/Ender2K89/Stealth-Bot/commit/{commit.hex}) {short} ({offset})'

        repo = pygit2.Repository('.git')
        commits = list(itertools.islice(repo.walk(repo.head.target, pygit2.GIT_SORT_TOPOLOGICAL), count))
        return '\n'.join(format_commit(c) for c in commits)

    async def send(self, content: str = None, embed: discord.Embed = None, reminders: bool = True,
                   reply: bool = True, footer: bool = True, timestamp: bool = True, color: bool = True,
                   reference: typing.Union[discord.Message, discord.MessageReference] = None, **kwargs) -> discord.Message:

        reference = (reference or self.message.reference or self.message) if reply is True else reference

        if self.bot.theme == "default":
            colors = [0x910023, 0xA523FF]
            emotes = []
            unicode_emotes = []
            star_emoji = [":star:", ":star2:"]

        elif self.bot.theme == "halloween":
            colors = [0xFF9A00, 0x000000, 0x09FF00, 0xC900FF, 0xFBFAF4]
            emotes = [':ghost:', ':jack_o_lantern:']
            unicode_emotes = ['👻', '🎃']
            star_emoji = ['<a:pumpkinhappy:919661769683771432>', '<a:pumpkindead:919662049322221610>', '<:ghostlove:919662188451495966>']

        elif self.bot.theme == "christmas":
            colors = [0xB3000C, 0xE40010, 0xD8D8D8, 0x1FD537, 0x1FD537]
            emotes = [':santa:', ':christmas_tree:', ':deer:', ':gift:', ':snowflake:']
            unicode_emotes = ['🎅', '🎄', '🦌', '🎁', '❄']
            star_emoji = ['<:blurple_sparkle:919660492086202438>', '<:red_sparkle:919660756478353500>', '<:pink_sparkle:919660699674902528>', '<:yellow_sparkle:919660787847528478>', '<:green_sparkle:919660572310667294>']

        else:
            colors = [0x910023, 0xA523FF]
            emotes = []
            unicode_emotes = []
            star_emoji = [":star:", ":star2:"]

        if embed:
            if embed.description:
                embed.description = embed.description # '\n'.join([l.strip() for l in content.split('\n')])

            if footer:
                embed.set_footer(text=f"{f'{random.choice(unicode_emotes)} ' if unicode_emotes else ''}Requested by {self.author}", icon_url=self.author.display_avatar.url)

            if not footer and embed.footer:
                embed.set_footer(text=f"{f'{random.choice(unicode_emotes)} ' if unicode_emotes else ''}{embed.footer.text}", icon_url=embed.footer.icon_url if embed.footer.icon_url else discord.Embed.Empty)

            if timestamp:
                embed.timestamp = discord.utils.utcnow()

            if color:
                color = random.choice(colors)
                embed.color = color

        if reminders:
            answers = [f"{random.choice(star_emoji)} Help **Ethrex Bot** grow by voting on top.gg: **<>**", f'{random.choice(star_emoji)} Feature not working like it\'s supposed to? Join our support server: **<https://discord.gg/jkop>**', f'{random.choice(star_emoji)} Got a question? DM me and the developer will respond as fast as they can!']
            number = random.randint(1, 10)

            content = content

            if number == 1:
                content = f"{random.choice(answers)}\n\n{str(content) if content else ''}"

        try:
            return await super().send(content=content, embed=embed, reference=reference, **kwargs)

        except discord.HTTPException:
            return await super().send(content=content, embed=embed, reference=None, **kwargs)

    async def confirm(self, message: str = 'Do you want to confirm?',
                      buttons: typing.Tuple[typing.Union[discord.PartialEmoji, str],
                                            str, discord.ButtonStyle] = None, timeout: int = 30,
                      delete_after_confirm: bool = False,
                      delete_after_timeout: bool = False,
                      delete_after_cancel: bool = None,
                      return_message: bool = False) \
            -> typing.Union[bool, typing.Tuple[bool, discord.Message]]:
        """ A confirmation menu. """

        delete_after_cancel = delete_after_cancel if delete_after_cancel is not None else delete_after_confirm

        view = Confirm(buttons=buttons or (
            (None, 'Confirm', discord.ButtonStyle.green),
            (None, 'Cancel', discord.ButtonStyle.red)
        ), timeout=timeout)
        view.ctx = self
        message = await self.send(message, view=view)
        await view.wait()
        if False in (delete_after_cancel, delete_after_confirm, delete_after_timeout):
            view.children = [view.children[0]]
            for c in view.children:
                c.disabled = True
                if view.value is False:
                    c.label = 'Cancelled!'
                    c.emoji = None
                    c.style = discord.ButtonStyle.red
                elif view.value is True:
                    c.label = 'Confirmed!'
                    c.emoji = None
                    c.style = discord.ButtonStyle.green
                else:
                    c.label = 'Timed out!'
                    c.emoji = '⏰'
                    c.style = discord.ButtonStyle.gray
        view.stop()
        if view.value is None:

            try:
                if return_message is False:
                    (await message.edit(view=view)) if delete_after_timeout is False else (await message.delete())
            except (discord.Forbidden, discord.HTTPException):
                pass
            return (None, message) if delete_after_timeout is False and return_message is True else None

        elif view.value:

            try:
                if return_message is False:
                    (await message.edit(view=view)) if delete_after_confirm is False else (await message.delete())
            except (discord.Forbidden, discord.HTTPException):
                pass
            return (True, message) if delete_after_confirm is False and return_message is True else True

        else:

            try:
                if return_message is False:
                    (await message.edit(view=view)) if delete_after_cancel is False else (await message.delete())
            except (discord.Forbidden, discord.HTTPException):
                pass

            return (False, message) if delete_after_cancel is False and return_message is True else False


    async def trigger_typing(self) -> None:
        try:
            await super().trigger_typing()

        except (discord.Forbidden, discord.HTTPException):
            pass

    async def dagpi(self, target: target_type = None, *, feature: ImageFeatures, **kwargs) -> discord.File:
        await self.trigger_typing()
        target = target or self.reference
        return await self.bot.dagpi_request(self, target, feature=feature, **kwargs)

    async def waifu(self, feature: str, **kwargs) -> discord.File:
        await self.trigger_typing()
        return await self.bot.waifu_request(self, feature=feature, **kwargs)

    @property
    def reference(self) -> typing.Optional[discord.Message]:
        return getattr(self.message.reference, 'resolved', None)