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


client = discord.Client()
bot = commands.Bot(command_prefix='/')

ID = 637850681666961408





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
async def kt(ctx,kasutamu):
    if ctx.message.author.id == ID:    
        await bot.change_presence(activity=discord.Game(name=kasutamu))
    else:
        await ctx.send("このコマンドは管理者専用です")

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
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        await ctx.send("ロード中です")
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))


    @commands.command()
    async def st(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""
        await ctx.send("ロード中です")

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: \n {}'.format(player.title))

    @commands.command()
    async def v(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()
        
    @commands.command()
    async def pause(self, ctx):
        await ctx.send("一時停止しました")
        await ctx.voice_client.pause()
    
    
    @commands.command()
    async def play(self, ctx):
        await ctx.send("一時停止した場所からスタートします")
        await ctx.voice_client.resume()


    @yt.before_invoke
    @st.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        

       

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
    embed=discord.Embed(title=" 管理BOTのヘルプです",description= "コマンドの説明", color=0xdc0909)
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
    embed.add_field(name= "```/ke [言葉]```", value= "BOTに喋らすことができますまた言葉がきえるます　（ボッチ用ですw)", inline=False)
    embed.add_field(name= "```/yt [URL]```", value= "youtubeを流すことができます(音源のみ)", inline=False)
    embed.add_field(name= "```/st [URL]```", value= "youtubeを流すことができます(音源のみ)", inline=False)
    embed.add_field(name= "```/pause```", value= "一時停止します", inline=False)
    embed.add_field(name= "```/play```", value= "一時停止した時間から再開します", inline=False)
    embed.add_field(name= "```/stop```", value= "曲が停止します＆BOTがvcから抜けます", inline=False)
    embed.add_field(name= "音楽流し方", value= "1.流したいｖｃに入ります　\n 2./yt・/stで流したい曲を指定します　\n 3. あとは待つだけ　\n 4.　終了したい場合は/stopをお願いします", inline=False)
    embed.add_field(name= "告知", value= "なにか追加してほしい機能があった場合・不具合などがあった場合/dmを利用し伝えてください", inline=False)
    embed.add_field(name= "その他", value= "音楽を流す機能に検索・ループ・リストなど追加する予定です　しばらくお待ちください", inline=False)
      
    await ctx.send(embed=embed)





bot.add_cog(Music(bot))           
bot.run("NzEyNTk3MjE4MzgwNzQyNjk5.Xu8RNw.7XXkCEY3OhsfSR6GY7ukDoXHWNg")
       


