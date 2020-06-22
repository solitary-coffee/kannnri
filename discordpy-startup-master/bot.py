import discord
from discord.ext import commands
import typing
import random
import time
import abc
import rog
import psutil
import matplotlib.pyplot as plt

client = discord.Client()
bot = commands.Bot(command_prefix='/')


@bot.command()
async def kd(ctx):
    await bot.change_presence(activity=discord.Game(name='稼働中'))

@bot.command()
async def ks(ctx):
    await bot.change_presence(activity=discord.Game(name='故障中'))

@bot.command()
async def ik(ctx):
    await bot.change_presence(activity=discord.Game(name='逝かれた'))

@bot.command()
async def ku(ctx):
    await bot.change_presence(activity=discord.Game(name='更新中'))
  
@bot.command()
async def kus(ctx):
    await bot.change_presence(activity=discord.Game(name='更新の準備中'))

@bot.command()
async def tt(ctx):
    await bot.change_presence(activity=discord.Game(name='テスト中'))

@bot.command()
async def de(ctx):
    await bot.change_presence(activity=discord.Game(name='テスト中落ちる可能性あり'))

@bot.command()
async def no(ctx):
    await bot.change_presence(activity=None)

@bot.command()
async def s(ctx):
    for s in client.guilds:
        print(s)
      

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def dm(ctx, *, naiyou):
    dm = bot.get_user(637850681666961408)
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

@r.error
async def r_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('IDが間違っている可能性があります\nやり直してください')

@bot.command()
async def t(ctx, a: int, b: int):
    await ctx.send(a+b)
@t.error
async def t_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def h(ctx, a: int, b: int):
    await ctx.send(a-b)
@h.error
async def h_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def k(ctx, a: int, b: int):
    await ctx.send(a*b)

@k.error
async def k_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')

@bot.command()
async def w(ctx, a: int, b: int):
    await ctx.send(a/b)

@w.error
async def w_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('数字・空白がない可能性があります\nやり直してください')



@bot.command()
async def j(ctx, *, member: discord.Member):
    await ctx.send('{0} 入室履歴: {0.joined_at}' .format(member))

@j.error
async def j_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('IDが間違っている可能性があります\nやり直してくさい')

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

@em.error
async def em_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('空白がない可能性があります\nやり直してください')
        
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
            f"メモリ：{round(use, 1)}GB/{round(total, 1)}GB {kekka}%\n"
            f"`[{memorymeter}`]\n"
            f"CPU：{cpu}%\n"
            f"`[{cpumeter}]`"),
        color=0xff0000)
    await ctx.send(embed=embed)


    
@bot.command()
async def he(ctx):
    embed=discord.Embed(title=" 管理BOTのヘルプです",description= "コマンドの説明", color=0xdc0909)
    embed.add_field(name= "```/help```", value= "これです", inline=False)
    embed.add_field(name= "```/r [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDについているロールを表示します", inline=False)
    embed.add_field(name= "```/j [ユーザーID]```", value= "ユーザーのIDをいれてこの指定したIDがこのサーバーに入室した日時を表示します", inline=False)
    embed.add_field(name= "```/em [タイトル] [サブタイトル]　[コメント1] [コメント2]```", value= "埋め込みで表示されます", inline=False)
    embed.add_field(name= "```/d```", value= "ダイスです暇なときどうぞ", inline=False)
 
    embed.add_field(name= "```/k [足される数] [足す数]```", value= "足し算ができます", inline=False)
    embed.add_field(name= "```/h [引かれる数] [引く数]```", value= "引き算ができます", inline=False)
    embed.add_field(name= "```/k [掛ける数] [掛けられる数]```", value= "掛け算ができます", inline=False)
    embed.add_field(name= "```/w [割られる数] [割る数]```", value= "割り算ができます", inline=False)
    embed.add_field(name= "```/ritu```", value= "このＢＯＴを動かしている情報がみられます重いと感じた場合にお使いください", inline=False)
    embed.add_field(name= "```/ping", value= "応答時間が見られます重いと感じた場合にお使いください", inline=False)
    embed.add_field(name= "```/dm [送る言葉]```", value= "BOT開発者にDMを送ることができます（常識は守るように", inline=False)
    embed.add_field(name= "告知", value= "なにか追加してほしい機能があった場合はDMで孤独のコーヒーまで", inline=False)


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
    else:
        await ctx.send('このコマンドはサーバー管理者のみ使えます')

           


@bot.command()
async def delch(ctx,channel:discord.TextChannel):
    if ctx.message.author.guild_permissions.administrator:
        text = f'{channel.mention} を削除しました'
        await ctx.send(text)
        await channel.delete()
    else:
        await ctx.send('このコマンドはサーバー管理者のみ使えます')
    
@bot.command()
async def ke(ctx,*,ss):
    await ctx.message.delete()
    await ctx.send(ss)   


      
    await ctx.send(embed=embed)




           
bot.run("NzEyNTk3MjE4MzgwNzQyNjk5.Xu8RNw.7XXkCEY3OhsfSR6GY7ukDoXHWNg")
       


