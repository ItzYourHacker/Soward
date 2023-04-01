import discord
DEFAULT_COLOR = 0xFF1B1B

def clean_code(content):
    if content.startswith('```') and content.endswith('```'):
        return "\n".join(content.split("\n")[1:][:-3])
    else:
        return content

class Pag():
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass