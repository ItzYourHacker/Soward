import discord
#from discord import VoiceRegion
import datetime
from dateutil.relativedelta import relativedelta
from discord.flags import BaseFlags, fill_with_flags, flag_value
from discord.ext import commands
import re
import typing

YOUTUBE_BARS = (
    (
        '<:bar_start_full:909502832082837514>',
        '<:bar_start_mid:909504169398915184>',
        None,
    ),
    
    (
        '<:bar_center_full:909503128058093590>',
        '<:bar_center_mid:909504186146779177>',
        '<:bar_center_empty:909504484076585030>',
        
    ),
    
    (
        '<:bar_end_full:909503316357173300>',
        '<:bar_end_mid:909504194598301816>',
        '<:bar_end_empty:909504491072684032>',
    ),
)

def generate_youtube_bar(position: int, duration: int, bar_length: int,
                         bar_style: typing.Tuple[typing.Tuple[str, str, str]] = None) -> str:
    bar_length = bar_length if bar_length > 0 else 1
    duration = duration if duration > 0 else 1
    played = int((position / duration) * bar_length)
    missing = int(bar_length - played)
    bars = bar_style or YOUTUBE_BARS
    bar = []
    if played == 0 and missing > 0:
        bar += [bars[0][1]]
        bar += [bars[1][2] * (missing - 2)]
        bar += [bars[2][2]]

    elif played > 0 and missing == 0:
        bar += [bars[0][0]]
        bar += [bars[1][0] * (played - 2)]
        bar += [bars[2][1]]

    elif played > 0 and missing > 0:
        bar += [bars[0][0]]
        bar += [bars[1][0] * (played - 1)]
        bar += [bars[1][1]]
        bar += [bars[1][2] * (missing - 2)]
        bar += [bars[2][2]]

    elif played > missing:
        bar += [bars[0][0]]
        bar += [bars[1][0] * (bar_length - 2)]
        bar += [bars[2][0]]

    return ''.join(bar)


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size


def deltaconv(s):
    hours = s // 3600
    s = s - (hours * 3600)
    minutes = s // 60
    seconds = s - (minutes * 60)
    if hours > 0:
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    return '{:02}:{:02}'.format(int(minutes), int(seconds))


def get_member_permissions(permissions):
    perms = []
    
    if permissions.administrator:
        perms.append("Administrator")
        
        return "Administrator"
    
    if permissions.manage_guild:
        perms.append("Manage guild")
        
    if permissions.ban_members:
        perms.append("Ban members")
        
    if permissions.kick_members:
        perms.append("Kick members")
        
    if permissions.manage_channels:
        perms.append("Manage channels")
        
    if permissions.manage_emojis:
        perms.append("Manage custom emotes")
        
    if permissions.manage_messages:
        perms.append("Manage messages")
        
    if permissions.manage_permissions:
        perms.append("Manage permissions")
        
    if permissions.manage_roles:
        perms.append("Manage roles")
        
    if permissions.mention_everyone:
        perms.append("Mention everyone")
        
    if permissions.manage_emojis:
        perms.append("Manage emojis")
        
    if permissions.manage_webhooks:
        perms.append("Manage webhooks")
        
    if permissions.move_members:
        perms.append("Move members")
        
    if permissions.mute_members:
        perms.append("Mute members")
        
    if permissions.deafen_members:
        perms.append("Deafen members")
        
    if permissions.priority_speaker:
        perms.append("Priority speaker")
        
    if permissions.view_audit_log:
        perms.append("See audit log")
        
    if permissions.create_instant_invite:
        perms.append("Create instant invites")
    
    return ", ".join(perms) if perms else 'No permissions'


