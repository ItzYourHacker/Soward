
import asyncio
import validators
import json as json_but_pain

from discord import Embed
from config import MAIN_COLOR, RED_COLOR


def success_embed(title, description):
    return Embed(
        title=title,
        description=description,
        color=MAIN_COLOR
    )


def error_embed(title, description):
    return Embed(
        title=title,
        description=description,
        color=RED_COLOR
    )

