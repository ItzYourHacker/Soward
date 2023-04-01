import discord
from discord.ext import commands
from bot import Bot


class ReactionRoles(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener("on_raw_reaction_add")
    async def give_role(self, payload: discord.RawReactionActionEvent):
        self_roles = await self.client.self_roles.find_one({"_id": payload.guild_id})
        if self_roles is None:
            return

        role_menus = self_roles['role_menus']
        if str(payload.message_id) not in role_menus:
            return

        menu = role_menus[str(payload.message_id)]
        if menu['type'] != 'reaction':
            return

        for role_id, emoji in menu['stuff'].items():
            if emoji == str(payload.emoji):
                guild = self.client.get_guild(payload.guild_id)
                role = guild.get_role(int(role_id))
                if role is not None:
                    await payload.member.add_roles(role, Reason="Ethrex Selfroles")
                    return

    @commands.Cog.listener("on_raw_reaction_remove")
    async def remove_role(self, payload: discord.RawReactionActionEvent):
        self_roles = await self.client.self_roles.find_one({"_id": payload.guild_id})
        if self_roles is None:
            return

        role_menus = self_roles['role_menus']
        if str(payload.message_id) not in role_menus:
            return

        menu = role_menus[str(payload.message_id)]
        if menu['type'] != 'reaction':
            return

        for role_id, emoji in menu['stuff'].items():
            if emoji == str(payload.emoji):
                guild = self.client.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                role = guild.get_role(int(role_id))
                if role is not None:
                    await member.remove_roles(role, reason="Ethrex Selfroles")
                    return


def setup(client: Bot):
    client.add_cog(ReactionRoles(client))