def get_member_badges(member, fetched_member):
    author_flags = member.public_flags
    flags = dict(author_flags)
    
    emotes = []
    text = []
        
    # Hypesquad
    
    if flags['hypesquad']:
        emotes.append("<:hypesquad:895688440610422900>")
        text.append("Hypesquad")
    
    if flags['hypesquad_bravery']:
        emotes.append("<:bravery:919659862030450758>")
        text.append("Hypesquad bravery")

    if flags['hypesquad_brilliance']:
        emotes.append("<:brilliance:919659887984791563>")
        text.append("Hypesquad brilliance")

    if flags['hypesquad_balance']:
        emotes.append("<:balance:919659908331368478>")
        text.append("Hypesquad balance")
        
    # Bug hunter

    if flags['bug_hunter']:
        emotes.append("{<:bughunter:895688440534937620>")
        text.append("Bug hunter 1")
        
    if flags['bug_hunter_level_2']:
        emotes.append("<:bughunter_gold:895688440610422899>")
        text.append("Bug hunter 2")
        
    # Premium
    
    if fetched_member.banner:
        emotes.append("<:nitro:895688440702726175>")
        text.append("Nitro user")

    if member.avatar and "<:nitro:895688440702726175>" not in emotes and "Nitro user" not in text:
        if member.avatar.is_animated() or member.guild_avatar and member.guild_avatar != member.avatar:
            emotes.append("<:nitro:895688440702726175>")
            text.append("Nitro user")
        
    if member.premium_since:
        emotes.append("<:boost:858326699234164756>")
        text.append("Booster")

    if flags['early_supporter']:
        emotes.append("<:supporter:896381619731071006>")
        text.append("Early supporter")
        
    # Other
    
    if flags['staff']:
        emotes.append("<:staff:858326975869485077>")
        text.append("Staff")

    if flags['partner']:
        emotes.append("<:partnernew:895688440933416980>")
        text.append("Partner")

    if flags['verified_bot_developer']:
        emotes.append("<:earlybotdev:895688440547520513>")
        text.append("Bot developer")

    if flags['verified_bot']:
        emotes.append("<:verified_bot:918166172631969843>")
        text.append("Verified bot")
        
    if flags['discord_certified_moderator']:
        emotes.append("<:certified_moderator:895688440589484072>")
        text.append("Certified moderator")
        
    if flags['system']:
        emotes.append("<a:loading:747680523459231834>")
        text.append("System")
        
    if flags['team_user']:
        emotes.append("TEAM USER")
        text.append("Team user")
        
    joined_emotes = " ".join(emotes)
    joined_text = ", ".join(text)

    return f"[{joined_emotes}](https://discord.com/users/{member.id}/ \"{joined_text}\")" if emotes and text else "No badges found..."

def get_server_region_emote(server: discord.Guild):
    r = discord.VoiceRegion.us_central
    region = server.region

    if region == VoiceRegion.amsterdam:
        return "🇳🇱"
    if region == VoiceRegion.brazil:
        return "🇧🇷"
    if region == VoiceRegion.dubai:
        return "🇦🇪"
    if region == VoiceRegion.eu_central:
        return "🇪🇺"
    if region == VoiceRegion.eu_west:
        return "🇪🇺"
    if region == VoiceRegion.europe:
        return "🇪🇺"
    if region == VoiceRegion.frankfurt:
        return "🇩🇪"
    if region == VoiceRegion.hongkong:
        return "🇭🇰"
    if region == VoiceRegion.india:
        return "🇮🇳"
    if region == VoiceRegion.japan:
        return "🇯🇵"
    if region == VoiceRegion.london:
        return "🇬🇧"
    if region == VoiceRegion.russia:
        return "🇷🇺"
    if region == VoiceRegion.singapore:
        return "🇸🇬"
    if region == VoiceRegion.southafrica:
        return "🇿🇦"
    if region == VoiceRegion.south_korea:
        return "🇰🇷"
    if region == VoiceRegion.sydney:
        return "🇦🇺"
    if region == VoiceRegion.us_central:
        return "🇺🇸"
    if region == VoiceRegion.us_east:
        return "🇺🇸"
    if region == VoiceRegion.us_south:
        return "🇺🇸"
    if region == VoiceRegion.us_west:
        return "🇺🇸"
    if region == VoiceRegion.vip_amsterdam:
        return "🇳🇱🌟"
    if region == VoiceRegion.vip_us_east:
        return "🇺🇸🌟"
    if region == VoiceRegion.vip_us_west:
        return "🇺🇸🌟"
    else:
        return ":x:"


