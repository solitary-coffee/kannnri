import discord
from discord.ext import commands
from contextlib import redirect_stdout
ID = 637850681666961408

import datetime
import pytz
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    async  def err(self,ctx):
        import textwrap
        ch = 766939626874994688
        e = discord.Embed(title=f"機能ログ:{ctx.author.name} \n`{textwrap.shorten(ctx.message.content, width=512)}` ", description=f"　{ctx.guild}/{ctx.channel}　\n{dt_now.strftime('%Y-%m-%d %H:%M')}", color=0xf00)
        await self.bot.get_channel(ch).send(embed=e)

    @commands.command()
    async def follow(self,ctx):
        try:

            await self.bot.get_channel(755753208365842472).follow(destination=ctx.channel,reason=None)
            await self.bot.get_channel(755753339769192469).follow(destination=ctx.channel,reason=None)
            await self.bot.get_channel(755753444614209596).follow(destination=ctx.channel,reason=None)
            await ctx.send("AMIKUのアナウンスチャンネルをフォローしました")
        except discord.errors.Forbidden :
            ctx.send("権限不足です`ウェブフック権限`を許可してください" ) 
                

    async def create_channel(self,message, channel_name):
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name=channel_name)
        return new_channel

    # 発言時に実行されるイベントハンドラを定義

    @commands.command()  
    async def newch(self,ctx,ss):
        await Greetings.err(self,ctx)
        try:

            if ctx.message.author.guild_permissions.administrator:
            # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
                new_channel = await self.create_channel(ctx, channel_name=ss)

            # チャンネルのリンクと作成メッセージを送信
                text = f'{new_channel.mention} を作成しました'
                await ctx.send(text)
            elif ctx.message.author.id == ID:    
                new_channel = await self.create_channel(ctx, channel_name=ss)

                # チャンネルのリンクと作成メッセージを送信
                text = f'{new_channel.mention} を作成しました'
                await ctx.send(text)
            else:
                await ctx.send('このコマンドはサーバー管理者のみ使えます')
        except discord.errors.Forbidden :
            await ctx.send("権限不足です`チャンネル管理`の権限を許可してください")

 

    @commands.command()
    async def delch(self,ctx,channel:discord.TextChannel):
        await Greetings.err(self,ctx)
        try:
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
        except:
            await ctx.send("権限不足です`チャンネル管理`の権限を許可してください")

def setup(bot):
    return bot.add_cog(Greetings(bot))
