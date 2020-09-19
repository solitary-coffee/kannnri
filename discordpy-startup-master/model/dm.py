import discord
from discord.ext import commands
ID = 637850681666961408

class dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None




    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def dm(self,ctx, *, naiyou):
        dm = self.bot.get_user(ID)
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

def setup(bot):
    return bot.add_cog(dm(bot))