def get_server_region(server: discord.Guild):
    r = discord.VoiceRegion.us_central
    region = server.region
    
    if region == VoiceRegion.amsterdam:
        return "Amsterdam"
    if region == VoiceRegion.brazil:
        return "Brazil"
    if region == VoiceRegion.dubai:
        return "Dubai"
    if region == VoiceRegion.eu_central:
        return "EU central"
    if region == VoiceRegion.eu_west:
        return "EU west"
    if region == VoiceRegion.europe:
        return "Europe"
    if region == VoiceRegion.frankfurt:
        return "Frankfurt"
    if region == VoiceRegion.hongkong:
        return "Hong Kong"
    if region == VoiceRegion.india:
        return "India"
    if region == VoiceRegion.japan:
        return "Japan"
    if region == VoiceRegion.london:
        return "London"
    if region == VoiceRegion.russia:
        return "Russia"
    if region == VoiceRegion.singapore:
        return "Singapore"
    if region == VoiceRegion.southafrica:
        return "South Africa"
    if region == VoiceRegion.south_korea:
        return "South Korea"
    if region == VoiceRegion.sydney:
        return "Sydney"
    if region == VoiceRegion.us_central:
        return "US Central"
    if region == VoiceRegion.us_east:
        return "US East"
    if region == VoiceRegion.us_south:
        return "US South"
    if region == VoiceRegion.us_west:
        return "US West"
    if region == VoiceRegion.vip_amsterdam:
        return "VIP Amsterdam"
    if region == VoiceRegion.vip_us_east:
        return "VIP US East"
    if region == VoiceRegion.vip_us_west:
        return "VIP US West"
    if str(region) == 'atlanta':
        return "🇺🇸 Atlanta"
    if str(region) == 'santa-clara':
        return "🇺🇸 Santa Clara"
    else:
        return "Unknown region"


def get_server_verification_level_emote(server: discord.Guild):
    verification_level = server.verification_level

    if str(server.verification_level).lower() == "low":
        return "<:low_verification:904471431759417405>"

    elif str(server.verification_level).lower() == "medium":
        return "<:medium_verification:904471432220782602>"

    elif str(server.verification_level).lower() == "high":
        return "<:high_verification:904471431809753129>"

    elif str(server.verification_level).lower() == "highest":
        return "<:highest_verification:904471431742652497>"

    else:
        return "<:none_verification:904471431973339137>"


def get_server_explicit_content_filter(server: discord.Guild):
    explict_content_level = server.explicit_content_filter

    if str(explict_content_level) == "no_role":
        return "Scan media content from members without a role."

    elif str(explict_content_level) == "all_members":
        return "Scan media from all members."

    else:
        return "Don't scan any media content."


def get_server_level_emote(server: discord.Guild):
    premium_tier = server.premium_tier

    if int(premium_tier) == 1:
        return "<:Level1_guild:895688440614649918>"

    elif int(premium_tier) == 2:
        return "<:Level2_guild:895688440589484074>"

    elif int(premium_tier) == 3:
        return "<:Level3_guild:895688440568483871>"

    else:
        return "<:Level0_guild:895688440492986390>"


def get_member_status_emote(member: discord.Member):
    status = str(member.status)

    if status == "online":
        return "<:status_online:925709091375026246>"

    elif status == "idle":
        return "<:status_idle:925709091312132126>"

    elif status == "dnd":
        return "<:status_dnd:925709090997538867>"

    elif status == "streaming":
        return "<:status_streaming:925709091396018186>"

    else:
        return "<:status_offline:925709091328897074>"


def get_member_custom_status(member: discord.Member):
    custom_activity = discord.utils.find(lambda act: isinstance(act, discord.CustomActivity), member.activities)#

    if custom_activity:
        return custom_activity.name

    else:
        return f"No status"


