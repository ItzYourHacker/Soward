import discord
import datetime

class ErrorEmbed:
  def error(title, reason):
    embed = discord.Embed(
      title = "<:icons_Wrong:1009926430127308881> " + title,
      description = reason,
      color = discord.Color.red(),
      timestamp = datetime.datetime.utcnow()
    )
    embed.set_author(name ="Error")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/812759024545169438/848318551446126603/fail.png")
    return embed