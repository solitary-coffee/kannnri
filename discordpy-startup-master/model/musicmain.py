#!/usr/bin/env python3
from discord.ext import commands

import music

import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_cog(music.Music(self.bot))

def setup(bot):
    return bot.add_cog(Greetings(bot))




