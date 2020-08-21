import discord
from discord.ext import commands
import typing
import random
import time
import abc
import rog
import psutil
import matplotlib.pyplot as plt
import asyncio
import youtube_dl
import ffmpeg
from apiclient.discovery import build
import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
import base64
import json
import os
import subprocess
import asyncio
import itertools
import sys
from async_timeout import timeout
from functools import partial
import asyncio
import itertools
import traceback
from youtube_dl.utils import lookup_unit_table
import random
import playlist

client = discord.Client()
bot = commands.Bot(command_prefix='/')

ID = 637850681666961408

kai = {
    "白米":1,
    "焼鮭とカボス":2, 
    "ホットドック":4,
    "サーロインステーキ":14,
    "高級海鮮コース":400,
    "板チョコ":1,
    "ショートケーキ":3,
    "ハンバーガー":2
}


@bot.event
async def on_ready():
    bot.session = aiohttp.ClientSession(loop=bot.loop)
    while True:

        await bot.change_presence(activity=discord.Game(name="herokuで稼働中"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="更新時間：2020/8/6/21:30"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="ヘルプ表示/help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="更新内容　/ku"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(name="音楽機能を大量に追加しました　詳細は/muhe"))
        await asyncio.sleep(15)
   


@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def dm(ctx, *, naiyou):
    dm = bot.get_user(ID)
    embed=discord.Embed(title= "メッセージを受信",description= "サーバからです" , color=0x3498db)
    embed.add_field(name= ctx.message.channel , value=  ctx.message.guild.name, inline=False)
    embed.add_field(name= ctx.message.author.name, value= naiyou, inline=False)


    await dm.send(embed=embed)
    await ctx.message.delete()
                                     
@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()
        await ctx.send('現在クールタイム中です %.2f秒後にもう一度やり直してください' % error.retry_after)


@bot.event
async def on_message(message):  
    if message.channel.id == 719307017331802173:
        print("ok")
    elif message.channel.id == 713588195555541033:
        print("ok")
    elif message.channel.id == 721837476666409010:
        print("ok")
    else:       
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

@bot.command()
async def kt(ctx, *,kasutamu):
    if ctx.message.author.id == ID:    
        await bot.change_presence(activity=discord.Game(name=kasutamu))
    else:
        await ctx.send("このコマンドは管理者専用です")

        
@bot.command(name='eval')
async def _eval(ctx, *, body):
    if ctx.message.author.id == ID:    
        blocked_words = ['.delete()', 'os', 'subprocess', 'history()', '("token")', "('token')",
                        'aW1wb3J0IG9zCnJldHVybiBvcy5lbnZpcm9uLmdldCgndG9rZW4nKQ==', 'aW1wb3J0IG9zCnByaW50KG9zLmVudmlyb24uZ2V0KCd0b2tlbicpKQ==']
        if ctx.author.id != bot.owner_id:
            for x in blocked_words:
                if x in body:
                    return await ctx.send('Your code contains certain blocked words.')
        env = {
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'source': inspect.getsource,
            'session':bot.session
        }

        env.update(globals())

        body = cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        def paginate(text: str):
            '''Simple generator that paginates text.'''
            last = 0
            pages = []
            for curr in range(0, len(text)):
                if curr % 1980 == 0:
                    pages.append(text[last:curr])
                    last = curr
                    appd_index = curr
            if appd_index != len(text)-1:
                pages.append(text[last:curr])
            return list(filter(lambda a: a != '', pages))
    
        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await ctx.message.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                    
                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                bot._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await ctx.message.add_reaction('\u2705')  # tick
        elif err:
            await ctx.message.add_reaction('\u2049')  # x
        else:
            await ctx.message.add_reaction('\u2705')
    else: 
        await ctx.send("管理者のみ利用可能")
        
def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')

def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

@bot.command()
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping1 = round((time_2-time_1)*1000)
    time_3 = time.perf_counter()
    await ctx.trigger_typing()
    time_4 = time.perf_counter()
    ping2 = round((time_4-time_3)*1000)
    time_5 = time.perf_counter()
    await ctx.trigger_typing()
    time_6 = time.perf_counter()
    ping3 = round((time_6-time_5)*1000)
       
    tt  = ping1 + ping2 + ping3
    tt1 = tt/3
    keka    = (round(tt1, 2))
    embed=discord.Embed(title= "ping確認",description= "測定結果", color=0xdc0909)
    embed.add_field(name="1回目は:" , value=f"{ping1} ", inline=False)
    embed.add_field(name="2回目は:" , value=f"{ping2} ", inline=False)
    embed.add_field(name="3回目は:" , value=f"{ping3} ", inline=False)
    embed.add_field(name="平均:" , value=keka , inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def tm(ctx, tm):
    if ctx.message.channel.id == 738407992281530411:
        dm = bot.get_user(716754062879490111)
        for word in kai:
            if word in ctx.message.content:
                await ctx.send(f"{tm}を購入しました　代金は{kai[tm]}$")
        embed=discord.Embed(title= f"{ctx.message.author.name}が購入しました",description= "サーバからです" , color=0x3498db)
        embed.add_field(name= f"買ったもの：{tm}" , value=  f"代金：{list[tm]}", inline=False)
        await dm.send(embed=embed)
    else:
        await ctx.send("ここで使えません")
    
@bot.command()
async def kn(ctx):
    embed=discord.Embed(title="内容更新",description= "8月6日更新", color=0xdc0909)
    embed.add_field(name= "追加したプログラム等", value= "リピート・シャッフル機能", inline=False)
    embed.add_field(name= "削除したプログラム等", value= "None", inline=False)
    embed.add_field(name= "修正したプログラム等", value= "None", inline=False)
    await ctx.send(embed=embed)


class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command()
async def r(ctx, *, member: MemberRoles ):
    """Tells you a member's roles."""
    await ctx.send('ロール: ' + ', '.join(member))

@bot.command()
async def t(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def h(ctx, a: int, b: int):
    await ctx.send(a-b)


@bot.command()
async def k(ctx, a: int, b: int):
    await ctx.send(a*b)



@bot.command()
async def w(ctx, a: int, b: int):
    await ctx.send(a/b)


@bot.command()
async def ke(ctx,*,ss):
    await ctx.message.delete()
    await ctx.send(ss)  



@bot.command()
async def j(ctx, *, member: discord.Member):
    await ctx.send('{0} 入室履歴: {0.joined_at}' .format(member))



@bot.command()
async def d(ctx):
    await ctx.send("ダイスをスタートします最初に1000渡します")   

    num_random = random.randrange(-1000,+1000)
    m = int(num_random)
    if 1000> m> 0:
        time.sleep(2)
        await ctx.send(m)
        await ctx.send(m+1000)

        await ctx.send('やりましたね～～さぁ次も・・・')
        await ctx.send('再び実行する際は/dをお願いします')

        
    else:
        time.sleep(2)
        await ctx.send(m)
        await ctx.send(m-1000)

        await ctx.send('うーーん次がありますよ')
        await ctx.send('再び実行する際は/dをお願いします')

#さいしょに1000渡してそれを定義そこから1000-ｍでとれるかも・・・・/dしたら1000渡してスタートawaitで1000-ｍでおｋ・・・？

@bot.command()
async def em(ctx, a, b, c, d):
    embed=discord.Embed(title= a,description= b, color=0xdc0909)
    embed.add_field(name= c, value= d, inline=True)
    await ctx.send(embed=embed)


        

@bot.command()
async def ritu(ctx):
    total = psutil.virtual_memory().total/1000/1000/1000
    use = psutil.virtual_memory().used/1000/1000/1000
    kekka = round(use/total*100, 0)
    content = int(kekka/5)
    cpu = psutil.cpu_percent(interval=1)
    content2 = int(cpu/5)        
    memorymeter = ("|" * content) + (" " * (20-content))
    cpumeter = ("|" * content2) + (" " * (20-content2))
    embed = discord.Embed(
        title="CPU/メモリ情報",
        description=(
            f"メモリ使用量：{round(use, 1)}GB\n"
            f"メモリ搭載量：{round(total, 1)}GB\n"
            f"メモリ使用率{kekka}%\n"
            f"`[{memorymeter}`]\n"
            f"CPU：{cpu}%\n"
            f"`[{cpumeter}]`"),
        color=0xff0000)
    await ctx.send(embed=embed)      


async def create_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

# 発言時に実行されるイベントハンドラを定義

@bot.command()
async def newch(ctx,ss):
    if ctx.message.author.guild_permissions.administrator:
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(ctx, channel_name=ss)

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await ctx.send(text)
    elif ctx.message.author.id == ID:    
        new_channel = await create_channel(ctx, channel_name=ss)

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await ctx.send(text)

    else:
        await ctx.send('このコマンドはサーバー管理者のみ使えます')

 

@bot.command()
async def delch(ctx,channel:discord.TextChannel):
    if ctx.message.author.id == ID:    
        text = f'{channel.mention} を削除しました'
        await ctx.send(text)
        await channel.delete()

    elif ctx.message.author.guild_permissions.administrator:    
        text = f'{channel.mention} を削除しました'
        await ctx.send(text)
        await channel.delete()        
    else:
        await ctx.send("このコマンドは管理者専用です")
api_key = 'AIzaSyCyMz5iWCEX0vvUabjYld1i3kjV2i9wS3Y'

def get_videos_search(keyword):
    youtube = build('youtube', 'v3', developerKey=api_key)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
    youtube_res = youtube_query.execute()
    return youtube_res.get('items', [])

@bot.command()
async def se(ctx,*,ss):
    result = get_videos_search(ss)
    for item in result:
        if item['id']['kind'] == 'youtube#video':
            embed=discord.Embed(title= "youtube検索結果",description= f"{ss}で検索しました", color=0xdc0909)
            embed.add_field(name=item['snippet']['title'] , value= 'https://www.youtube.com/watch?v=' + item['id']['videoId'], inline=True)
            await ctx.send(embed=embed)

@bot.command()
async def he(ctx):
    embed=discord.Embed(title=" 管理BOTのヘルプ[1]です",description= "基本コマンドの説明", color=0xdc0909)
    embed.add_field(name= "```/he```", value= "これです", inline=False)
    embed.add_field(name= "```/r [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDについているロールを表示します", inline=False)
    embed.add_field(name= "```/j [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDがこのサーバーに入室した日時を表示します", inline=False)
    embed.add_field(name= "```/em [タイトル] [サブタイトル]　[コメント1] [コメント2]```", value= "埋め込みで表示されます", inline=False)
    embed.add_field(name= "```/d```", value= "ダイスです暇なときどうぞ", inline=False)
 
    embed.add_field(name= "```/k [足される数] [足す数]```", value= "足し算ができます", inline=False)
    embed.add_field(name= "```/h [引かれる数] [引く数]```", value= "引き算ができます", inline=False)
    embed.add_field(name= "```/k [掛ける数] [掛けられる数]```", value= "掛け算ができます", inline=False)
    embed.add_field(name= "```/w [割られる数] [割る数]```", value= "割り算ができます", inline=False)
    embed.add_field(name= "```/ritu```", value= "このＢＯＴを動かしている情報がみられます重いと感じた場合にお使いください", inline=False)
    embed.add_field(name= "```/ping```", value= "応答時間が見られます重いと感じた場合にお使いください", inline=False)
    embed.add_field(name= "```/dm [送る言葉]```", value= "BOT開発者にDMを送ることができます（常識は守るように", inline=False)
    embed.add_field(name= "```/newch [チャンネル名]```", value= "サーバー管理者のみ利用可能　新しくチャンネルを作ることができます", inline=False)
    embed.add_field(name= "```/delch [チャンネル名]```", value= "サーバー管理者のみ利用可能　チャンネルを削除できます", inline=False)
    embed.add_field(name= "その他情報", value= "``` ```", inline=False)
    embed.add_field(name= "**音楽機能**", value= "別枠です　コマンド　/muhe", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def muhe(ctx):
    embed=discord.Embed(title=" 管理BOTのヘルプ[2]です",description= "音楽コマンドの説明", color=0xdc0909)
    embed.add_field(name= "```/play [URL・キーワード]```", value= "　youtubeから再生します \n　キーワードは検索し一番上のを再生します", inline=False)
    embed.add_field(name= "```/pause```", value= "一時停止します", inline=False)
    embed.add_field(name= "```/resume```", value= "一時停止から再生します", inline=False)
    embed.add_field(name= "```/skip```", value= "リストに入ってる次の曲を流します", inline=False)
    embed.add_field(name= "```/q```", value= "リストです", inline=False)
    embed.add_field(name= "```/np```", value= "再生している曲名・再生者を表示します", inline=False)
    embed.add_field(name= "```/vol```", value= "音量を調節できます（上げすぎると音割れします）", inline=False)
    embed.add_field(name= "```/stop```", value= "止まります＆BOTが抜けます", inline=False)
    embed.add_field(name= "```/loop```", value= "コマンドを実行した現在のリストをリピートします ", inline=False)
    embed.add_field(name= "```/loopend```", value= "リピートを終了します", inline=False)    
    embed.add_field(name= "```/mix```", value= "シャッフルします（playlistはしません）", inline=False)
    embed.add_field(name= "```/se [キーワード]```", value= "５曲　検索します", inline=False)
   
    await ctx.send(embed=embed)
loopka = 0


ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}
  # ipv6 addresses cause issues sometimes


ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        print("６7")
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        print("DL1")
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        await ctx.send(f'```ini\n[ {data["title"]}がリストに入りました.]\n```', delete_after=10)
        

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)
        
        print("DL１終わり")
     

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        print("ｄｌ2")
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)
        print("ｄｌ2終わり")
   


class MusicPlayer:
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current', 'np', 'volume','update','updating')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue =  asyncio.Queue()
        self.next = asyncio.Event()

        self.np = None  # Now playing message
        self.volume : bool= .5
        self.update: bool = False
        self.updating: bool = False
        self.current = False



    
    
    
 
        
        
        print("設定")
        ctx.bot.loop.create_task(self.player_loop())
    @property
    def entries(self) -> None:
        print("ループ設定")
        return list(self.queue._queue)  # type: ignore  # false-positive
        

    async def player_loop(self):
        """Our main player loop."""
        print("再生始まり")
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            print("再生途中")
            
            
                
            
            self.next.clear()
            
            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    source = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)

            
            
            source.volume  = self.volume 
            self.current = source

            self._guild.voice_client.play(source , after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            self.np = await self._channel.send(f'再生：  `{source.title}` \n 再生者： '
                                               f'`{source.requester}`', delete_after=10)
           
            await self.next.wait()
    
                

            # Make sure the FFmpeg process is cleaned up.
            


            
                # We are no longer playing this song...
            try:
                pass   
            except discord.HTTPException:
                pass

    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))
        


class Music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self.players = {}


    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass
    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage
        return True

    async def __error(self, ctx, error):
        """A local error handler for all errors arising from commands in this cog."""
        if isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.send('This command can not be used in Private Messages.')
            except discord.HTTPException:
                pass
        elif isinstance(error, InvalidVoiceChannel):
            await ctx.send('Error connecting to Voice Channel. '
                           'Please make sure you are in a valid channel or provide me with one')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = MusicPlayer(ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        """Connect to voice.
        Parameters
        ------------
        channel: discord.VoiceChannel [Optional]
            The channel to connect to. If a channel is not specified, an attempt to join the voice channel you are in
            will be made.
        This command also handles moving the bot to different channels.
        """
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise InvalidVoiceChannel('No channel to join. Please either specify a valid channel or join one.')

        vc = ctx.voice_client

        if vc:
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Moving to channel: <{channel}> timed out.')
        else:
            try:
                await channel.connect()
            except asyncio.TimeoutError:
                raise VoiceConnectionError(f'Connecting to channel: <{channel}> timed out.')

        await ctx.send(f'再生するボイスチャット: **{channel}**')

    @commands.command(name='play', aliases=['sing'])
    async def play_(self, ctx, *, search:str):
        """Request a song and add it to the queue.
        This command attempts to join a valid voice channel if the bot is not already in one.
        Uses YTDL to automatically search and retrieve a song.
        Parameters
        ------------
        search: str [Required]
            The song to search and retrieve using YTDL. This could be a simple search, an ID or URL.
        """
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)

        # If download is False, source will be a dict which will be used later to regather the stream.
        # If download is True, source will be a discord.FFmpegPCMAudio with a VolumeTransformer.
        source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)

        await player.queue.put(source)

    @commands.command(name='pause')
    async def pause_(self, ctx):
        """Pause the currently playing song."""
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'一時停止：\n {ctx.author}')

    @commands.command(name='resume')
    async def resume_(self, ctx):
        """Resume the currently paused song."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am n')
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'一時停止したところからスタートします：{ctx.author}')

    @commands.command(name='skip')
    async def skip_(self, ctx):
        """Skip the song."""
        vc = ctx.voice_client
       


        if not vc or not vc.is_connected():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.send(f'スキップ：{ctx.author}')

    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx):
        """Retrieve a basic queue of upcoming songs."""
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)

        player = self.get_player(ctx)
        if player.queue.empty():
            return await ctx.send('曲リストには何もはいってません', delete_after=20)

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(player.queue._queue, 0, 30)) 

        fmt = '\n'.join(f'**`{_["title"]}`**\n URL: {_["web_url"]} ' for _ in upcoming)
        embed = discord.Embed(title=f'リスト -  {len(upcoming)}曲', description=fmt)

        await ctx.send(embed=embed)

    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        """Display information about the currently playing song."""
        print("情報")
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)

        player = self.get_player(ctx)
        if not player.current:
            return await ctx.send('曲が入っていません', delete_after=20)

        try:
            # Remove our previous now_playing message.
            await player.np.delete()
        except discord.HTTPException:
            pass

        player.np = await ctx.send(f'再生: `{vc.source.title}`\n '
                                   f'再生者： `{vc.source.requester}`')

    @commands.command(name='volume', aliases=['vol'])
    async def change_volume(self, ctx, *, vol: float):
        """Change the player volume.
        Parameters
        ------------
        volume: float or int [Required]
            The volume to set the player to in percentage. This must be between 1 and 100.
        """
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)

        if not 0 < vol < 101:
            return await ctx.send('音量は100以内です', delete_after=20)

        player = self.get_player(ctx)

        if vc.source:
            vc.source.volume = vol / 100

        player.volume = vol / 100
        await ctx.send(f'**`{ctx.author}`**: 音量を変更 **{vol}%**')

    @commands.command(name='stop')
    async def stop_(self, ctx):
        """Stop the currently playing song and destroy the player.
        !Warning!
            This will destroy the player assigned to your guild, also deleting any queued songs and settings.
        """
        global loopka
        vc = ctx.voice_client
        loopka = 0

        if not vc or not vc.is_connected():
            return await ctx.send('ボイスチャットに入っていません', delete_after=20)

        await self.cleanup(ctx.guild)
    @commands.command(name="loop")
    async def repeat_(self, ctx):
        global loopka
        """Repeat the currently playing song.
        Examples
        ----------
        <prefix>repeat
            {ctx.prefix}repeat
        """
        player = self.get_player(ctx)

        await ctx.trigger_typing()

        vc = ctx.voice_client
        loopka = 1

        if not vc:
            await ctx.invoke(self.connect_)

        upcoming = list(itertools.islice(player.queue._queue, 0, 30)) 
        fmt = list(f' {_["web_url"]} ' for _ in upcoming)
        fmt.append(vc.source.web_url)
        print(fmt) 

        await ctx.send("repeat")

        vc = ctx.voice_client
        while loopka == 1: 
            loopke = list(itertools.islice(player.queue._queue, 0, 30)) 
            print(upcoming)
            if len(loopke) <=  1 :   
                for search in fmt :
                    source = await YTDLSource.create_source(ctx,search, loop=self.bot.loop, download=True)
                    await player.queue.put(source)
                    print("if Trune")
            print("loop スルー")
            await asyncio.sleep(10)
        else:
            print("loop終了")

         

    @commands.command(name="loopend")
    async def repeatend_(self, ctx):
        global loopka
        
        loopka = 0 


        await ctx.send("loopを終了します")

    @commands.command(name='pl')
    async def playlist_(self, ctx,plli):
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = self.get_player(ctx)
        if 'bokaro' in plli :
            for search in  playlist.bokaro:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)

                await player.queue.put(source)
    
  
        elif 'sui' in plli :
            for search in  playlist.sui:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)

                await player.queue.put(source)

        elif 'perc' in plli :
            for search in  playlist.bokaro:
                source = await YTDLSource.create_source(ctx, search, loop=self.bot.loop, download=True)

                await player.queue.put(source)
        else:
            await ctx.send(f"{plli} の名前のplaylistが見つかりませんでした")

    @commands.command(name="shuffle", aliases=["mix"])
    async def shuffle_(self, ctx):
        """Shuffle the current queue.
        Aliases
        ---------
            mix
        Examples
        ----------
        <prefix>shuffle
            {ctx.prefix}shuffle
            {ctx.prefix}mix
        """
    

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)


          
        await self.do_shuffle(ctx)

        await ctx.send("シャッフルします")
    async def do_shuffle(self, ctx):
        player = self.get_player(ctx)
        random.shuffle(player.queue._queue)



bot.add_cog(Music(bot))
bot.run(os.environ['TOKEN'])
       


