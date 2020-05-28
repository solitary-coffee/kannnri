import discord
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='稼働中'))

CHANNEL_ID = 709606780631777360
	
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
