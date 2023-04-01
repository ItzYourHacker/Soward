
from discord.ext.commands import Converter, Context, BadArgument


class InvalidAddRemoveArgument(BadArgument):
    pass


class InvalidTimeZone(BadArgument):
    pass


class InvalidCategory(BadArgument):
    def __init__(self, category: str):
        self.category = category


class ImportantCategory(BadArgument):
    def __init__(self, category: str):
        self.category = category


class AddRemoveConverter(Converter):
    async def convert(self, ctx: Context, argument: str):
        if argument.lower() in ['add']:
            return True
        elif argument.lower() in ['remove']:
            return False
        else:
            raise InvalidAddRemoveArgument(argument)


class Lower(Converter):
    async def convert(self, ctx: Context, argument: str):
        return argument.lower()


class Category(Converter):
    async def convert(self, ctx: Context, argument: str):
        categories: list = [cog for cog in ctx.bot.cogs if cog.lower() == cog and len(ctx.bot.get_cog(cog).get_commands()) != 0]
        imp_categories = ['config', 'user']
        if argument.lower() in imp_categories:
            raise ImportantCategory(argument)
        elif argument.lower() in categories:
            return ctx.bot.get_cog(argument.lower())
        else:
            raise InvalidCategory(argument)


        