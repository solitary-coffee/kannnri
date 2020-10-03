import discord
from discord.ext import commands
ID = 637850681666961408


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    class MemberRoles(commands.MemberConverter):
        async def convert(self, ctx, argument):
            member = await super().convert(ctx, argument)

            return [role.name for role in member.roles[1:]]
    @commands.command()
    async def j(self,ctx, *, member: discord.Member):
        await ctx.send('{0} 入室履歴: {0.joined_at}' .format(member))

    @commands.command()
    async def r(self,ctx, *, member: MemberRoles ):
        """Tells you a member's roles."""
        await ctx.send('ロール: ' + ', '.join(member))

    @commands.command()
    async def ke(self,ctx,*,ss):
        await ctx.message.delete()
        await ctx.send(ss)  

    @commands.command()
    async def em(self,ctx, a,*, b):
        embed=discord.Embed(title= a,description= b, color=0xdc0909)
        embed.add_field(name= "**AMIKU 関連ー**", value= "[公式サーバー](https://discord.gg/GWrvMT4)　\n [導入リンク](https://discord.com/api/oauth2/authorize?client_id=712597218380742699&permissions=808512560&scope=bot)", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ban(ctx, member: discord.Member, *, reason=None):    
        if ctx.message.author.id == ID:    
            await member.ban(reason=reason)
            embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"BANが成功しました:{member.mention}",color=0xff0000)
            embed.add_field (name=f"ID:{member.id}", value=f"ＢＡＮ理由：{reason}", inline=False)
            await ctx.send (embed=embed)


        elif ctx.message.author.guild_permissions.administrator:   
            await member.ban(reason=reason)
            embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"BANが成功しました:{member.mention}",color=0xff0000)
            embed.add_field (name=f"ID:{member.id}", value=f"ＢＡＮ理由：{reason}", inline=False)
            await ctx.send (embed=embed) 

    @commands.command()
    async def kick(ctx, member: discord.Member, *, reason=None):    
        if ctx.message.author.id == ID:    
            await member.ban(reason=reason)
            embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"kickが成功しました:{member.mention}",color=0xff0000)
            embed.add_field (name=f"ID:{member.id}", value=f"Kick理由：{reason}", inline=False)
            await ctx.send (embed=embed)


        elif ctx.message.author.guild_permissions.administrator:   
            await member.ban(reason=reason)
            embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"kickが成功しました:{member.mention}",color=0xff0000)
            embed.add_field (name=f"ID:{member.id}", value=f"kick理由：{reason}", inline=False)
            await ctx.send (embed=embed) 
      
        else:
            await ctx.send("このコマンドは管理者専用です")




def setup(bot):
    return bot.add_cog(Greetings(bot))