def get_member_activity(member: discord.Member):
    activity = discord.utils.find(lambda act: isinstance(act, discord.Activity) or isinstance(act, discord.Spotify),
                                  member.activities)

    if activity:
        if activity.type == discord.ActivityType.playing:
            return f"Playing **{activity.name}**"

        elif activity.type == discord.ActivityType.streaming:
            return f"Streaming **{activity.name}**"

        elif activity.type == discord.ActivityType.listening:
            return f"Listening To **{activity.name}**"

        elif activity.type == discord.ActivityType.watching:
            return f"Watching **{activity.name}**"

        elif activity.type == discord.ActivityType.custom:
            return f"Custom Activity **{activity.name}**"

        elif activity.type == discord.ActivityType.competing:
            return f"Competing in **{activity.name}**"

    else:
        return f"No activity"


def get_member_client(member: discord.Member):
    desktopStatus = ""
    mobileStatus = ""
    webStatus = ""

    if str(member.desktop_status) == "online":
        desktopStatus = "<:status_online_desktop:904449910622007306>"

    elif str(member.desktop_status) == "idle":
        desktopStatus = "<:status_idle_desktop:904449910626205747>"

    elif str(member.desktop_status) == "dnd":
        desktopStatus = "<:status_dnd_desktop:904449910601035896>"

    elif str(member.desktop_status) == "streaming":
        desktopStatus = "<:status_streaming_desktop:904449910693298287>"

    else:
        desktopStatus = "<:status_offline_desktop:904449910743633961>"

    if str(member.mobile_status) == "online":
        mobileStatus = "<:status_online_mobile:899267887561330728>"

    elif str(member.mobile_status) == "idle":
        mobileStatus = "<:status_idle_mobile:899267832955686943>"

    elif str(member.mobile_status) == "dnd":
        mobileStatus = "<:status_dnd_mobile:899267914304200734>"

    elif str(member.mobile_status) == "streaming":
        mobileStatus = "<:status_streaming_mobile:904449910642987069>"

    else:
        mobileStatus = "<:status_offline_mobile:899267788353449985>"

    if str(member.web_status) == "online":
        webStatus = "<:status_online_web:899368966768689225>"

    elif str(member.web_status) == "idle":
        webStatus = "<:status_idle_web:899368956748501012>"

    elif str(member.web_status) == "dnd":
        webStatus = "<:status_dnd_web:899368975513833532>"

    elif str(member.web_status) == "streaming":
        webStatus = "<:status_streaming_web:904449910710108230>"

    else:
        webStatus = "<:status_offline_web:899368940189413437>"

    return f"[ {desktopStatus} ] [ {mobileStatus} ] [ {webStatus} ]"

def get_member_status_client(member: discord.Member):
    desktopStatus = ""
    mobileStatus = ""
    webStatus = ""
    bruh = []
    status = []

    if str(member.desktop_status) == "online":
        status.append("<:status_online_desktop:904449910622007306>")

    elif str(member.desktop_status) == "idle":
        status.append("<:status_idle_desktop:904449910626205747>")

    elif str(member.desktop_status) == "dnd":
        status.append("<:status_dnd_desktop:904449910601035896>")

    elif str(member.desktop_status) == "streaming":
        status.append("<:status_streaming_desktop:904449910693298287>")

    else:
        bruh.append(member.id)

    if str(member.mobile_status) == "online":
        status.append("<:status_online_mobile:899267887561330728>")

    elif str(member.mobile_status) == "idle":
        status.append("<:status_idle_mobile:899267832955686943>")

    elif str(member.mobile_status) == "dnd":
        status.append("<:status_dnd_mobile:899267914304200734>")

    elif str(member.mobile_status) == "streaming":
        status.append("<:status_streaming_mobile:904449910642987069>")

    else:
        bruh.append(member.id)

    if str(member.web_status) == "online":
        status.append("<:status_online_web:899368966768689225>")

    elif str(member.web_status) == "idle":
        status.append("<:status_idle_web:899368956748501012>")

    elif str(member.web_status) == "dnd":
        status.append("<:status_dnd_web:899368975513833532>")

    elif str(member.web_status) == "streaming":
        status.append("<:status_streaming_web:904449910710108230>")

    else:
        bruh.append(member.id)

    return ' '.join(status)

def get_member_spotify(member: discord.Member):
    spotify = discord.utils.find(lambda act: isinstance(act, discord.Spotify), member.activities)

    if spotify:
        return f"[{spotify.title}]({spotify.track_url}) by {spotify.artist} on {spotify.album}"

    else:
        return f"No spotify"


