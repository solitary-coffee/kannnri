import discord
from discord.ext import commands
import sys
import json

goban = []
motolist =[]
bank = [637850681666961408,719448076506365972,675676179390267402] 
bans = [637850681666961408]
nai = []
class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    async def rodo(self,ctx):
        global goban
        goban =[]
        mass =  self.bot.get_channel(769733803831853136)

        id = mass.last_message_id
        msg = await mass.fetch_message(id)
        await msg.attachments[0].save("goban.json")
        with open("goban.json", "r",encoding="utf-8") as data:
            data = json.load(data)
            for da in (data['goban']):
                goban += [da]
        



    @commands.Cog.listener()
    async def on_ready(self):
        global goban
        
        mass =  self.bot.get_channel(769733803831853136)

        id = mass.last_message_id
        msg = await mass.fetch_message(id)
        await msg.attachments[0].save("goban.json")
        with open("goban.json", "r",encoding="utf-8") as data:
            data = json.load(data)
            for da in (data['goban']):
                goban += [da]
        print(goban)
        
    @commands.Cog.listener()
    async def on_message(self,message):
        global goban
        if message.author.bot:
        # もし、送信者がbotなら無視する
            return
        GLOBAL_CH_NAME = "coffee-global" # グローバルチャットのチャンネル名

        if message.channel.name == GLOBAL_CH_NAME:
            if message.author.id in goban:
                embed = discord.Embed(title="あなたはGBANされています", description="異議などは　[こちらまで](https://discord.gg/GWrvMT4)　", color=0xf00)
        

                await message.channel.send(embed=embed)

                return
    
            else:
                try:
                    
                    await message.delete()
                except:
                    print("e")            
                 # 元のメッセージは削除しておく
                channels = self.bot.get_all_channels()
                global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
                # channelsはbotの取得できるチャンネルのイテレーター
                #  global_channelsは hoge-global の名前を持つチャンネルのリスト
                if message.author.id in bans :
                    ken = "BAN権限・管理"
                elif message.author.id in bank :
                    ken = "BAN権限"
            
                else:
                    ken = "None"
                embed = discord.Embed(title=f"ID:{message.author.id}",
                    description=message.content, color=0x00bfff)
                embed.add_field(name='権限', value=f"{ken}", inline=False)
                embed.set_author(name=message.author.display_name, 
                    icon_url=message.author.avatar_url_as(format="png"))
                embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                    icon_url=message.guild.icon_url_as (format="png"))

 
                #    Embedインスタンスを生成、投稿者、投稿場所などの設定
                for  channel1 in global_channels:
                    try:
                    
                        await channel1.send(embed=embed)
                        pass
                    
                    except discord.errors.Forbidden :
                        await message.channel.send("権限不足です`埋め込みリンク`の権限を許可してください")
        
                        pass
        

    @commands.command()
    async def gb(self,ctx,ss,riyu=None): 
        global motolist
        if ctx.author.id in bank:
            with open("goban.json", "r",encoding="utf-8") as moto:

                moto = json.load(moto)
                for da in (moto['goban']):
                    motolist += [f"{da}"]
            with open("goban.json","w",encoding="utf-8") as data:                     
                    # ']'を削除
                data.write('{\n')   
                data.write('"goban":[\n')  
                for moto in motolist: 

                    data.write(f'{str(moto)}')
                    data.write(", \n")

                data.write(f'{ss}\n ]')    
                data.write('\n}')               
          

        
            await ctx.send(f"データベースに{ss}を追加しました")
            await self.bot.get_channel(769733803831853136).send(file=discord.File('goban.json'))
            print(motolist)
            motolist = []
            await Greetings.rodo(self,ctx)
            await self.bot.get_channel(779888284004384848).send(f"```BANID：{ss}\n 理由：{riyu} \n 実行者：{ctx.author.name}```")
        else:
            await ctx.send("BAN権限者のみ実行可能")
    
    @commands.command()
    async def gbsaku(self,ctx,ss,riyu=None):
        global motolist 
        if ctx.author.id in bank:
        
            with open("goban.json", "r",encoding="utf-8") as moto:

                moto = json.load(moto)
                for da in (moto['goban']):
                    if  int(ss) == int(da):
                        print("e")
                        pass
                    elif int(0) == int(da):
                        pass
                    
                    else:
                        motolist += [da]
            print(motolist)

        
            with open("goban.json","w",encoding="utf-8") as data:
                data.write('{\n')   
                data.write('"goban":[\n')  

                for moto in motolist: 
  
                    data.write(f'{str(moto)}')
                    data.write(", \n")
                data.write("0")

                data.write(f'\n ]')    
                data.write('\n}')   
        
            await ctx.send(f"データベースから{ss}を削除しました")
            await self.bot.get_channel(769733803831853136).send(file=discord.File('goban.json'))
            await self.bot.get_channel(779888284004384848).send(f"```BANID：{ss}\n 理由：{riyu} \n 実行者：{ctx.author.name}```")

            await Greetings.rodo(self,ctx)
        else:
            await ctx.send("BAN権限者のみ実行可能")
    @commands.command()
    async def gbz(self,ctx): 
        global nai
        if ctx.author.id in bank:
            with open("goban.json", "r",encoding="utf-8") as moto:

                moto = json.load(moto)
                for da in (moto['goban']):
                    nai += [f"{da}"]
                await ctx.send(nai)

        

def setup(bot):
    return bot.add_cog(Greetings(bot))
