import discord
from discord.ext import commands
from googletrans import Translator
from deta import rog
from deta import goban
from deta import buno
translator = Translator()
import os

bot = commands.Bot(command_prefix="/")
import asyncio
import datetime

dt_now = datetime.datetime.now()
@bot.event
async def on_ready():
    while True:

        await bot.change_presence(activity=discord.Game(name="herokuで稼働中"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name=f"起動時間:{dt_now.strftime('%Y-%m-%d %H:%M')}"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="ヘルプ表示/he"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="グローバルチャンネル名をcoffee-global"))
        await asyncio.sleep(15)


bot.load_extension("model.sub")
bot.load_extension("model.dm")
bot.load_extension("model.kanri")
bot.load_extension("model.ch")
bot.load_extension("model.info")
bot.load_extension("model.special")
bot.load_extension("model.game")
bot.load_extension("model.other")
bot.load_extension("model.musicmain")
bot.load_extension("model.help")
bot.load_extension("model.keisan")
bot.load_extension("model.goch")

@bot.command()
async def rito(ctx):    
    bot.reload_extension("model.sub")
    await ctx.send("サブ機能が正常に再起動しました")
    bot.reload_extension("model.dm")
    await ctx.send("dm機能が正常に再起動しました")
    bot.reload_extension("model.kanri")
    await ctx.send("管理者機能が正常に再起動しました")
    bot.reload_extension("model.ch")
    await ctx.send("チャンネル機能が正常に再起動しました")    
    bot.reload_extension("model.info")
    await ctx.send("情報機能が正常に再起動しました")
    bot.reload_extension("model.special")
    await ctx.send("専用機能が正常に再起動しました")
    bot.reload_extension("model.game")
    await ctx.send("ゲーム機能が正常に再起動しました")
    bot.reload_extension("model.other")
    await ctx.send("その他機能が正常に再起動しました")
    bot.reload_extension("model.musicmain")
    await ctx.send("音楽機能が正常に再起動しました")
    bot.reload_extension("model.help")
    await ctx.send("ヘルプ機能が正常に再起動しました")
    bot.reload_extension("model.keisan")
    await ctx.send("計算機能が正常に再起動しました")
    bot.reload_extension("model.goch")
    await ctx.send("グローバルチャット機能が正常に再起動しました")
    await ctx.send("すべての機能が正常に再起動しました")


bot.run(os.environ['TOKEN'])