def get_join_order(member: discord.Member, guild: discord.Guild):
    sort_mems = sorted(guild.members, key=lambda member: member.joined_at)
    index = sort_mems.index(member)
    members = [f'{member}' for member in sort_mems[(index - 3 if index != 0 else index):index + 4]]
    join_position = '```yaml\n' + '\n'.join(
        [f"{n}.     {s}" for n, s in enumerate(members, start=index + 1)]).replace(f"  {member}",
                                                                                   f"> {member}") + '\n```'

    return join_position


def get_member_avatar_urls(member: discord.Member, ctx, id):
    avatars = []
    
    if member.avatar:
        if member.avatar.is_animated():
            avatars.append(f"Avatar: [PNG]({member.avatar.replace(format='png', size=2048).url}) **|** [GIF]({member.avatar.replace(format='webp', size=2048).url})")

        else:
            avatars.append(f"Avatar: [PNG]({member.avatar.replace(format='png', size=2048).url})")
    
    if member.display_avatar != member.avatar:
        if member.display_avatar.is_animated():
            avatars.append(f"Server avatar: [PNG]({member.display_avatar.replace(format='png', size=2048).url}) **|** [GIF]({member.display_avatar.replace(format='webp', size=2048).url})")
        
        else:
            avatars.append(f"Server avatar: [PNG]({member.display_avatar.replace(format='png', size=2048).url})")
            
    return '\n'.join(avatars) if avatars else 'No avatar found...'


def get_member_banner_urls(member: discord.Member, ctx,  id):
    banners = []
    
    if member.banner:
        if member.banner.is_animated():
            banners.append(f"Banner: [PNG]({member.banner.replace(format='png', size=2048).url}) **|** [GIF]({member.banner.replace(format='gif', size=2048).url})")

        else:
            banners.append(f"Banner: [PNG]({member.banner.replace(format='png', size=2048).url})")

    return '\n'.join(banners) if banners else 'No banner found...'


def get_server_banner_urls(guild: discord.Guild):
    banners = []
    
    if guild.banner:
        if guild.banner.is_animated():
            banners.append(f"[PNG]({guild.banner.replace(format='png', size=2048).url}) **|** [GIF]({guild.banner.replace(format='gif', size=2048).url})")

        else:
            banners.append(f"[PNG]({guild.banner.replace(format='png', size=2048).url})")
            
    return '\n'.join(banners) if banners else 'No banner found...'


def get_server_logging(ctx, database, guild: discord.Guild):
    if not database['logs_channel_id']:
        return f"{ctx.tick(False)}"
    
    logs_channel = guild.get_channel(database['logs_channel_id'])
    return f"{ctx.tick(True)} | {logs_channel.mention}"


def get_server_welcome(ctx, database, guild: discord.Guild):
    if not database['welcome_channel_id']:
        return f"{ctx.tick(False)}"
    
    welcome_channel = guild.get_channel(database['welcome_channel_id'])
    return f"{ctx.tick(True)} | {welcome_channel.mention}"


def get_member_color(member: discord.Member):
    if member.color:
        return f"{member.color}"

    else:
        return f"No color found"


def get_member_accent_color(member: discord.Member):
    if member.accent_color:
        return f"{member.accent_color}"

    else:
        return f"No accent color found"


def get_guild_boosts(guild: discord.Guild):
    last_boost = max(guild.members, key=lambda m: m.premium_since or guild.created_at)
    if guild.premium_tier != 0:

        if last_boost and guild.premium_subscription_count and last_boost.premium_since:
            return f"{get_server_level_emote(guild)} Level: {guild.premium_tier:,}\n<:boost:858326699234164756> Boosts: {guild.premium_subscription_count:,}\n<:boost:858326699234164756> __**Last Boost**__\n{last_boost}\n({discord.utils.format_dt(last_boost.premium_since, style='R') if last_boost.premium_since else ''})"

        else:
            return f"{get_server_level_emote(guild)} Level: {guild.premium_tier:,}\n<:boost:858326699234164756> Boosts: {guild.premium_subscription_count:,}"

    else:
        return f"No boosts"
    

