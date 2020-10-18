import discord
from discord import embeds
from discord.ext import commands
from googletrans import Translator
from deta import rog
from deta import goban
from deta import buno
import sys
import traceback
import logging
translator = Translator()

import textwrap

bot = commands.Bot(command_prefix='.')
import asyncio
import datetime
dt_now = datetime.datetime.now()

import logging

# ログレベルを DEBUG に変更
logging.basicConfig(filename='discord.log', level=logging.DEBUG)
formatter = '%(levelname)s : %(asctime)s : %(message)s'

# ログレベルを DEBUG に変更
logging.basicConfig(level=logging.DEBUG, format=formatter)

# 従来の出力
logging.info('error{}'.format('outputting error'))
logging.info('warning %s %s' % ('was', 'outputted'))
# logging のみの書き方
logging.info('info %s %s', 'test', 'test')

async  def err(ctx):
    ch = 766939626874994688
    e = discord.Embed(title=f"機能ログ:{ctx.author.name} \n`{textwrap.shorten(ctx.message.content, width=512)}` ", description=f"　{ctx.guild}/{ctx.channel}　\n{dt_now.strftime('%Y-%m-%d %H:%M')}", color=0xf00)
    await bot.get_channel(ch).send(embed=e)

@bot.event
async def on_ready():
    ch = 766939585951170560
    e = discord.Embed(title="起動ログ", description=f"{dt_now.strftime('%Y-%m-%d %H:%M')}", color=0xf00)
    await bot.get_channel(ch).send(embed=e)
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
    j =  ctx.author.name
    await err(ctx)
@bot.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    ch = 764771338552082474


    
   

    e = discord.Embed(title='エラー', colour=0xcc3366)
    e.add_field(name='実行者', value=ctx.author.name)
    e.add_field(name='タグ・ID', value=f'{ctx.author} (ID: {ctx.author.id})')

    fmt = f'チャンネル: {ctx.channel} (ID: {ctx.channel.id})'
    if ctx.guild:
        fmt = f'{fmt}\nサーバー: {ctx.guild} (ID: {ctx.guild.id})'

    e.add_field(name='実行場', value=fmt, inline=False)
    e.add_field(name='実行コマンド', value=f"`{textwrap.shorten(ctx.message.content, width=512)}`",inline=False)

    exc = ''.join(
        traceback.format_exception(type(error), error, error.__traceback__, chain=False))
    e.description = f'```py\n{exc}\n```'
    e.add_field(name='discord.py ver', value=discord.__version__)
    e.add_field(name='python ver', value=sys.version)
    e.timestamp = datetime.datetime.utcnow()
    m = await bot.get_channel(ch).send(embed=e)
    embed = discord.Embed(title="エラー", description="", color=0xf00)
    embed.add_field(name="申し訳ございません　エラーが発生しました", value=f"このエラーについて問い合わせるときは `/dm` またはサーバーでお願いします　\n(開発者からBOT を通じて連絡する場合がございます) \n またこのコードも一緒にお知らせください：{m.id} \n \n [公式サーバー](https://discord.gg/GWrvMT4)", inline=False)

    await ctx.send(embed=embed)



bot.run(os.environ['TOKEN'])
