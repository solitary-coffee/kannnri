from discord.ext import commands
import sys
import json
import requests
import  discord


goban = []
goid = []
motolist =[]
bank = [637850681666961408,719448076506365972,675676179390267402] 
bans = [637850681666961408]
nai = []


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    async def banrodo(self,ctx):
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
        print("--------------------------------------------")
        print(f"グローバルチャットBANID更新:\n{goban}")
        
    async def idrodo(self,ctx):
        global goid
        goid =[]
        mass =  self.bot.get_channel(781118741491613717)

        id = mass.last_message_id
        msg = await mass.fetch_message(id)
        await msg.attachments[0].save("goid.json")
        with open("goid.json", "r",encoding="utf-8") as data:
            data = json.load(data)
            for da in (data['goid']):
                if int(da) == 0:
                    pass
                else: 
                    goid += [da]
        print("-----------------------------------------------")
        print(f"グローバルチャットID更新:\n {goid}")
        
        



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
        print(f"coffee-globalでBANしてるID: \n {goban}")
    
        global goid
        
        mass =  self.bot.get_channel(781118741491613717)

        id = mass.last_message_id
        msg = await mass.fetch_message(id)
        await msg.attachments[0].save("goid.json")
        with open("goid.json", "r",encoding="utf-8") as data:
            data = json.load(data)
            for da in (data['goid']):
                if int(da) == 0:
                    pass
                else:        
                    goid += [da]
        print(f"coffee-globalで登録しているチャンネルID:  \n {goid}")
        
        
    @commands.Cog.listener()
    async def on_message(self,message):
        global goban
        global goid
        if message.author.bot:
        # もし、送信者がbotなら無視する
            return
    
        if message.channel.id in goid :
            if message.author.id in goban:
                embed = discord.Embed(title="あなたはGBANされています", description="異議などは　[こちらまで](https://discord.gg/GWrvMT4)　", color=0xf00)
        

                await message.channel.send(embed=embed)

                return
    
            else:
                try:
                    
                    await message.delete()
                except:
                    pass
                          
                 # 元のメッセージは削除しておく
                
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
                for  CHANNEL_ID in goid:
                    try:
                        channel1 = self.bot.get_channel(CHANNEL_ID)
                        
                        await channel1.send(embed=embed)
                        
                    
                    except:
                        print("-------------------------------------")
                        print(f"グローバルチャットでエラー\nチャンネルID:{CHANNEL_ID}")
   
        

        

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
           
            motolist = []
            await Greetings.banrodo(self,ctx)
            await self.bot.get_channel(779888284004384848).send(f"```BANID：{ss}\n 理由：{riyu} \n 実行者：{ctx.author.name}```")
            print("-------------------------------------------------")
            print(f"グローバルチャットBANID更新（追加のみ）:\n {ss}")
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

                        pass
                    elif int(0) == int(da):
                        pass
                    
                    else:
                        motolist += [da]
                        print("----------------------------------------")
                        print(f"リストに追加:\n{da}")
          

        
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

            await Greetings.banrodo(self,ctx)
            print("-------------------------------------------------")
            print(f"グローバルチャットBANID更新（削除のみ):\n {ss}")
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


    @commands.command()
    async def global_join(self,ctx,riyu=None): 
        global motolist
        global goid

        
        
        with open("goid.json", "r",encoding="utf-8") as moto:

            moto = json.load(moto)
                
            for da in (moto['goid']):
                if int(da) == 0:
                    pass
                else:  
                    motolist += [f"{da}"]
        with open("goid.json","w",encoding="utf-8") as data:                     
                    # ']'を削除
            data.write('{\n')   
            data.write('"goid":[\n')  
            for moto in motolist: 

                data.write(f'{str(moto)}')
                data.write(",")

            data.write(f'{ctx.channel.id}\n ]')    
            data.write('\n}')               

          

        
        await ctx.send(f"グローバルチャットに参加しました")
        await self.bot.get_channel(781118741491613717).send(file=discord.File('goid.json'))
        
        motolist = []

        em = discord.Embed(title="グローバルチャット参加通知",
            description=f"coffee-globalに参加チャンネルが増えました\n 参加鯖名:{ctx.guild.name}", color=0x00bfff)
        for  CHANNEL_ID in goid:
            try:
                channel1 = self.bot.get_channel(CHANNEL_ID)                       
                await channel1.send(embed=em)                    
            except discord.errors.Forbidden :        
                pass
        await Greetings.idrodo(self,ctx)
       
        webhook_url  = 'https://discord.com/api/webhooks/781131142031212574/zLg24ljOOl2AlFjwNYhq8Ozk5aSbxM0qM2OvVp0NhF9v7a7m3nOuj8CHA0okLtlNF6iB'
        embeds       = [
                   {    'title':"グローバルチャットに参加しました",
                       'description': f'鯖名:{ctx.guild.name}\n  チャンネル名：{ctx.channel.name}',
                       'color': 6389247,
  
                    }
               ]
        main_content = {
                   'username': 'AMIKUグローバルチャットログ',
                   #'avatar_url': '画像のURL',
                   'content': '',
                   'embeds': embeds
                 }
        headers      = {'Content-Type': 'application/json'}

        response     = requests.post(webhook_url, json.dumps(main_content), headers=headers)
        print("-------------------------------------------------")
        print(f"グローバルチャットID更新（追加のみ）:\n {ctx.channel.id}")
    @commands.command()
    async def global_Withdrawal(self,ctx):
        global motolist 
        ss = ctx.channel.id
        motolist = []
        
        with open("goid.json", "r",encoding="utf-8") as moto:

            moto = json.load(moto)
            for da in (moto['goid']):
                if  int(ss) == int(da):
                    print("e")
                    pass
                elif int(0) == int(da):
                    pass
                    
                else:
                    motolist += [da]
        print(motolist)

        
        with open("goid.json","w",encoding="utf-8") as data:
            data.write('{\n')   
            data.write('"goid":[\n')  

            for moto in motolist: 
  
                data.write(f'{str(moto)}')
                data.write(", \n")
                
            data.write("0")

            data.write(f'\n ]')    
            data.write('\n}')   
        
        await ctx.send(f"グローバルチャットから脱退しました")
        await self.bot.get_channel(781118741491613717).send(file=discord.File('goid.json'))
        webhook_url  = 'https://discord.com/api/webhooks/781131142031212574/zLg24ljOOl2AlFjwNYhq8Ozk5aSbxM0qM2OvVp0NhF9v7a7m3nOuj8CHA0okLtlNF6iB'
        embeds       = [
                   {    'title':"グローバルチャットから脱退しました",
                       'description': f'鯖名:{ctx.guild.name}\n  チャンネル名：{ctx.channel.name}',
                       'color': 15146762,
  
                    }
               ]
        main_content = {
                   'username': 'AMIKUグローバルチャットログ',
                   #'avatar_url': '画像のURL',
                   'content': '',
                   'embeds': embeds
                 }
        headers      = {'Content-Type': 'application/json'}

        response     = requests.post(webhook_url, json.dumps(main_content), headers=headers)

        await Greetings.idrodo(self,ctx)
        print("-------------------------------------------------")
        print(f"グローバルチャットID更新（削除のみ):\n {ctx.channel.id}")
          
 
        

def setup(bot):
    return bot.add_cog(Greetings(bot))