def get_member_roles(member: discord.Member, guild: discord.Guild):
        roles = ""
        
        for role in member.roles:
            
            if role is guild.default_role:
                continue
            
            roles = f"{roles} {role.mention}"
            
        if roles != "":
            roles = f"{roles}"
            
        return roles if roles else 'No roles'
    

class NotSH(commands.CheckFailure):
    pass


def is_sh_server():
    def predicate(ctx):
        if ctx.guild.id == 799330949686231050:
            return True
        else:
            raise NotSH("You can only use this command in `Stealth Hangout`!\ndiscord.gg/ktkXwmD2kF")

    return commands.check(predicate)


class NotSPvP(commands.CheckFailure):
    pass


def is_spvp_server():
    def predicate(ctx):
        if ctx.guild.id == 882341595528175686:
            return True
        else:
            raise NotSPvP("You can only use this command in `ClassicPvP`!\nhttps://discord.gg/afBDa2Kqc9")

    return commands.check(predicate)


class Blacklisted(commands.CheckFailure):
    pass


def is_user_blacklisted():
    blacklisted_ids = []

    def predicate(ctx):
        if ctx.author.id not in blacklisted_ids:
            return True
        else:
            raise Blacklisted(
                "It appears that you're blacklisted from this bot. Contact  if you think this is a mistake.")

    return commands.check(predicate)

class plural:
    def __init__(self, value):
        self.value = value

    def __format__(self, format_spec):
        v = self.value
        singular, sep, plural = format_spec.partition('|')
        plural = plural or f'{singular}s'
        if abs(v) != 1:
            return f'{v} {plural}'
        return f'{v} {singular}'


def human_join(seq, delim=', ', final='or'):
    size = len(seq)
    if size == 0:
        return ''

    if size == 1:
        return seq[0]

    if size == 2:
        return f'{seq[0]} {final} {seq[1]}'

    return delim.join(seq[:-1]) + f' {final} {seq[-1]}'


class ShortTime:
    compiled = re.compile("""(?:(?P<years>[0-9])(?:years?|y))?             # e.g. 2y
                             (?:(?P<months>[0-9]{1,2})(?:months?|mo))?     # e.g. 2months
                             (?:(?P<weeks>[0-9]{1,4})(?:weeks?|w))?        # e.g. 10w
                             (?:(?P<days>[0-9]{1,5})(?:days?|d))?          # e.g. 14d
                             (?:(?P<hours>[0-9]{1,5})(?:hours?|h))?        # e.g. 12h
                             (?:(?P<minutes>[0-9]{1,5})(?:minutes?|m))?    # e.g. 10m
                             (?:(?P<seconds>[0-9]{1,5})(?:seconds?|s))?    # e.g. 15s
                          """, re.VERBOSE)

    def __init__(self, argument, *, now=None):
        match = self.compiled.fullmatch(argument)
        if match is None or not match.group(0):
            raise commands.BadArgument('invalid time provided')

        data = {k: int(v) for k, v in match.groupdict(default=0).items()}
        now = now or datetime.datetime.now(datetime.timezone.utc)
        self.dt = now + relativedelta(**data)

    @classmethod
    async def convert(cls, ctx, argument):
        return cls(argument, now=ctx.message.created_at)


