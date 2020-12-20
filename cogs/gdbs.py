import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import command
import json 
import random
from random import choice
from datetime import datetime, timedelta



class GDBS(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.rate_channel = 766700804181852231
        self.command_channel = 766694495302975528



    @command()
    async def rate(self, ctx, level_id:int, stars:int, rate_type: str, *, name:str):
        try:
            if ctx.channel.id == self.command_channel:
                rates = ctx.guild.get_channel(self.rate_channel)

                if stars == 1:
                    rate_icon = '<:robot_dolbaeb:767291737437372446>'
                elif stars == 2:
                    rate_icon = '<:veseliy:767048784211345430>'
                elif stars == 3:
                    rate_icon = '<:normalno:767047776252592138>'
                elif stars == 4 or stars == 5:
                    rate_icon = '<:strashno:767056518901792769>'
                elif stars == 6 or stars == 7:
                    rate_icon = '<:zloy:767048070969163816>'
                elif stars == 8 or stars == 9:
                    rate_icon = '<:zloy_batya:767048139046649926>'

                if rate_type == 'rate':
                    rating = '<:rate_menu:767265798099959858> Rate  (1 <:cp:767054752961134643>)'
                elif rate_type == 'featured':
                    rating = '<a:rate_menu_gay:767054272528777217> Featured  (2 <:cp:767054752961134643>)'
                elif rate_type == 'epic':
                    rating = '<a:rate_menu_shakal:767054636438913045> Epic  (3 <:cp:767054752961134643>)'

                embed = discord.Embed(
                    title = '<:zvezda:767054247023345684> Уровень рейтнут!',
                    description = f'Модератор - {ctx.author}',
                    color = discord.Color.from_rgb(0,255,0)
                )
                embed.add_field(name='Название', value=f'{name}')
                embed.add_field(name='Оценка', value=f'{rate_icon} {stars}<:zvezda:767054247023345684>')
                embed.add_field(name='Тип оценки', value=f'{rating}')
                embed.set_footer(text=f'ID: {level_id}')

                await rates.send(embed=embed)

                log_embed = discord.Embed(
                    title = 'Отправлено!',
                    description = f'Параметры: {level_id}, {rate_icon} {stars}<:zvezda:767054247023345684>, {rating}, {name}',
                    color = ctx.author.color
                )

                await ctx.send(embed=log_embed)
        except Exception as e:
            print(e)



    @command()
    async def rerate(self, ctx, level_id:int, stars:int, rate_type: str, *, name:str):
        try:
            if ctx.channel.id == self.command_channel:
                rates = ctx.guild.get_channel(self.rate_channel)

                if stars == 1:
                    rate_icon = '<:robot_dolbaeb:767291737437372446>'
                elif stars == 2:
                    rate_icon = '<:veseliy:767048784211345430>'
                elif stars == 3:
                    rate_icon = '<:normalno:767047776252592138>'
                elif stars == 4 or stars == 5:
                    rate_icon = '<:strashno:767056518901792769>'
                elif stars == 6 or stars == 7:
                    rate_icon = '<:zloy:767048070969163816>'
                elif stars == 8 or stars == 9:
                    rate_icon = '<:zloy_batya:767048139046649926>'

                if rate_type == 'rate':
                    rating = '<:rate_menu:767265798099959858> Rate  (1 <:cp:767054752961134643>)'
                elif rate_type == 'featured':
                    rating = '<a:rate_menu_gay:767054272528777217> Featured  (2 <:cp:767054752961134643>)'
                elif rate_type == 'epic':
                    rating = '<a:rate_menu_shakal:767054636438913045> Epic  (3 <:cp:767054752961134643>)'

                embed = discord.Embed(
                    title = '<:zvezda:767054247023345684> Рейт изменён!',
                    description = f'Модератор - {ctx.author}',
                    color = discord.Color.gold()
                )
                embed.add_field(name='Название', value=f'{name}')
                embed.add_field(name='Новая оценка', value=f'{rate_icon} {stars}<:zvezda:767054247023345684>')
                embed.add_field(name='Тип оценки', value=f'{rating}')
                embed.set_footer(text=f'ID: {level_id}')

                await rates.send(embed=embed)

                log_embed = discord.Embed(
                    title = 'Отправлено!',
                    description = f'Параметры: {level_id}, {rate_icon} {stars}<:zvezda:767054247023345684>, {rating}, {name}',
                    color = ctx.author.color
                )

                await ctx.send(embed=log_embed)
        except Exception as e:
            print(e)


    @command()
    async def unrate(self, ctx, level_id:int, *, name:str):
        try:
            if ctx.channel.id == self.command_channel:
                rates = ctx.guild.get_channel(self.rate_channel)

                embed = discord.Embed(
                    title = '<:soboleznyu:767261750910910485> С уровня снят рейт...',
                    description = f'Модератор - {ctx.author}',
                    color = discord.Color.from_rgb(0,255,0)
                )
                embed.add_field(name='Название', value=f'{name}')
                embed.set_footer(text=f'id: {level_id}')

                await rates.send(embed=embed)

                log_embed = discord.Embed(
                    title = 'Отправлено!',
                    description = f'Параметры: {level_id}, {name}',
                    color = ctx.author.color
                )

                await ctx.send(embed=log_embed)
        except Exception as e:
            print(e)



    @command()
    async def demon(self, ctx, level_id:int, demon:str, rate_type: str, *, name:str):
        try:
            if ctx.channel.id == self.command_channel:
                rates = ctx.guild.get_channel(self.rate_channel)

                if demon == 'easy':
                    rate_icon = '<:dolbaeb:767048221049618433>'
                elif demon == 'medium':
                    rate_icon = '<:dolbaebx2:767048291438821396>'
                elif demon == 'hard':
                    rate_icon = '<:dolbaebx3:767048843895767100>'
                elif demon == 'insane':
                    rate_icon = '<:dolbaebx4:767049645523468298>'
                elif demon == 'extreme':
                    rate_icon = '<:dolbaebx5:767049815594237963>'

                if rate_type == 'rate':
                    rating = '<:rate_menu:767265798099959858> Rate  (1 <:cp:767054752961134643>)'
                elif rate_type == 'featured':
                    rating = '<a:rate_menu_gay:767054272528777217> Featured  (2 <:cp:767054752961134643>)'
                elif rate_type == 'epic':
                    rating = '<a:rate_menu_shakal:767054636438913045> Epic  (3 <:cp:767054752961134643>)'
                

                embed = discord.Embed(
                    title = '<:tupoy_dolbaeb_dymaet:767267135331500062> Новый демон!',
                    description = f'Модератор - {ctx.author}',
                    color = discord.Color.from_rgb(0,0,255)
                )
                embed.add_field(name='Название', value=f'{name}')
                embed.add_field(name='Оценка', value=f'{rate_icon} 10<:zvezda:767054247023345684>')
                embed.add_field(name='Тип оценки', value=f'{rating}')
                embed.set_footer(text=f'ID: {level_id}')

                await rates.send(embed=embed)

                log_embed = discord.Embed(
                    title = 'Отправлено!',
                    description = f'Параметры: {level_id}, {rate_icon} 10<:zvezda:767054247023345684>, {rating}, {name}',
                    color = ctx.author.color
                )

                await ctx.send(embed=log_embed)
        except Exception as e:
            print(e)


    @command()
    async def redemon(self, ctx, level_id:int, demon:str, rate_type: str, *, name:str):
        try:
            if ctx.channel.id == self.command_channel:
                rates = ctx.guild.get_channel(self.rate_channel)

                if demon == 'easy':
                    rate_icon = '<:dolbaeb:767048221049618433>'
                elif demon == 'medium':
                    rate_icon = '<:dolbaebx2:767048291438821396>'
                elif demon == 'hard':
                    rate_icon = '<:dolbaebx3:767048843895767100>'
                elif demon == 'insane':
                    rate_icon = '<:dolbaebx4:767049645523468298>'
                elif demon == 'extreme':
                    rate_icon = '<:dolbaebx5:767049815594237963>'

                if rate_type == 'rate':
                    rating = '<:rate_menu:767265798099959858> Rate  (1 <:cp:767054752961134643>)'
                elif rate_type == 'featured':
                    rating = '<a:rate_menu_gay:767054272528777217> Featured  (2 <:cp:767054752961134643>)'
                elif rate_type == 'epic':
                    rating = '<a:rate_menu_shakal:767054636438913045> Epic  (3 <:cp:767054752961134643>)'
                

                embed = discord.Embed(
                    title = '<:tupoy_dolbaeb_dymaet:767267135331500062> Изменена оценка демона!',
                    description = f'Модератор - {ctx.author}',
                    color = discord.Color.from_rgb(0,0,255)
                )
                embed.add_field(name='Название', value=f'{name}')
                embed.add_field(name='Новая оценка', value=f'{rate_icon} 10<:zvezda:767054247023345684>')
                embed.add_field(name='Тип оценки', value=f'{rating}')
                embed.set_footer(text=f'ID: {level_id}')

                await rates.send(embed=embed)

                log_embed = discord.Embed(
                    title = 'Отправлено!',
                    description = f'Параметры: {level_id}, {rate_icon} 10<:zvezda:767054247023345684>, {rating}, {name}',
                    color = ctx.author.color
                )

                await ctx.send(embed=log_embed)
        except Exception as e:
            print(e)


    @command()
    async def vote(self, ctx):
        embed = discord.Embed(
            ttile = 'Помощь серверу',
            description = 'Что бы помочь нам и бесплатно получить роль <@&770265071887581206>:\n\n - Перейдите по этой ссылке https://top.gg/servers/766330409704882196/vote;\n - авторизуйтесь;\n - нажмите кнопку Vote!',
            color = ctx.author.color
        )
        await ctx.send(embed=embed)


    @command(name='заявка')
    async def this_is(self, ctx):
        this = discord.Embed(
            title = 'Заполните заявку по этой форме',
            description = '1. Ваш возраст, и как к вам можно обращаться?\n2. Были ли вы хоть когда нибудь модератором в других приватных серверах? Если да, то где?.\n3. Сколько времени в неделю вы будете уделять модерированию?\n4. Оцените себя по шкале от 1 до 10, на сколько вы опытны и ответственны в модерировании приватных серверов.',
            color = discord.Color.from_rgb(0,255,0)
        )
        this.add_field(name='Для заполнения формы пропишите команду', value='`>подать-заявку [ваша форма]`\n\nЗаявка заполняется строго по форме, и как только будет вынесено решение, вам лично придет ответ.')
        try:
            await ctx.author.send(embed=this)
        except:
            await ctx.send('Не могу отправить вам сообщение. Убедитесь, что у вас доступны личные сообщения.')
        await ctx.message.delete()

    @command(name='подать-заявку')
    async def is_modapply(self, ctx, *, apply_info: str):
        if ctx.channel.type == discord.ChannelType.private:
            channel = self.client.get_channel(782944336614260737)
            embed = discord.Embed(
                title = 'Заявка на модератора',
                description = apply_info,
                color = discord.Color.from_rgb(255,0,0)
            )
            await channel.send(content=ctx.author, embed=embed)
            await ctx.send('Заявка отправлена :white_check_mark:')
        else:
            await ctx.send(':x: Заявку можно подать только в личных сообщениях с ботом.')

        
    @command()
    async def modapply(self, ctx, member: discord.Member, acc: str):
        if ctx.author.id == 616691484057534465 or ctx.author.id == 647735617496547330:
            if acc == 'accept':
                try:
                    await member.add_roles(ctx.guild.get_role(766349938991824939))
                    embed = discord.Embed(
                        description = ':white_check_mark: Ваша заявка на модератора была принята, перейдите в канал <#766694495302975528> для получения всей информации.'
                    )
                    await member.send(embed=embed)
                    await ctx.send(f'{member} принят в модераторы!')

                except Exception as e:
                    await ctx.send(f'Произошла ошибка: {e}')

            elif acc == 'reduse':
                try:
                    embed = discord.Embed(
                        description = ':x: К сожалению, ваша заявка была отклонена.'
                    )
                    await member.send(embed=embed)
                    await ctx.send('Сообщение об отклонении отправлено.')

                except Exception as e:
                    await ctx.send(f'Произошла ошибка: {e}')


    

    @command(name='анонимная-история', aliases=['анонимная_история'])
    @commands.cooldown(1, 61, commands.BucketType.user)
    async def anon_story(self, ctx, *, story: str):
        if ctx.channel.type == discord.ChannelType.private:
            stories_channel = self.client.get_channel(784099291344928818)

            embed = discord.Embed(
                title = 'Анонимная история',
                description = story,
                timestamp = datetime.now()
            )
            await stories_channel.send(embed=embed)
            await ctx.send(':white_check_mark: Ваша история отправлена')
        else:
            await ctx.send(embed=discord.Embed(description=':x: Данная команда доступна только в личных сообщениях'))











def setup(client):
    client.add_cog(GDBS(client))
