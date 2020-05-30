import discord
from discord.ext import commands

client = discord.Client()

CHANNEL_ID = 987654321987654321 
CHANNEL_IDD = 704908660274364471


async def greet():
    channel = client.get_channel(CHANNEL_IDD)
    await channel.send('管理BOTは起動しました')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='稼働中'))
    await greet()

CHANNEL_ID = 713931338092118027
	
list = ["死ね","カス","キチガイ","基地外","くそ","ガキ" ]
 
@client.event
async def on_message(message):    
    for word in list:
      if message.author.bot:
       return
      if word in message.content:
        await message.delete()
        await message.channel.send(message.author.mention +"\n" + '現在のコメントは削除されました\n理由：スパム判定になりました。\n身に覚えがない場合は孤独のコーヒーまで')
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(message.author.mention+"\n" +" 削除されたコメント:" + word +"\n" +'コメントが削除されました\n誤作動の場合があります\n削除されたコメントを見ましょう\n誤作動の場合は削除されたコメントといっしょにコーヒーまで')







           
       

client.run("NzEyNTk3MjE4MzgwNzQyNjk5.Xs5LnA.uFPoETQqeNH1bMk8UkK_pZLJ3zY")
