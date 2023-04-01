import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb

class ready(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://PRINCE123:nxtontop@cluster0.wr5qth2.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.connection["Rbot"]["servers"]

    @commands.Cog.listener()
    async def on_ready(self):
        for server in self.client.guilds:
            data = await self.db.find_one({"guild": server.id})
            if data == None:
                await self.db.insert_one(
                    {
                        "guild": server.id,
                        "welcome": {
                            "message": None,
                            "channel": None,
                            "enabled": False,
                            "embed": False,
                            "title": None,
                            "description": None,
                            "thumbnail": None,
                            "footer": None,
                            "image": None
                        }
                    }
                )

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.db.insert_one(
            {
                "guild": guild.id,
                "welcome": {
                    "message": None,
                    "channel": None,
                    "enabled": False,
                    "embed": False,
                    "title": None,
                    "description": None,
                    "thumbnail": None,
                    "footer": None,
                    "image": None
                }
            }
        )


def setup(client):
    client.add_cog(ready(client))