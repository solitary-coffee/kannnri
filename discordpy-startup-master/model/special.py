import discord
from discord.ext import commands
import asyncio


yu = {
    "空輸":2,
    "船":5,
    "トラック":6,
}
oka = {
    "空輸":5000,
    "船":500,
    "トラック":2000,
}

oka = {
    "木材":10,
    "石材":40,
    "石油":50,
    "天然ガス":50,
    "二酸化チタン":60,
    "鉄骨":100,
    "コンクリート":200,
    "現金":"時価です、管理者に確認してください",

}

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


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def tm(self,ctx, tm):
        if ctx.message.guild.id == 727850593330397265:
            dm = self.bot.get_user(716754062879490111)
            for word in kai:
                if word in ctx.message.content:
                    await ctx.send(f"{tm}を購入しました　代金は{kai[tm]}$")
            embed=discord.Embed(title= f"{ctx.message.author.name}が購入しました",description= "サーバからです" , color=0x3498db)
            embed.add_field(name= f"買ったもの：{tm}" , value=  f"代金：{list[tm]}", inline=False)
            await dm.send(embed=embed)
        else:
            await ctx.send("ここで使えません")




    @commands.command()
    async def kau(self,ctx,mono,kosuu,yusou,kaisya):
        if ctx.message.guild.id == 727850593330397265:
            await ctx.send(f"{mono}を{kosuu}個を{yusou}で{kaisya}に送ります")
            zai = yu[yusou] * 3060
            await ctx.send(f"材料費は　{oka[mono]} ＄です")
            await ctx.send("出荷費は・・\n それぐらい自分で計算しろｗ　\n (現在ＢＯＴは反抗期です すいません")
            await ctx.send(f"輸送時間は　{yu[yusou]}時間です（予想です遅れる場合もあります")
            await asyncio.sleep(zai)
            await ctx.send(f"{ctx.message.author.mention}さん　荷物が届いてます") 

def setup(bot):
    return bot.add_cog(Greetings(bot))