import discord
import asyncio
import json
import typing as t

from discord.ext import commands
from config import (
    EMOJIS, SUPPORT_SERVER_LINK
)
from embed import error_embed, success_embed
from bot import Bot
from ui import SelfRoleEditor, SelfRoleOptionSelecter
from converters import Lower
from message import wait_for_msg
from recursive_utils import prepare_emojis_and_roles
from reactions import prepare_rolemenu


class config(commands.Cog, description="Self role module"):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command(help="Configure self roles for members in your server!", aliases=['selfrole', 'reactionrole'])
    @commands.has_permissions(manage_guild=True, manage_roles=True)
    @commands.bot_has_permissions(administrator=True)
    @commands.cooldown(3, 120, commands.BucketType.guild)
    @commands.max_concurrency(3, commands.BucketType.guild)
    async def selfroles(self, ctx: commands.Context, option: Lower = None, message_id: t.Optional[int] = None):
       # async with ctx.typing():
            prefix = ctx.clean_prefix
            guild_self_roles = await self.client.self_roles.find_one({"_id": ctx.guild.id})
            if guild_self_roles is None:
                await self.client.self_roles.insert_one({
                    "_id": ctx.guild.id,
                    "role_menus": {}
                })
                guild_self_roles = await self.client.self_roles.find_one({"_id": ctx.guild.id})
            role_menus = guild_self_roles['role_menus']
            info_embed = success_embed(
                f"{EMOJIS['reaction']} Self Roles",
                f"""

**You can use the following commands to configure role menus:**
 `{prefix}selfrole create` \n
 `{prefix}selfrole edit` \n
 `{prefix}selfrole delete` \n
 `{prefix}selfrole list` \n
                """
            )
            if not option:
                ctx.command.reset_cooldown(ctx)
                return await ctx.reply(embed=info_embed)
            if option in ['create', 'new']:
                if len(role_menus) >= 20:
                    return await ctx.reply("You can only have max `20` rolemenus.")
                view = SelfRoleOptionSelecter(ctx)
                main_msg = await ctx.reply(embed=success_embed(
                    f"{EMOJIS['loading']} Rolemenu creation...",
                    "Please select a rolemenu type for this rolemenu!"
                ), view=view)
                await view.wait()
                if view.value is None:
                    ctx.command.reset_cooldown(ctx)
                    return await main_msg.edit(content=f"{EMOJIS['tick_no']}Command cancelled.", embed=None, view=None)
                self_role_type = view.value
                await main_msg.edit(embed=success_embed(
                    f"{EMOJIS['loading']} Rolemenu creation...",
                    "Please send the channel in which you want the rolemenu to be in."
                ), view=None)
                m = await wait_for_msg(ctx, 60, main_msg)
                if m == 'pain':
                    ctx.command.reset_cooldown(ctx)
                    return
                try:
                    text_channel = await commands.TextChannelConverter().convert(ctx, m.content)
                except Exception:
                    await main_msg.delete()
                    raise commands.ChannelNotFound(m.content)
                if self_role_type == 'reaction':
                    await main_msg.edit(embed=success_embed(
                        f"{EMOJIS['loading']} Rolemenu creation...",
                        "If you would like to have the rolemenu in an already sent message, please enter the message ID of that message.\n\nYou can send `none` to skip this step."
                    ))
                    m = await wait_for_msg(ctx, 60, main_msg)
                    if m == 'pain':
                        return
                    if m.content.lower() != 'none':
                        try:
                            custom_msg = await text_channel.fetch_message(int(m.content.lower()))
                            custom_msg_id = custom_msg.id
                        except Exception:
                            custom_msg_id = None
                            await ctx.send("I wasn't able to find the message from your message ID, so I will create a rolemenu message for you.")
                    else:
                        custom_msg_id = None
                else:
                    custom_msg_id = None
                await main_msg.edit(embed=success_embed(
                    f"{EMOJIS['loading']} Rolemenu creation...",
                    "Please send all the roles separated with a comma `,`.\n\nExample: `@amoungus, @18+, @18-, Female, @Male`\nPlease follow this format."
                ))
                m = await wait_for_msg(ctx, 60, main_msg)
                if m == 'pain':
                    return
                roles_text_list = m.content.replace(" ", "").split(",")
                roles = []
                for role_text in roles_text_list:
                    try:
                        role = await commands.RoleConverter().convert(ctx, role_text)
                        if role.position < ctx.guild.me.top_role.position and (role.position < ctx.author.top_role.position or ctx.author == ctx.guild.owner) and role not in roles:
                            roles.append(role)
                    except Exception:
                        pass
                if len(roles) == 0:
                    ctx.command.reset_cooldown(ctx)
                    return await main_msg.edit(embed=error_embed(
                        f"{EMOJIS['tick_no']} Error!",
                        f"Looks like no roles were found in your message.\nOr all the roles were above my top role.\nYou can join our **[Support Server](https://discord.gg/pt9HeCrFek)** for help."
                    ))
                final_output = await prepare_emojis_and_roles(ctx, roles, main_msg)
                if final_output is None:
                    return
                msg_id = await prepare_rolemenu(ctx, final_output, text_channel, self_role_type, custom_msg_id)
                role_menus = guild_self_roles['role_menus']
                role_menus.update({
                    str(msg_id): {
                        "type": self_role_type,
                        "channel": text_channel.id,
                        "stuff": final_output
                    }
                })
                await self.client.self_roles.update_one(
                    filter={"_id": ctx.guild.id},
                    update={"$set": {"role_menus": role_menus}}
                )
                return await main_msg.edit(content=f"The rolemenu has been setup in {text_channel.mention}", embed=None, view=None)
            if option in ['delete', 'remove']:
                if message_id is None:
                    ctx.command.reset_cooldown(ctx)
                    return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Invalid Usage!", "Please mention a message ID."))
                if str(message_id) not in role_menus:
                    ctx.command.reset_cooldown(ctx)
                    return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Not found!", "This rolemenu doesn't exist."))
                role_menus.pop(str(message_id))
                await self.client.self_roles.update_one(
                    filter={"_id": ctx.guild.id},
                    update={"$set": {"role_menus": role_menus}}
                )
                return await ctx.reply(embed=success_embed(f"{EMOJIS['tick_yes']} Rolemenu removed!", "The rolemenu has been removed from the database, you can now delete the message."))
            if option in ['show', 'list']:
                embed = success_embed(
                    f"{EMOJIS['tick_yes']} Your rolemenus!",
                    f"This server has a total of **{len(role_menus)}** rolemenus."
                )
                for msg_id, menu in role_menus.items():
                    embed.add_field(
                        name=msg_id,
                        value=f"""
**Message:** [Click me](https://discord.com/channels/{ctx.guild.id}/{menu['channel']}/{msg_id})
**Menu type:** {menu['type'].title()}
**Roles:** {len(menu['stuff'])}
**Channel:** <#{menu['channel']}>
                        """,
                        inline=False
                    )
                return await ctx.reply(embed=embed)
            if option in ['edit']:
                if message_id is None:
                    ctx.command.reset_cooldown(ctx)
                    return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Invalid Usage!", "Please mention a message ID."))
                if str(message_id) not in role_menus:
                    ctx.command.reset_cooldown(ctx)
                    return await ctx.reply(embed=error_embed(f"{EMOJIS['tick_no']} Not found!", "This rolemenu doesn't exist."))
                view = SelfRoleEditor(ctx)
                main_msg = await ctx.reply(embed=success_embed(
                    f"{EMOJIS['loading']} What would you like to edit?",
                    "Please select an option!"
                ), view=view)
                await view.wait()
                if not view.value:
                    ctx.command.reset_cooldown(ctx)
                    return await main_msg.edit(content=f"{EMOJIS['tick_no']}Command cancelled.", embed=None, view=None)
                if view.value == 'add':
                    await main_msg.edit(embed=success_embed(
                        f"{EMOJIS['loading']} Rolemenu edit...",
                        f"{EMOJIS['tick_yes']} Please send the roles separated with a comma `,`.\n\nExample: `@Artist, @Foodie, @Music Lover, @Cutie`\nPlease follow this format."
                    ), view=None)
                    m = await wait_for_msg(ctx, 60, main_msg)
                    if m == 'pain':
                        return
                    roles_text_list = m.content.replace(" ", "").split(",")
                    roles = []
                    for role_text in roles_text_list:
                        try:
                            role = await commands.RoleConverter().convert(ctx, role_text)
                            if role.position < ctx.guild.me.top_role.position and (role.position < ctx.author.top_role.position or ctx.author == ctx.guild.owner) and role not in roles:
                                roles.append(role)
                        except Exception:
                            pass
                    if len(roles) == 0:
                        ctx.command.reset_cooldown(ctx)
                        return await main_msg.edit(embed=error_embed(
                            f"{EMOJIS['tick_no']} Error!",
                            f"Looks like no roles were found in your message.\nOr all the roles were above my top role.\nYou can join our **[Support Server]({SUPPORT_SERVER_LINK})** for help."
                        ))
                    await main_msg.edit(content="", embed=success_embed(
                        f"{len(roles)} Roles found!",
                        f"I have found **{len(roles)}** in your message.\n\n{' '.join(role.mention for role in roles)}\n\nNow you need to react to this message with the corresponding emojis for the rolemenu to be complete!"
                    ), view=None)
                    final_output = await prepare_emojis_and_roles(ctx, roles, main_msg)
                    if final_output is None:
                        return
                    current_role_menu = role_menus[str(message_id)]
                    stuff = current_role_menu['stuff']
                    for role_id, emoji in final_output.items():
                        stuff.update({role_id: emoji})
                    current_role_menu.update({"stuff": stuff})
                    role_menus.update({str(message_id): current_role_menu})
                    await self.client.self_roles.update_one(
                        filter={"_id": ctx.guild.id},
                        update={"$set": {"role_menus": role_menus}}
                    )
                    await prepare_rolemenu(ctx, stuff, self.client.get_channel(current_role_menu['channel']), current_role_menu['type'], message_id, edit=True)
                    return await main_msg.edit(content=f"{EMOJIS['tick_yes']}The rolemenu has been updated!", embed=None, view=None)
                if view.value == 'remove':
                    current_role_menu = role_menus[str(message_id)]
                    if len(current_role_menu['stuff']) == 1:
                        ctx.command.reset_cooldown(ctx)
                        return await main_msg.edit(embed=error_embed(
                            f"{EMOJIS['tick_no']} Error!",
                            "There's only one role in the rolemenu! You cannot remove that!"
                        ), view=None)
                    await main_msg.edit(embed=success_embed(
                        f"{EMOJIS['loading']} Rolemenu edit...",
                        f"{EMOJIS['tick_yes']} Please send the roles separated with a comma `,`.\n\nExample: `@Artist, @Foodie, @Music Lover, @Cutie`\nPlease follow this format."
                    ), view=None)
                    m = await wait_for_msg(ctx, 60, main_msg)
                    if m == 'pain':
                        return
                    roles_text_list = m.content.replace(" ", "").split(",")
                    roles = []
                    for role_text in roles_text_list:
                        try:
                            role = await commands.RoleConverter().convert(ctx, role_text)
                            if str(role.id) in role_menus[str(message_id)]['stuff']:
                                roles.append(role)
                        except Exception:
                            pass
                    if len(roles) == 0:
                        ctx.command.reset_cooldown(ctx)
                        return await main_msg.edit(embed=error_embed(
                            f"{EMOJIS['tick_no']} Error!",
                            f"Looks like no roles were found in your message.\nOr all the roles were above my top role.\nYou can join our **[Support Server]({SUPPORT_SERVER_LINK})** for help."
                        ))
                    stuff = current_role_menu['stuff']
                    for role in roles:
                        if str(role.id) in stuff:
                            stuff.pop(str(role.id))
                    current_role_menu.update({"stuff": stuff})
                    role_menus.update({str(message_id): current_role_menu})
                    await self.client.self_roles.update_one(
                        filter={"_id": ctx.guild.id},
                        update={"$set": {"role_menus": role_menus}}
                    )
                    await prepare_rolemenu(ctx, stuff, self.client.get_channel(current_role_menu['channel']), current_role_menu['type'], message_id, edit=True)
                    return await main_msg.edit(content=f"{EMOJIS['tick_yes']}The rolemenu has been updated!", embed=None, view=None)

            await ctx.reply(embed=info_embed)


def setup(client):
    client.add_cog(config(client))