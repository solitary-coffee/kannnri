import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def he(self,ctx):
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
        embed.add_field(name= "```/kick [ID] [理由:なくてもおｋ]```", value= "サーバー管理者のみ利用可能　キックができます", inline=False)
        embed.add_field(name= "```/ban [ID] [理由:なくてもおｋ]```", value= "サーバー管理者のみ利用可能　banができます", inline=False)
        embed.add_field(name= "```/follow```", value= "お知らせなどを受信できます", inline=False)
        embed.add_field(name= "その他情報", value= "```お知らせ等を受信するには /follow  ```", inline=False)
        embed.add_field(name= "**音楽機能**", value= "別枠です　コマンド　/muhe", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def muhe(self,ctx):
        embed=discord.Embed(title=" 管理BOTのヘルプ[2]です",description= "音楽コマンドの説明", color=0xdc0909)
        embed.add_field(name= "```/play [URL・キーワード]```", value= "　youtubeから再生します \n　キーワードは検索し一番上のを再生します", inline=False)
        embed.add_field(name= "```/pause```", value= "一時停止します", inline=False)
        embed.add_field(name= "```/resume```", value= "一時停止から再生します", inline=False)
        embed.add_field(name= "```/skip```", value= "リストに入ってる次の曲を流します", inline=False)
        embed.add_field(name= "```/q```", value= "リストです", inline=False)
        embed.add_field(name= "```/np```", value= "再生している曲名・再生者を表示します", inline=False)
        embed.add_field(name= "```/vol```", value= "音量を調節できます（上げすぎると音割れします）", inline=False)
        embed.add_field(name= "```/stop```", value= "リスト＆オート再生機能が終了します（BOTは抜けません）", inline=False)
        embed.add_field(name= "```/sloop```", value= "現在の曲をリピートします ", inline=False)
        embed.add_field(name= "```/qloop```", value= "現在のをリストリピートします", inline=False)    
        embed.add_field(name= "```/mix```", value= "シャッフルします（playlistはしません）", inline=False)
        embed.add_field(name= "```/leave```", value= "BOT vcから抜けますから", inline=False)
        embed.add_field(name= "```/se [キーワード]```", value= "５曲　検索します", inline=False)
   
        await ctx.send(embed=embed)

def setup(bot):
    return bot.add_cog(Greetings(bot))
