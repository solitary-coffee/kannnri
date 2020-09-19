import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def neko(self,ctx):
        await ctx.send("にゃーん")

def setup(bot):
    return bot.add_cog(Greetings(bot))