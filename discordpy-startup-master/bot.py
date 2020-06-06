import discord
import rog
from discord.ext import commands


client = discord.Client()

CHANNEL_ID = 987654321987654321 
CHANNEL_IDD = 704908660274364471


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='稼働中'))


CHANNEL_ID = 709606780631777360
	
@client.event
async def on_message(message):  
    if message.content == '/list':
      await message.channel.send(rog.list) 
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






           
client.run("NzEyNTk3MjE4MzgwNzQyNjk5.XtMLNw.tbWatTcfovhYmVd7yKSaS6RoULg")

           
       