def human_timedelta(dt, *, source=None, accuracy=3, brief=False, suffix=True):
    now = source or datetime.datetime.now(datetime.timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)

    if now.tzinfo is None:
        now = now.replace(tzinfo=datetime.timezone.utc)

    # Microsecond free zone
    now = now.replace(microsecond=0)
    dt = dt.replace(microsecond=0)

    # This implementation uses relativedelta instead of the much more obvious
    # divmod approach with seconds because the seconds approach is not entirely
    # accurate once you go over 1 week in terms of accuracy since you have to
    # hardcode a month as 30 or 31 days.
    # A query like "11 months" can be interpreted as "!1 months and 6 days"
    if dt > now:
        delta = relativedelta(dt, now)
        suffix = ''
    else:
        delta = relativedelta(now, dt)
        suffix = ' ago' if suffix else ''

    attrs = [
        ('year', 'y'),
        ('month', 'mo'),
        ('day', 'd'),
        ('hour', 'h'),
        ('minute', 'm'),
        ('second', 's'),
    ]

    output = []
    for attr, brief_attr in attrs:
        elem = getattr(delta, attr + 's')
        if not elem:
            continue

        if attr == 'day':
            weeks = delta.weeks
            if weeks:
                elem -= weeks * 7
                if not brief:
                    output.append(format(plural(weeks), 'week'))
                else:
                    output.append(f'{weeks}w')

        if elem <= 0:
            continue

        if brief:
            output.append(f'{elem}{brief_attr}')
        else:
            output.append(format(plural(elem), attr))

    if accuracy is not None:
        output = output[:accuracy]

    if len(output) == 0:
        return 'now'
    else:
        if not brief:
            return human_join(output, final='and') + suffix
        else:
            return ' '.join(output) + suffix

@fill_with_flags()
class LoggingEventsFlags(BaseFlags):

    def __init__(self, permissions: int = 0, **kwargs: bool):
        super().__init__(**kwargs)
        if not isinstance(permissions, int):
            raise TypeError(f"Expected int parameter, received {permissions.__class__.__name__} instead.")
        self.value = permissions
        for key, value in kwargs.items():
            if key not in self.VALID_FLAGS:
                raise TypeError(f"{key!r} is not a valid permission name.")
            setattr(self, key, value)

    @classmethod
    def all(cls):
        bits = max(cls.VALID_FLAGS.values()).bit_length()
        value = (1 << bits) - 1
        self = cls.__new__(cls)
        self.value = value
        return self

    @classmethod
    def message(cls):
        return cls(0b000000000000000000000000000111)

    @classmethod
    def join_leave(cls):
        return cls(0b000000000000000000011000011000)

    @classmethod
    def member(cls):
        return cls(0b000000000000000000000111100000)

    @classmethod
    def voice(cls):
        return cls(0b000000110000000111100000000000)

    @classmethod
    def server(cls):
        return cls(0b111111111111111000000000000000)

    @flag_value
    def message_delete(self):
        return 1 << 0

    @flag_value
    def message_purge(self):
        return 1 << 1

    @flag_value
    def message_edit(self):
        return 1 << 2

    @flag_value
    def member_join(self):
        return 1 << 3

    @flag_value
    def member_leave(self):
        return 1 << 4

    @flag_value
    def member_update(self):
        return 1 << 5

    @flag_value
    def user_ban(self):
        return 1 << 6

    @flag_value
    def user_unban(self):
        return 1 << 7

    @flag_value
    def user_update(self):
        return 1 << 8

    @flag_value
    def invite_create(self):
        return 1 << 9

    @flag_value
    def invite_delete(self):
        return 1 << 10

    @flag_value
    def voice_join(self):
        return 1 << 11

    @flag_value
    def voice_leave(self):
        return 1 << 12

    @flag_value
    def voice_move(self):
        return 1 << 13

    @flag_value
    def voice_mod(self):
        return 1 << 14

    @flag_value
    def emoji_create(self):
        return 1 << 15

    @flag_value
    def emoji_delete(self):
        return 1 << 16

    @flag_value
    def emoji_update(self):
        return 1 << 17

    @flag_value
    def sticker_create(self):
        return 1 << 18

    @flag_value
    def sticker_delete(self):
        return 1 << 19

    @flag_value
    def sticker_update(self):
        return 1 << 20

    @flag_value
    def server_update(self):
        return 1 << 21

    @flag_value
    def stage_open(self):
        return 1 << 22

    @flag_value
    def stage_close(self):
        return 1 << 23

    @flag_value
    def channel_create(self):
        return 1 << 24

    @flag_value
    def channel_delete(self):
        return 1 << 25

    @flag_value
    def channel_edit(self):
        return 1 << 26

    @flag_value
    def role_create(self):
        return 1 << 27

    @flag_value
    def role_delete(self):
        return 1 << 28

    @flag_value
    def role_edit(self):
        return 1 << 29