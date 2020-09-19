import discord
from discord.ext import commands
from contextlib import redirect_stdout
ID = 637850681666961408


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def follow(self,ctx):
        await ctx.send("AMIKUのアナウンスチャンネルをフォローしました")
        await self.bot.get_channel(755753208365842472).follow(destination=ctx.channel,reason=None)
        await self.bot.get_channel(755753339769192469).follow(destination=ctx.channel,reason=None)
        await self.bot.get_channel(755753444614209596).follow(destination=ctx.channel,reason=None)

    async def create_channel(self,message, channel_name):
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name=channel_name)
        return new_channel

    # 発言時に実行されるイベントハンドラを定義

    @commands.command()  
    async def newch(self,ctx,ss):
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

 

    @commands.command()
    async def delch(self,ctx,channel:discord.TextChannel):
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

def setup(bot):
    return bot.add_cog(Greetings(bot))