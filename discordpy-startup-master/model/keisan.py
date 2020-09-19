import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def t(self,ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def h(self,ctx, a: int, b: int):
        await ctx.send(a-b)


    @commands.command()
    async def k(self,ctx, a: int, b: int):
        await ctx.send(a*b)



    @commands.command()
    async def w(self,ctx, a: int, b: int):
        await ctx.send(a/b)


def setup(bot):
    return bot.add_cog(Greetings(bot))