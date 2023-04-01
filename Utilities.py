# -*- coding: utf-8 -*-
import contextlib
import io
import logging
import os
import random
import base64
import pprint
import traceback

import aiohttp
import discord
from discord.ext.commands.errors import CommandNotFound, MissingPermissions
import pymysql.cursors
from classes import NotGuildOwner, NotVoter
from discord.ext import commands

columnNames = ["defaultPrefix", "prefix1", "prefix2", "prefix3", "prefix4", "prefix5"]


def DotenvVar(var: str):
    return os.getenv(var)

topggSession = aiohttp.ClientSession(headers={"Authorization": DotenvVar("top-gg-auth")})

def EmojiBool(bool: bool):
    switch = {
        True: "<:Icons_correct:1017402689027592222>",
        False: "<:Wrong:1017402708703064144>",
    }
    return switch.get(bool, "N/A")











