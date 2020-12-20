import asyncio
import discord
from discord.ext import commands
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Reacts(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.relations = {}
        self.relations_au = {}

        self.sxs = {}
        self.sxs_au = {}

    @commands.command(aliases=['обнять'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def hug(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            embed = discord.Embed(
            title = 'Обнимашки',
            description = f'{ctx.author.mention} обнимает себя :heart:',
            color = ctx.author.color,
            timestamp = datetime.now()
        )
        else:
            embed = discord.Embed(
                title = 'Обнимашки',
                description = f'{ctx.author.mention} обнимает {member.mention} :heart:',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
        images = ['https://cdn.discordapp.com/attachments/640586936301387787/752890112441974784/171021_2147.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752889653107097620/c5365d892718425ea58371b8d4e6fc64e29f6902_hq.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752889654151479296/8X6d.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752889653857878046/orig_1.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/760219136117964850/anime-love-28.gif']
        embed.set_image(url=choice(images))
        await ctx.send(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)


    @commands.command(aliases=['обида', 'обидеться'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def offend(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            embed = discord.Embed(
            title = 'Обида',
            description = f'{ctx.author.mention} обиделся на себя :pensive:',
            color = ctx.author.color,
            timestamp = datetime.now()
        )
        else:
            embed = discord.Embed(
                title = 'Обида',
                description = f'{ctx.author.mention} обиделся на {member.mention} :pensive:',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
        images = ['https://cdn.discordapp.com/attachments/646341217013202990/752867153434378250/tenor_8.gif',
        'https://cdn.discordapp.com/attachments/646341217013202990/752867153207754822/tenor_7.gif']
        embed.set_image(url=choice(images))
        await ctx.send(embed=embed)

    @offend.error
    async def offend_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)

    @commands.command(aliases=['поцеловать', 'поцелуй'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def kiss(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            embed = discord.Embed(
            title = 'Поцелуй',
            description = f'{ctx.author.mention} хз как, но целует себя :heart:',
            color = ctx.author.color,
            timestamp = datetime.now()
        )
        else:
            embed = discord.Embed(
                title = 'Поцелуй',
                description = f'{ctx.author.mention} целует {member.mention} :heart:',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
        images = ['https://cdn.discordapp.com/attachments/640586936301387787/752890476457230366/e4454f593497f54817bd2466845cfe9e749780f4_hq.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752890476851626024/99c41869ba1551575aefd9c8ffc533de.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752890477342097448/anime-gif-kiss-4.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/760214606768504892/99px_ru_animacii_25931_misaki_takasaki__misaki_takasaki_celuet_yukari_nejima.gif',
        'https://cdn.discordapp.com/attachments/646341217013202990/752866013875404931/SAVE_20200908_152002.jpg',
        'https://cdn.discordapp.com/attachments/646341217013202990/752867094508339281/tenor_1.gif',
        'https://cdn.discordapp.com/attachments/646341217013202990/752867151982886963/tenor_3.gif']
        embed.set_image(url=choice(images))
        await ctx.send(embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)

    @commands.command(aliases=['пощечина', 'пощёчина', 'ударить'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def slap(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            embed = discord.Embed(
            title = 'Пощёчина',
            description = f'{ctx.author.mention} бьёт по щеке себя!',
            color = ctx.author.color,
            timestamp = datetime.now()
        )
        else:
            embed = discord.Embed(
                title = 'Пощёчина',
                description = f'{ctx.author.mention} бьёт по щеке {member.mention}!',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
        images = ['https://cdn.discordapp.com/attachments/646341217013202990/752867152729735248/tenor_5.gif',
        'https://cdn.discordapp.com/attachments/646341217013202990/752867152985325658/tenor_6.gif',
        'https://cdn.discordapp.com/attachments/640586936301387787/752891159512088717/Tumblr_mrbvwpBu2E1spbtxxo1_500.gif']
        embed.set_image(url=choice(images))
        await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)

    @commands.command(aliases=['сенпай_не_делай_этого'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def senpai_dont_do_it(self, ctx, member: discord.Member = None):
        if member == None or member == ctx.author:
            embed = discord.Embed(
            title = 'Изнасилование',
            description = f'{ctx.author.mention} насилует себя!',
            color = ctx.author.color,
            timestamp = datetime.now()
        )
        else:
            embed = discord.Embed(
                title = 'Изнасилование',
                description = f'{ctx.author.mention} насилует {member.mention}!',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
        images = []
        embed.set_image(url=choice(images))
        await ctx.send(embed=embed)

    @senpai_dont_do_it.error
    async def senpai_dont_do_it_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)



    @commands.command(aliases=['отношения'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def relation(self, ctx, member: discord.Member = None):
        if member == ctx.author:
            await ctx.send('Ну это уже слишком, предлагать себе встречаться... Как самовлюблённо.')
        elif member == None:
            await ctx.send('Выбери кому встречаться предлагаешь хоть :/')
        else:
            embed = discord.Embed(
                title = 'Отношения',
                description = f'{ctx.author.mention} предлагает встречаться {member.mention} :heart: :heart: :heart:',
                color = ctx.author.color,
                timestamp = datetime.now()
            )
            
            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            
            self.relations.update({str(message.id): member.id})
            self.relations_au.update({str(message.id): ctx.author.id})
            

    @relation.error
    async def relation_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.delete()
            msg = await ctx.send(f'{ctx.message.author.mention}, кулдаун для этой команды - 5 секунд.')
            await msg.delete(3)



    @commands.command(aliases=['секс'])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def sex(self, ctx, member: discord.Member = None):
        
        if member == ctx.author or member == None:
            embed = discord.Embed(
            title = 'Секс',
            description = f'{ctx.author.mention}, нельзя заниматься этим с самим собой :>',
            color = ctx.author.color,
            timestamp = datetime.now()
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                description = f'{ctx.author.mention} предлагает заняться сексом {member.mention}!',
                color = ctx.author.color,
                timestamp = datetime.now()
            )

            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            try:
                self.sxs.update({str(message.id): member.id})
                self.sxs_au.update({str(message.id): ctx.author.id})
            except Exception as e:
                await ctx.send(e)
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        
        try:
            msg = await reaction.message.channel.fetch_message(reaction.message.id)
            
            if str(msg.id) in self.sxs.keys():
                
                if user.id in self.sxs.values():
                    msg_author = user.guild.get_member(self.sxs_au[str(msg.id)])
                    

                    if str(reaction) == '✅':
                        

                        embed = discord.Embed(
                            title = 'Cекс',
                            description = f'{msg_author.mention} и {user.mention} занялись сексом! :heart:',
                            color = user.color,
                            timestamp = datetime.utcnow()
                        )
                        images = ['https://cdn.discordapp.com/attachments/640586936301387787/759675505728290873/1384353032_1585294803.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/759675505376755762/94cbee09697d30a4a6f87fb77b653bacbceb621e_hq.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/759673553599201310/Anime--Anime-Nisemonogatari-Hachikuji-Mayoi-1472773.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/759676231863238673/imouto-paradise--Anime---952660.gif']
                        embed.set_image(url = choice(images))

                        del self.sxs[str(msg.id)]
                        await msg.edit(embed=embed)
                        await msg.clear_reactions()
                    
                    elif str(reaction) == '❌':
                        
                        embed = discord.Embed(
                            title = 'Cекс',
                            description = f'{msg_author.mention}, {user.mention} отказывается от секса с вами.',
                            color = discord.Color.red(),
                            timestamp = datetime.utcnow()
                        )
                        del self.sxs[str(msg.id)]
                        await msg.edit(embed=embed)
                        await msg.clear_reactions()

        # -----------------------------------------------------------------------------------------------------
            
            if str(msg.id) in self.relations.keys():
                
                if user.id in self.relations.values():
                    msg_author = user.guild.get_member(self.relations_au[str(msg.id)])
                    

                    if str(reaction) == '✅':
                        

                        embed = discord.Embed(
                            title = 'Отношения',
                            description = f'{user.mention} принимает предожение встречаться от {msg_author.mention}! :heart:',
                            color = user.color,
                            timestamp = datetime.utcnow()
                        )
                        images = ['https://cdn.discordapp.com/attachments/640586936301387787/760213610327703662/TestyLiveAsianwaterbuffalo-size_restricted.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/760216399565815838/500x292_0xac120002_17472146771540471599.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/760217586058264606/anime-love-5.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/760218261710307368/anime-love-44.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/760219136575668304/anime-love-56.gif',
                        'https://cdn.discordapp.com/attachments/640586936301387787/760219136931790928/anime-love-11.gif']
                        embed.set_image(url = choice(images))

                        del self.relations[str(msg.id)]
                        await msg.edit(embed=embed)
                        await msg.clear_reactions()
                    
                    elif str(reaction) == '❌':
                        
                        embed = discord.Embed(
                            title = 'Отношения',
                            description = f'{msg_author.mention}, похоже {user.mention} отказывается встречаться с вами. :broken_heart:',
                            color = discord.Color.red(),
                            timestamp = datetime.utcnow()
                        )
                        del self.relations[str(msg.id)]
                        await msg.edit(embed=embed)
                        await msg.clear_reactions()

        except Exception as e:
            await reaction.message.channel.send(e)



    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        pass










def setup(client):
    client.add_cog(Reacts(client))
