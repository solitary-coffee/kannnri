import discord
from discord.ext import commands

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
        await ctx.send(embed=embed)



def setup(bot):
    return bot.add_cog(Greetings(bot))