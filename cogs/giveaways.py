import asyncio
import discord
from discord.ext import commands 
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Giveaways(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.g = {}
        self.g_authors = []
        self.reroll_members = {}
        self.ended_g = {}

    def isauthor(self, ctx):
        return ctx.auhtor.id in self.g_authors


    @commands.command(aliases=['gw', 'g', 'розыгрыш'])
    async def giveaway(self, ctx, _time: int, time_type: str, *, prize: str):
        if ctx.author.id == 616691484057534465 or ctx.author.id == 647735617496547330:
            if time_type == 's':
                pass
            

            if time_type == 'm':
                _time *= 60
            

            if time_type == 'h':
                _time *= 3600
            

            if time_type == 'd':
                _time *= 86400
            

            embed = discord.Embed(
                title = ':tada: Розыгрыш!',
                description = f'{prize}\n\nАвтор - {ctx.author.mention}\nЧто бы учавстовать нажмите на 🎊',
                color = self.client.user.color,
                timestamp = datetime.utcnow() + timedelta(seconds=_time)
            )
            embed.set_footer(text='Итоги')

            message = await ctx.send(embed=embed)
            await message.add_reaction('🎊')

            self.g.update({str(message.id): prize})
            self.g_authors.append(ctx.author.id)

            await asyncio.sleep(_time)

            try:
                ch_message = await message.channel.fetch_message(message.id)
                reactions = ch_message.reactions
                users = await reactions[0].users().flatten()

                if str(message.id) in self.g:

                    if len(users) > 1:

                        users.remove(users[0])
                        self.reroll_members.update({str(message.id): users.copy()})
                        winner = choice(users)

                        await message.channel.send(f':tada:Поздравляю {winner.mention}, ты выигрываешь **{prize}**!')

                        self.ended_g.update({str(message.id): prize})
                        del self.g[str(message.id)]
                    else:
                        await message.channel.send('Никто не выиграл, т.к. никто не учавствовал. :pensive:')

                else:
                    pass
            except Exception as e:
                await ctx.send(e)


    @commands.command(aliases=['енд', 'закончить'])
    @commands.check(commands.has_permissions(manage_guild=True or isauthor))
    async def end(self, ctx, g: int):
        if ctx.author.id == 616691484057534465 or ctx.author.id == 647735617496547330:
            try:

                if str(g) in self.g:

                    msg = await ctx.fetch_message(g)
                    reactions = msg.reactions
                    users = await reactions[0].users().flatten()
                    users.remove(users[0])

                    self.reroll_members.update({str(g): users.copy()})

                    winner = choice(users)
                    await ctx.send(f':tada:Поздравляю {winner.mention}, ты выигрываешь {self.g[str(g)]}')

                    self.ended_g.update({str(g): self.g[str(g)]})
                    del self.g[str(g)]

                else:
                    await ctx.send('Не могу досрочно закончить розыгрыш.')

            except Exception as e:
                print(e)


    @commands.command(aliases=['реролл'])
    @commands.check(commands.has_permissions(manage_guild=True or isauthor))
    async def reroll(self, ctx, g: int, islast: str = None):
        if ctx.author.id == 616691484057534465 or ctx.author.id == 647735617496547330:
            try:
                if not len(self.reroll_members[str(g)]) < 1:
                    if str(g) in self.ended_g:

                        if islast == None:

                            winner = choice(self.reroll_members[str(g)])
                            await ctx.send(f':tada:Новый победитель - {winner.mention}, он выигрывает {self.ended_g[str(g)]}!')

                        if islast == 'last':

                            try:
                                
                                winner = choice(self.reroll_members[str(g)])
                                await ctx.send(f':tada:Новый победитель - {winner.mention}, он выигрывает {self.ended_g[str(g)]}!')

                                del self.g[str(g)]
                                self.g_authors.remove(ctx.author.id)
                                del self.reroll_members[str(g)]
                                del self.ended_g[str(g)]

                            except:
                                pass
                    else:
                        await ctx.send('В данный момент реролл недоступен.')
            except Exception as e:
                print(e)


    # @commands.command(aliases=['gsettings', 'gs', 'настройки'])
    # @commands.check(commands.has_permissions(manage_guild=True or isauthor))
    # async def g_settings(self, ctx, g: int, settings: str = None):
    #     if settings == 'static':
    #         del self.g[str(g)]
    #         del self.ended_g[str(g)]
    #         await ctx.send('Настройки: no_reroll, no_early_end.')

    #     elif settings == 'no_reroll':
    #         del self.ended_g[str(g)]
    #         await ctx.send('Настройки: no_reroll.')

    #     elif settings == 'no_end':
    #         del self.g[str(g)]
    #         await ctx.send('Настройки: no_early_end')

    #     else:
    #         await ctx.send('err: Настройки указаны неверно.')
        
        
        



def setup(client):
    client.add_cog(Giveaways(client))
