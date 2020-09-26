import discord
from discord.ext import commands
from deta import gapl
import random
import time
gari1 = []
gari2 = []
gali = {
}


ti1 = list()
ti2 = list()
pl1n = []
pl2n = []

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def suta(self,ctx,channel1: discord.VoiceChannel,channel2: discord.VoiceChannel):
        if ctx.message.guild.id  in gapl.kili:     
            global pl1n ,pl2n ,gari1,gari2,ti1,ti2,gali
            def check(m):
                return m.author == ctx.author
            vc = await channel1.connect()                        
            gari1 = [i.name for i in vc.channel.members]
            await vc.disconnect()

            vc = await channel2.connect()                        
            gari2 = [i.name for i in vc.channel.members]
            await vc.disconnect()

            gale1 = len(gari1)
            gale2 = len(gari2)
            pl1n = len(gari1)
            pl2n = len(gari2)
            await ctx.send("チーム1の戦闘情報は")
            for i in range(gale1):
                if gari1[i] == ctx.me.display_name:
                    pass
                else:
                    gali.update([(f"{gari1[i]}hp",random.randint(100, 200) ),(f"{gari1[i]}afk",random.randint(25, 50))])
                    hp = gali[gari1[i] + "hp"] 
                    afk = gali[gari1[i] + "afk"]
                    ti1.append (gari1[i])
        
                    await ctx.send(f"```{gari1[i]} HP：{hp}　AFK：{afk}```")
            await ctx.send("チーム2の戦闘情報は")
            for i in range(gale2):
                if gari2[i] == ctx.me.display_name:
                    pass           
                else:
                    gali.update([(f"{gari2[i]}hp",random.randint(100, 200) ),(f"{gari2[i]}afk",random.randint(25, 50))])
                    hp = gali[gari2[i] + "hp"] 
                    afk = gali[gari2[i] + "afk"]
                    ti2.append (gari2[i])
                    await ctx.send(f"```{gari2[i]} HP：{hp}　AFK：{afk}```")
            def check1(m):
                return m.author.name == pl1
            await ctx.send("です")
            while pl1n > 1 and   pl2n > 1:
                pl1 = random.choice(ti1)
                pl1afk = gali[pl1 + "afk"]
                await ctx.send(f"チーム1の{pl1}さんが選択します　[戦闘：1、回復：2]" )
                msg = await self.bot.wait_for("message", check=check1)
                pl2 = random.choice(ti2)      
                pl2hp = gali[pl2 + "hp"]  
                if  msg.content  == str(1):
                  
                    pl2hps =  random.choice([pl1afk-5 ,pl1afk-4,pl1afk-3,pl1afk-2,pl1afk-1,pl1afk,pl1afk+1,pl1afk+2, pl1afk+3,pl1afk+4,  pl1afk+5,0])
                    p2hpg = pl2hp - pl2hps
                    await ctx.send(f"戦闘します 自分の　AFK ：`{pl1afk}` ")
                    await ctx.send(f"攻撃相手は　{pl2}です　相手のＨＰ`{pl2hp}`　")
                    gali.update([(f"{pl2}hp",p2hpg )])
                
                    if p2hpg <= 0:
                        await ctx.send(f"{pl2} さんは倒されました")
                        pl1n -= 1
                    elif pl2hps == 0:
                        await ctx.send("ミスしました　攻撃量は`0`です")
                    else:    
                        await ctx.send(f"攻撃後のＨＰ　` {p2hpg}`")
                if  msg.content  == str(2):
                    pl1hp = gali[pl1 + "hp"]  
                    pl1hps =  random.randint(pl1afk-20 , pl1afk-15)
                    p1hpg = pl1hp + pl1hps
                    gali.update([(f"{pl1}hp",p1hpg )])
                    await ctx.send(f"回復完了　[{pl1hp}]→ [{p1hpg}]")


                def check2(m):
                    return m.author.name == pl2
                pl2 = random.choice(ti2)
                pl2afk = gali[pl2 + "afk"]
                await ctx.send(f"チーム2の{pl2}さんが選択します　[戦闘：1、回復：2]" )
                msg = await self.bot.wait_for("message", check=check2)
                if  msg.content  == str(1):
                 
                    pl1 = random.choice(ti1)      
                    pl1hp = gali[pl1 + "hp"]  
                    pl1hps =  random.choice([pl2afk-5 ,pl2afk-4,pl2afk-3,pl2afk-2,pl2afk-1,pl2afk,pl2afk+1,pl2afk+2, pl2afk+3,pl2afk+4,  pl2afk+5,0])
                    p1hpg = pl1hp - pl1hps
                    await ctx.send(f"戦闘します 自分の　AFK ：`{pl2afk}` ")
                    await ctx.send(f"攻撃相手は　{pl1}です　相手のＨＰ`{pl1hp}`　")
                    gali.update([(f"{pl1}hp",p1hpg )])
                    if p1hpg <= 0:
                        await ctx.send(f"{pl1} さんは倒されました")
                        pl2n -= 1
                    elif pl1hps == 0:
                        await ctx.send("ミスしました　攻撃量は`0`です")
            
                    else:    
                        await ctx.send(f"攻撃後のＨＰ　` {p1hpg}`")
                if  msg.content  == str(2):
                    pl2afk = gali[pl2 + "afk"] 
                    pl2hp = gali[pl2 + "hp"]  
                    pl2hps =  random.randint(pl2afk-20 , pl2afk-15)
       
                    p2hpg = pl2hp + pl2hps
                    gali.update([(f"{pl2}hp",p2hpg )])
                    await ctx.send(f"回復完了　[{pl2hp}]→[{p2hpg}]")

            if pl1n == 0:
                await ctx.send("チーム1が全滅させられました　よってチーム2の勝利です")
                gari1 = []
                gari2 = []
                gali = {

                }   


                ti1 = []
                ti2 = []
                pl1n = []
                pl2n = []
            elif pl2n == 0:
                await ctx.send("チーム2が全滅させられました　よってチーム1の勝利です")
                gari1 = []
                gari2 = []
                gali = {

                }   


                ti1 = []
                ti2 = []
                pl1n = []
                pl2n = []
    @commands.command()
    async def d(self,ctx):
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


def setup(bot):
    return bot.add_cog(Greetings(bot))
