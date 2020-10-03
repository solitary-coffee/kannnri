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
@bot.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    if message.content.startswith('!trans'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            befor_lang = detact.lang
            if befor_lang == 'ja':
                convert_string = translator.translate(str, src=befor_lang, dest='en')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = translator.translate(str, src=befor_lang, dest='ja')
                embed = discord.Embed(title='変換結果', color=0xff0000)
                embed.add_field(name='Befor', value=str)
                embed.add_field(name='After', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=befor_lang, dest=after_lang)
            embed = discord.Embed(title='変換結果', color=0xff0000)
            embed.add_field(name='Befor', value=str)
            embed.add_field(name='After', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。'
        await message.channel.send(m)
    if message.guild.id not in buno.gila:      
        for word in rog.list:
            if message.author.bot:
                return
            if word in message.content:
                await message.delete()
                embed=discord.Embed(title="現在のコメントは削除されました",description=message.author.mention, color=0xdc0909)
                embed.add_field(name="削除されたコメント(部分):", value= word, inline=True)
                embed.add_field(name="理由：", value="現在のコメントは暴言にあたります", inline=True)
                embed.add_field(name="削除されたコメント(全文):", value= message.content, inline=False)  
                embed.add_field(name="違反したサーバー", value= message.guild, inline=True)
                embed.add_field(name="違反したチャンネル", value= message.channel, inline=True)
                embed.add_field(name="その他", value="意図しないで削除された場合は孤独のコーヒーまでお願いします", inline=False)
                embed.add_field(name="違反した時間（UTC時間です日本時間は+９時間", value= message.created_at, inline=True)
                                                      

                await message.channel.send(embed=embed)  


    await bot.process_commands(message)

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
