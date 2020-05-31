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
    for word in rog.list:
      if message.author.bot:
        return
      if word in message.content:
        await message.delete()
        embed=discord.Embed(title="現在のコメントは削除されました",description=message.author.mention, color=0xdc0909)
        embed.add_field(name="削除されたコメント:", value= word, inline=True)
        embed.add_field(name="理由：", value="現在のコメントは暴言にあたります", inline=True)
        embed.add_field(name="その他", value="意図しないで削除された場合は削除されたコメントと全文を孤独のコーヒーまでお願いします", inline=False)
      

        await message.channel.send(message.author.mention)
        await message.channel.send(embed=embed) 
     







           
client.run("NzEyODE3NDcxOTIwMjc1NTA2.Xszqbg.hLOUi_FKlPK6XgDsXjn-C1wIzk4")

           
       

