import discord
from discord.ext import commands
import time
import psutil

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
    async def ping(self,ctx):
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
        await Greetings.err(ctx)

    @commands.command()
    async def ritu(self,ctx):
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
        await Greetings.err(self,ctx)  


                          

def setup(bot):
    return bot.add_cog(Greetings(bot))
