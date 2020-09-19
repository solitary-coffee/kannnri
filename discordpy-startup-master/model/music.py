import discord
from discord.ext import commands
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
import youtube_dl
from deta import playlist
import random
from apiclient.discovery import build

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    api_key = 'AIzaSyCyMz5iWCEX0vvUabjYld1i3kjV2i9wS3Y'

    def get_videos_search(self,keyword):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
        youtube_res = youtube_query.execute()
        return youtube_res.get('items', [])

    @commands.command()
    async def se(self,ctx,*,ss):
        result = self.get_videos_search(ss)
        for item in result:
            if item['id']['kind'] == 'youtube#video':
                embed=discord.Embed(title= "youtube検索結果",description= f"{ss}で検索しました", color=0xdc0909)
                embed.add_field(name=item['snippet']['title'] , value= 'https://www.youtube.com/watch?v=' + item['id']['videoId'], inline=True)
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
        async def create_source(self,cls, ctx, search: str, *, loop, download=False):
            print("DL1")
            loop = loop or asyncio.get_event_loop()

            to_run = partial(Greetings.ytdl.extract_info, url=search, download=download)
            data = await loop.run_in_executor(None, to_run)

            if 'entries' in data:
                # take first item from a playlist
                data = data['entries'][0]

            await ctx.send(f'```ini\n[ {data["title"]}がリストに入りました.]\n```', delete_after=10)
        

            if download:
                source = Greetings.ytdl.prepare_filename(data)
            else:
                return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

            return Greetings.YTDLSource(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)
        
            print("DL１終わり")

        @classmethod
        async def regather_stream(self,cls, data, *, loop):
            """Used for preparing a stream, instead of downloading.
            Since Youtube Streaming links expire."""
            print("ｄｌ2")
            loop = loop or asyncio.get_event_loop()
            requester = data['requester']

            to_run = partial(self.ytdl.extract_info, url=data['webpage_url'], download=False)
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
            elif isinstance(error, self.InvalidVoiceChannel):
                await ctx.send('Error connecting to Voice Channel. '
                            'Please make sure you are in a valid channel or provide me with one')

            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        def get_player(self, ctx):
            """Retrieve the guild player, or generate one."""
            try:
                player = self.players[ctx.guild.id]
            except KeyError:
                player = Greetings.MusicPlayer(ctx)
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
                    await ctx.send('参加するチャンネルがありません。有効なチャンネルを指定するか、チャンネルに参加してください。')

            vc = ctx.voice_client

            if vc:
                if vc.channel.id == channel.id:
                    return
                try:
                    await vc.move_to(channel)
                except asyncio.TimeoutError:
                    await ctx.send(f'Moving to channel: <{channel}> timed out.')
            else:
                try:
                    await channel.connect()
                except asyncio.TimeoutError:
                    await ctx.send(f'Connecting to channel: <{channel}> timed out.')

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
            source = await Greetings.YTDLSource.create_source(self,ctx, search, loop=self.bot.loop, download=True)

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
            vc = ctx.voice_client

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
                        source = await self.YTDLSource.create_source(ctx,search, loop=self.bot.loop, download=True)
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
                    source = await Greetings.YTDLSource.create_source(self,ctx, search, loop=self.bot.loop, download=True)

                    await player.queue.put(source)
    
  
            elif 'sui' in plli :
                for search in  playlist.sui:
                    source = await Greetings.YTDLSource.create_source(self,ctx, search, loop=self.bot.loop, download=True)

                    await player.queue.put(source)

            elif 'perc' in plli :
                for search in  playlist.bokaro:
                    source = await Greetings.YTDLSource.create_source(self,ctx, search, loop=self.bot.loop, download=True)

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
            
def setup(bot):
    bot.add_cog(Greetings.Music(bot))
    return bot.add_cog(Greetings(bot))
