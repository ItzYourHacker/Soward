import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb


class welcome_event(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://PRINCE123:nxtontop@cluster0.wr5qth2.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.connection["Rbot"]["servers"]

    @commands.Cog.listener()
    async def on_member_join(self, user):
        try:
            guild = user.guild
            data = await self.db.find_one({"guild": guild.id})

            if data["welcome"]["enabled"] != True:
                return            
            if data["welcome"]["channel"] == None:
                return
            if data['welcome']["embed"] != True: 

              if data["welcome"]["message"] == None:
                return
              else: 

                channel = self.client.get_channel(data["welcome"]["channel"])
                message = data["welcome"]["message"]
                if "{user.id}" in message:
                    message = message.replace("{user.id}", "%s" % (user.id))

                if "{user.mention}" in message:
                  message = message.replace("{user.mention}", "%s" % (user.mention))

                if "{user.tag}" in message:
                  message = message.replace("{user.tag}", "%s" % (user.discriminator))

                if "{user.name}" in message:
                  message = message.replace("{user.name}", "%s" % (user.name))
                
                if "{user.avatar}" in message:
                  message = message.replace("{user.avatar}", "%s" % (user.avatar_url))

                if "{server.name}" in message:
                  message = message.replace("{server.name}", "%s" % (user.guild.name))
                
                if "{server.membercount}" in message:
                  message = message.replace("{server.membercount}", "%s" % (user.guild.member_count))
                
                if "{server.icon}" in message:
                  message = message.replace("{server.icon}", "%s" % (user.guild.icon_url))

                await channel.send(message)

            else:
              channel = self.client.get_channel(data["welcome"]["channel"])
              message = data["welcome"]["description"]
              message1 = data["welcome"]["title"]
              thumbnail = data["welcome"]["thumbnail"]
              image = data["welcome"]["image"] 
              message2 = data['welcome']['footer']
              
              if "{user.id}" in message:
                message = message.replace("{user.id}", "%s" % (user.id))

              if "{user.mention}" in message:
                message = message.replace("{user.mention}", "%s" % (user.mention))

              if "{user.tag}" in message:
                message = message.replace("{user.tag}", "%s" % (user.discriminator))

              if "{user.name}" in message:
                message = message.replace("{user.name}", "%s" % (user.name))
                
              if "{user.avatar}" in message:
                message = message.replace("{user.avatar}", "%s" % (user.avatar_url))

              if "{server.name}" in message:
                message = message.replace("{server.name}", "%s" % (user.guild.name))
                
              if "{server.membercount}" in message:
                message = message.replace("{server.membercount}", "%s" % (user.guild.member_count))
                
              if "{server.icon}" in message:
                message = message.replace("{server.icon}", "%s" % (user.guild.icon_url))

              if "{user.id}" in message1:
                    message1 = message1.replace("{user.id}", "%s" % (user.id))

              if "{user.mention}" in message1:
                message1 = message1.replace("{user.mention}", "%s" % (user.mention))

              if "{user.tag}" in message1:
                message1 = message1.replace("{user.tag}", "%s" % (user.discriminator))

              if "{user.name}" in message1:
                message1 = message1.replace("{user.name}", "%s" % (user.name))
                
              if "{user.avatar}" in message1:
                message1 = message1.replace("{user.avatar}", "%s" % (user.avatar_url))

              if "{server.name}" in message1:
                message1 = message1.replace("{server.name}", "%s" % (user.guild.name))
                
              if "{server.membercount}" in message1:
                message1 = message1.replace("{server.membercount}", "%s" % (user.guild.member_count))
                
              if "{server.icon}" in message1:
                message1 = message1.replace("{server.icon}", "%s" % (user.guild.icon_url))

              if "{user.id}" in message2:
                    message2 = message2.replace("{user.id}", "%s" % (user.id))

              if "{user.mention}" in message2:
                message2 = message2.replace("{user.mention}", "%s" % (user.mention))

              if "{user.tag}" in message2:
                message2 = message2.replace("{user.tag}", "%s" % (user.discriminator))

              if "{user.name}" in message2:
                message2 = message2.replace("{user.name}", "%s" % (user.name))
                

              if "{server.name}" in message2:
                message2 = message2.replace("{server.name}", "%s" % (user.guild.name))
                
              if "{server.membercount}" in message2:
                message2 = message2.replace("{server.membercount}", "%s" % (user.guild.member_count))
                
              await channel.send(f"{user.mention}")


              embed = discord.Embed(title=f"{message1}",description=f"{message}", color=0xFF1B1B)  
              embed.set_thumbnail(url=f"{thumbnail}")
              embed.set_image(url=f"{image}")
              embed.set_footer(text=f"{message2}")

              await channel.send(F"{user.mention}", embed=embed)
              
          
        except Exception:
            pass

def setup(client):
    client.add_cog(welcome_event(client))