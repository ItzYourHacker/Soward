import discord
from discord.ext import commands
import json
from utilities.Tools import*
badgesgiver = [980361546918162482,925246550018519040,940973004647718912,971301161678290964,969991261048164352,1018139793789563000,984815117730480228,990643162928279592]

class badge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(aliases=["addb"])
    async def addbadge(self, ctx, user: discord.Member, *, badge):
            if ctx.author.id in badgesgiver:
                    with open("badges.json", "r") as f:
                            idk = json.load(f)
                            if str(user.id) not in idk:
                                    idk[str(user.id)] = []
                                    idk[str(user.id)].append(f"{badge}")
                                    await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",  color=0xFF1B1B))
                            elif str(user.id) in idk:
                                    idk[str(user.id)].append(f"{badge}")
                                    await ctx.reply(embed=discord.Embed(title=f" Added badge {badge} to {user}.",color=0xFF1B1B))
                                    with open("badges.json", "w") as f:
                                            json.dump(idk, f, indent=4)


    @commands.command(aliases=["profile"])
    @blacklist_check()
    async def badges(self,ctx, user: discord.Member=None):
            user = user or ctx.author
            with open("badges.json", "r") as f:
                    idk = json.load(f)
                    if str(user.id) not in idk:
                            await ctx.reply(embed=discord.Embed(description=f"{user} Have no badges join [support server](https://discord.gg/k6YNHy36JJ) to get some badges.",color=0xFF1B1B), mention_author=False)
                            return
                    elif str(user.id) in idk:
                            embed = discord.Embed(color=discord.Colour(0xFF1B1B),title="<a:hypesquad:1017430505353904128> Soward Achivement <a:hypesquad:1017430505353904128> ",description=f"{user.mention} badges\n\n")
                            for bd in idk[str(user.id)]:
                                    embed.description += f"{bd}\n"
                                    embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
                                    embed.set_thumbnail(url=user.display_avatar.url)
                                    await ctx.send(embed=embed)
       
    @commands.command(aliases=['rb'])
    async def removebadge(self, ctx, user: discord.User = None):
            if ctx.author.id in badgesgiver:
                    if user is None:
                            await ctx.reply(embed=discord.Embed(title="You must specify a user to remove badge.", color=0xFF1B1B))
                            return
                            with open('badges.json', 'r') as f:
                                    badges = json.load(f)
                            try:
                                    if str(user.id) in badges:
                                            badges.remove(str(user.id))
                                            with open('badges.json', 'w') as f:
                                                    json.dump(badges, f, indent=4)
                                                    await ctx.reply(embed=discord.Embed(title=f"Removed badge of {user}", color=0xFF1B1B))
                            except KeyError:
                                    await ctx.reply("This user has no badge.")

def setup(bot):
    bot.add_cog(badge(bot))