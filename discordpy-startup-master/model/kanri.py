import discord
from discord.ext import commands
import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
ID = 637850681666961408

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def kt(self,ctx, *,kasutamu):
        if ctx.message.author.id == ID:    
            await self.bot.change_presence(activity=discord.Game(name=kasutamu))
        else:
            await ctx.send("このコマンドは管理者専用です")

    @commands.command(name='eval')
    async def _eval(self,ctx, *, body):
        if ctx.message.author.id == ID:    
            blocked_words = [ 'os', 'subprocess', 'history()', '("token")', "('token')",
                        'aW1wb3J0IG9zCnJldHVybiBvcy5lbnZpcm9uLmdldCgndG9rZW4nKQ==', 'aW1wb3J0IG9zCnByaW50KG9zLmVudmlyb24uZ2V0KCd0b2tlbicpKQ==']
            if ctx.author.id != self.bot.owner_id:
                for x in blocked_words:
                    if x in body:
                        return await ctx.send('Your code contains certain blocked words.')
            env = {
                'ctx': ctx,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
                'source': inspect.getsource
            }

            env.update(globals())

            body = self.cleanup_code(body)
            stdout = io.StringIO()
            err = out = None

            to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

            def paginate(text: str):
                '''Simple generator that paginates text.'''
                last = 0
                pages = []
                for curr in range(0, len(text)):
                    if curr % 1980 == 0:
                        pages.append(text[last:curr])
                        last = curr
                        appd_index = curr
                if appd_index != len(text)-1:
                    pages.append(text[last:curr])
                return list(filter(lambda a: a != '', pages))
    
            try:
                exec(to_compile, env)
            except Exception as e:
                err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
                return await ctx.message.add_reaction('\u2049')

            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
            else:
                value = stdout.getvalue()
                if ret is None:
                    if value:
                        try:
                    
                            out = await ctx.send(f'```py\n{value}\n```')
                        except:
                            paginated_text = paginate(value)
                            for page in paginated_text:
                                if page == paginated_text[-1]:
                                    out = await ctx.send(f'```py\n{page}\n```')
                                    break
                                await ctx.send(f'```py\n{page}\n```')
                else:
                    self.bot._last_result = ret
                    try:
                        out = await ctx.send(f'```py\n{value}{ret}\n```')
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            try:
                if out:
                    await ctx.message.add_reaction('\u2705')  # tick
                elif err:
                    await ctx.message.add_reaction('\u2049')  # x
                else:
                    await ctx.message.add_reaction('\u2705')
            except:
                await ctx.send("コマンドメッセージが見つかりません")
                await asyncio.sleep(10)
        else: 
            await ctx.send("管理者のみ利用可能")
        
    def cleanup_code(self,content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self,e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'


def setup(bot):
    return bot.add_cog(Greetings(bot))
