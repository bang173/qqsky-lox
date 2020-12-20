import discord
from discord import __version__ as discord_version
from discord.utils import get
import random
import time
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
from psutil import Process, virtual_memory
from platform import python_version
import typing
import asyncio
import datetime
from datetime import timedelta
import inspect
from Cybernator import Paginator as pages



client = commands.Bot(command_prefix = '>', intents=discord.Intents.all())

status = cycle(['В разработке | >help'])

def isitme(ctx):
    return ctx.author.id == 616691484057534465 or ctx.author.id == 647735617496547330

def is_guild_owner(ctx):
    return ctx.author.id == ctx.guild.owner_id

client.remove_command('help')

@client.event
async def on_ready():
    change_status.start()
    print('Bot run. \n \n Logs:')
    channel = client.get_channel(783038231025156136)
    await channel.send(embed=discord.Embed(description=':white_check_mark: Bot restarted'))

# @client.event
# async def on_disconnect():
    # channel = client.get_channel(783038231025156136)
    # await channel.send(embed=discord.Embed(description=':x: Bot stopped'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('err: Аргументы указаны неверно.')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('err: Отсутствует необходимый аргумент.')
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'err: Команда сейчас на кулдауне.')

@client.event
async def on_guild_join(guild: discord.Guild):
    print(f'joined to guild "{guild.name}"')

@client.event
async def on_guild_remove(guild: discord.Guild):
    print(f'removed from guild "{guild.name}"')
    
    
@client.command(aliases = ['stats', 'стат', 'стата', 'статистика'])
async def stat(ctx):
    try:
        embed = discord.Embed(
            title = 'Статистика бота',
            color = ctx.author.color,
            timestamp = datetime.datetime.now(),
            thumbnail = client.user.avatar_url
        )
        proc = Process()
        with proc.oneshot():
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            mem_usage = mem_total * (mem_of_total / 100)

        fields = [
            ('discord.py - версия', discord_version, True),
            ('Использование памяти', f'{mem_usage:,.3f} МБ / {mem_total:,.0f} МБ ({mem_of_total:.0f}%)', True),
            ('Пинг', f'`{round(client.latency*1000)}` ms', True)
        ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(e)
    

@client.command(aliases=['хелп', 'помощь'])
async def help(ctx):

    em = discord.Embed(
        title = 'Помощь',
        description = 'Основной префикс - >',
        color = discord.Color.blurple()
    )
    em.add_field(name='Все команды имеют русский аналог, который указан в скобках перед командой', value='В том числе и эта команда: `>хелп`, `>помощь`')
    


    em1 = discord.Embed(
        title = 'Команды модерации',
        color = discord.Color.blurple()
    )
    em1.add_field(name='(`кик`)`kick @участник [причина]`', value='```Выгоняет участника```')
    em1.add_field(name='(`бан`)`ban @участник [причина]`', value='```Банит участника```')
    em1.add_field(name='(`очистить`)`purge [кол-во]`', value='```Удаляет указанное количество сообщений в текущем канале```')
    

    em2 = discord.Embed(
        title = 'Информационные команды',
        color = discord.Color.blurple()
    )
    em2.add_field(name='(`юзер`, `пользователь`)`user @участник(необяз.)`', value='```Показывает информацию о пользователе```')
    em2.add_field(name='(`сервер`)`server`', value='```Показывает информацию о сервере```')
    em2.add_field(name='(`стата`)`stats`', value='```Статистика бота```')
    

    em3 = discord.Embed(
        title = 'Развлекательные команды',
        color = discord.Color.blurple()
    )
    em3.add_field(name='(`секс`)`sex @участник`', value='```Предложить @участнику заняться сексом```')
    em3.add_field(name='(`обнять`)`hug @участник`', value='```Обнять @участника```')
    em3.add_field(name='(`поцелуй`, `поцеловать`)`kiss @участник`', value='```Поцеловать @участника```')
    em3.add_field(name='(`обида`)`offend @участник`', value='```Обидеться на кого-то```')
    em3.add_field(name='(`пощечина`, `ударить`)`slap @участник`', value='```Дать пощёчину @участнику```')
    em3.add_field(name='(`отношения`)`relation @участник`', value='```Предложить встречаться @участнику```')
    em3.add_field(name='(`выбрать`)`choose [1 вариант] [2 вариант]`', value='```Выбирает между первым или вторым вариантом.```')
    

    em4 = discord.Embed(
        title = 'Утилиты',
        color = discord.Color.blurple()
    )
    em4.add_field(name='(`голосование`)`poll "Заголовок" {"Варианты выбора"}`', value='```Устроить голосование\nПример: >poll "Что сегодня поесть?" "Купи пельмени и поешь" "Говяжий дошик" и т.д.```')

    em5 = discord.Embed(
        ttile = 'Коллабы',
        color = discord.Color.blurple()
    )
    em5.add_field(name='(`новый-коллаб`)`new-collab [название без пробелов] {@участники-коллаба}`', value='**Команду можно использовать только 1 раз в день!**\nСоздать отдельный канал для какого либо коллаба.')
    em5.add_field(name='(`закончить-коллаб`)`end-collab`', value='Завершить коллаб и удалить канал с вашим коллабом.')


    embeds = [em, em1, em2, em3, em4, em5]
    message = await ctx.send(embed=em)
    pager = pages(client, message, only=ctx.author, delete_message=True, footer_icon=ctx.author.avatar_url, timeout=120, use_more=False, use_exit=True, exit_reaction=['❌'], reactions = ['◀', '▶'], embeds=embeds)
    await pager.start()


@client.command(aliases=['бан'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str):
    if ctx.guild.id == 650023366220316702:
        channel = client.get_channel(752176340186431488)
        await member.ban(reason=reason)
        em = discord.Embed(
            title = 'Бан',
            description = f'{member.mention} забанен по причине `{reason}`',
            color = discord.Color.dark_red()
        )
        await ctx.send(embed=em)
        embed = discord.Embed(
            title = 'Бан',
            description = f'{member.mention} забанен по причине `{reason}`\nЗабанил {ctx.author.mention}',
            color = discord.Color.dark_red(),
            timestamp = ctx.message.created_at
        )
        await channel.send(embed=embed)
    else:
        await member.ban(reason=reason)
        em = discord.Embed(
            title = 'Бан',
            description = f'{member.mention} забанен по причине `{reason}`',
            color = discord.Color.dark_red()
        )
        await ctx.send(embed=em)


@client.command(aliases=['кик'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str):
    if ctx.guild.id == 650023366220316702:
        channel = client.get_channel(752176340186431488)
        await member.kick(reason=reason)
        em = discord.Embed(
            title = 'Кик',
            description = f'{member.mention} выгнан по причине `{reason}`',
            color = discord.Color.dark_blue()
        )
        await ctx.send(embed=em)
        embed = discord.Embed(
            title = 'Кик',
            description = f'{member.mention} выгнан по причине `{reason}`\nВыгнал {ctx.author.mention}',
            color = discord.Color.dark_blue(),
            timestamp = ctx.message.created_at
        )
        await channel.send(embed=embed)
    else:
        await member.kick(reason=reason)
        em = discord.Embed(
            title = 'Кик',
            description = f'{member.mention} выгнан по причине `{reason}`',
            color = discord.Color.dark_blue()
        )
        await ctx.send(embed=em)




@client.command(aliases=['очистить'])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if ctx.guild.id == 650023366220316702:
        channel = client.get_channel(752176340186431488)
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title = 'Очистка сообщений',
            description = f'Пользователь {ctx.author.mention} очистил {amount} сообщений в канале {ctx.channel.mention}',
            color = discord.Color.dark_orange()
        )
        await channel.send(embed=embed)
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Проведена очистка {amount} сообщений.')


@client.command(aliases=['юзер', 'пользователь', 'юсер'])
async def user(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    embed = discord.Embed(
        colour = discord.Color.dark_purple(),
    )
    embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name='Участник', value=f'**{member}**', inline=True)

    if f'{member.status}' == 'online':
        embed.add_field(name='Статус', value='Онлайн', inline=True)
    elif f'{member.status}' == 'offline':
        embed.add_field(name='Статус', value='Оффлайн', inline=True)
    elif f'{member.status}' == 'idle':
        embed.add_field(name='Статус', value='Неактивен', inline=True)
    elif f'{member.status}' == 'dnd':
        embed.add_field(name='Статус', value='Не беспокоить', inline=True)
    elif f'{member.status}' == 'invisible':
        embed.add_field(name='Статус', value='Невидимка', inline=True)
    
    embed.add_field(name='Присоединился к Discord', value=member.created_at.strftime('***%a, %#d %B %Y, %I:%M %p UTC***'), inline=True)
    embed.add_field(name='Присоединился к серверу', value=member.joined_at.strftime('***%a, %#d %B %Y, %I:%M %p UTC***'), inline=True)
    embed.add_field(name=f'Кол-во ролей - **{len(roles)}**   Список:', value='       '.join([role.mention for role in roles][::-1]), inline=True)
    await ctx.send(embed=embed)


@client.command(aliases=['сервер'])
async def server(ctx, guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    embed = discord.Embed(
        title = f'{guild.name}',
        colour = discord.Colour.dark_purple(),
        timestamp = ctx.message.created_at
    )
    embed.set_author(name='Информация о сервере')

    if guild.region == discord.VoiceRegion.russia:
        embed.add_field(name='**Регион**', value='Россия', inline=True)
    elif guild.region == discord.VoiceRegion.europe:
        embed.add_field(name='**Регион**', value='Европа', inline=True)
    elif guild.region == discord.VoiceRegion.japan:
        embed.add_field(name='**Регион**', value='Япония', inline=True)
    elif guild.region == discord.VoiceRegion.london:
        embed.add_field(name='**Регион**', value='Лондон(Великобритания)', inline=True)
    

    if guild.verification_level == discord.VerificationLevel.none:
        embed.add_field(name='**Уровень верификации(модерации)**', value='Нет верицикации', inline=True)
    elif guild.verification_level == discord.VerificationLevel.low:
        embed.add_field(name='**Уровень верификации(модерации)**', value='Низкий', inline=True)
    elif guild.verification_level == discord.VerificationLevel.medium:
        embed.add_field(name='**Уровень верификации(модерации)**', value='Средний', inline=True)
    elif guild.verification_level == discord.VerificationLevel.high:
        embed.add_field(name='**Уровень верификации(модерации)**', value='Высокий', inline=True)
    elif guild.verification_level == discord.VerificationLevel.extreme:
        embed.add_field(name='**Уровень верификации(модерации)**', value='Экстримальный', inline=True)
    

    if guild.default_notifications == discord.NotificationLevel.all_messages:
        embed.add_field(name='**Уведомления по умолчанию**', value='Все сообщения', inline=True)
    elif guild.default_notifications == discord.NotificationLevel.only_mentions:
        embed.add_field(name='**Уведомления по умолчанию**', value='Только @упoминания', inline=True)

    embed.add_field(name='**Уровень буста**', value=guild.premium_tier, inline=True)
    embed.add_field(name='**Лимит отправки файлов(байт)**', value=guild.filesize_limit, inline=True)
    embed.add_field(name='**Владелец**', value=f'***{guild.owner}***', inline=True)
    embed.add_field(name='**Количество участников**', value=guild.member_count, inline=True)
    embed.add_field(name='**Сервер создан**', value=guild.created_at.strftime('***%a, %#d %B %Y, %I:%M %p UTC***'), inline=True)
    embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=['выбрать'])
async def choose(ctx, arg1: str, arg2: str):
    choise = random.choice([f'{arg1}', f'{arg2}'])
    embed = discord.Embed(
        description = f'**{arg1}** или **{arg2}**?\n\nМне кажется ***{choise}***',
        color = discord.Color.green()
    )
    await ctx.send(embed=embed)

@client.command(aliases=['репорт'])
@commands.cooldown(1, 300, commands.BucketType.member)
async def report(ctx, member: discord.Member, *, reason: str):
    if ctx.guild.id == 650023366220316702:
        channel = client.get_channel(752181454062092418)
        await ctx.send('Репорт отправлен. Подождите когда его рассмотрят.')
        embed = discord.Embed(
            title = 'Репорт',
            description = f'Поступила жалоба на {member.mention}\nСодержание: `{reason}`\n\nрепорт от {ctx.author.mention} в канале {ctx.channel.mention}'
        )
        await channel.send(embed=embed)
    else:
        await ctx.send('err: Данная команда недоступна на этом сервере.')
   
@client.command(aliases=['полл', 'голосование'])
async def poll(ctx, title: str, *fields):
    if len(fields) > 10:
        await ctx.send('err: Больше 10 строк нельзя')
    else:
        try:
            field_reacts = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

            embed = discord.Embed(
                description = f'Автор - {ctx.author.mention}',
                color = ctx.author.color,
                timestamp = datetime.datetime.now()
            )

            options = [('Заголовок', f'{title}', False), ('Варианты', '\n'.join([f'{field_reacts[index]} {field}' for index, field in enumerate(fields)]), False),
            ('Помощь', 'Выберите цифру варианта, за который голосуете', False)]

            for name, val, inl in options:
                embed.add_field(name=name, value=val, inline=inl)

            await ctx.message.delete()
            message = await ctx.send(embed=embed)

            for reaction in field_reacts[:len(fields)]:
                await message.add_reaction(reaction)
        except Exception as e:
            print(e)


    







    
# @client.command(aliases=['рассылка'])
# @commands.check(is_guild_owner)
# @commands.cooldown(1, 86400*2, commands.BucketType.guild)
# async def dm_mailing(ctx, logchannel: discord.TextChannel, *, arg1: str):
#     await logchannel.send('запуск рассылки!')

#     for discord.Member in ctx.guild.members:

#         try:
#             await discord.Member.send('{}'.format(arg1))
#             await logchannel.send(f':white_check_mark: Отправляю сообщение пользователю __**{discord.Member.name}**__')

#         except:
#             await logchannel.send(f':x: Не могу отправить сообщение пользователю __**{discord.Member.name}**__')
#             pass

#     await logchannel.send('рассылка успешно завершена!')

# @dm_mailing.error
# async def spam_error(ctx, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         await ctx.send('err: Кулдаун данной команды 2 дня в целях минимизации нагрузки.')
    
@client.command(name='eval', pass_context=True, aliases=['execute', 'exec'])
@commands.check(isitme)
async def eval_(ctx, *, command: str):
    try:
        res = eval(command.replace('`', ''))
    except Exception as e:
        channel = client.get_channel(752176340186431488)
        embed = discord.Embed(
            title = 'Выполнить',
            description = f'```{command}```',
            color = discord.Color.red(),
            timestamp = datetime.datetime.now()
        )
        
        embed.add_field(name='Error response', value=e)
        await channel.send(embed=embed)
        await ctx.send(f'err: {e}')

    if inspect.isawaitable(res):
        channel = ctx
        embed = discord.Embed(
            title = 'Выполнить',
            description = f'```{command}```',
            color = ctx.author.color,
            timestamp = datetime.datetime.now()
        )
        embed.add_field(name='Type', value=str(type(res)))
        embed.add_field(name='Response', value=await res)
        await channel.send(embed=embed)
    else:
        channel = client.get_channel(752176340186431488)
        embed = discord.Embed(
            title = 'Выполнить',
            description = f'```{command}```',
            color = ctx.author.color,
            timestamp = datetime.datetime.now()
        )
        embed.add_field(name='Type', value=str(type(res)))
        embed.add_field(name='Response', value=res)
        await channel.send(embed=embed)
       
@eval_.error
async def eval_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('err: У вас нет прав на использование этой команды.')
        
@client.command(name='__eval', pass_context=True, aliases=['__execute', '__exec'])
@commands.check(isitme)
async def eval__(ctx, handler: str, *, argument):
    channel = ctx
    if handler == '--return':
        try:
            evaluator = eval(f'type({argument})')
            em = discord.Embed(
                title = 'Return',
                description = f'```{argument}```',
                color = ctx.author.color,
                timestamp = datetime.datetime.now()
            )
            em.add_field(name='Returner', value = str(evaluator))
            embed = discord.Embed(
                title = 'Вернуть',
                description = f'```{argument}```',
                color = ctx.author.color,
                timestamp = datetime.datetime.now()
            )
            embed.add_field(name='Response', value = str(evaluator))
            await ctx.send(embed=em)
        except Exception as e:
            channel = client.get_channel(752176340186431488)
            embed = discord.Embed(
                title = 'Вернуть',
                description = f'```{argument}```',
                color = discord.Color.red(),
                timestamp = datetime.datetime.now()
            )

            embed.add_field(name='Error response', value=e)
            await ctx.send(f'err: {e}')
        
    await channel.send(embed=embed)

@eval__.error
async def eval__error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('err: У вас нет прав на использование этой команды')

@client.command(aliases=['ембед'])
@commands.check(isitme)
async def embed(ctx, *, content: str = None):
    embed = discord.Embed(
        title = 'а)) - Навигация по ролям',
        description = content,
        color = discord.Color.from_rgb(13, 242, 173),
        timestamp = ctx.message.created_at
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    
    await ctx.send(embed=embed)



# @client.command()
# @commands.has_role(763006190971387904)
# async def among(ctx, *, content: str):
#     await ctx.message.delete()
#     embed = discord.Embed(
#         title = 'Among Us',
#         description = content,
#         color = discord.Color.blurple(),
#         timestamp = ctx.message.created_at
#     )
#     await ctx.send(embed=embed)

# @client.command()
# @commands.has_role(763006190971387904)
# async def among_members(ctx, members: commands.Greedy[discord.Member]):
#     among_role = ctx.guild.get_role(762332782767636560)
#     for member in members:
#         await member.add_roles(among_role)

# @client.command()
# @commands.has_role(763006190971387904)
# async def among_end(ctx, members: commands.Greedy[discord.Member]):
#     among_role = ctx.guild.get_role(762332782767636560)
#     for member in members:
#         await member.remove_roles(among_role)



@client.command()
@commands.check(isitme)
async def w(ctx, *, content):
    if ctx.guild != None:
        try:
            await ctx.message.delete()
            webhook = await ctx.channel.create_webhook(name=ctx.author.name)
            await webhook.send(content=content, avatar_url=ctx.author.avatar_url)
            await webhook.delete()
        except Exception as e:
            print(e)
    else:
        await ctx.send('Данная команда не может быть использована здесь.')


@client.command()
@commands.has_role(784144967865073715)
async def enu(ctx, message: discord.Message, *, enu: str):
    enus = {'A': '🇦', 'B': '🇧', 'C': '🇨', 'D': '🇩', 'E': '🇪', 'F': '🇫', 'G': '🇬', 
            'H': '🇭', 'I': '🇮', 'J': '🇯', 'K': '🇰', 'L': '🇱', 'M': '🇲', 'N': '🇳',
            'O': '🇴', 'P': '🇵', 'Q': '🇶', 'R': '🇷', 'S': '🇸', 'T': '🇹', 'U': '🇺',
            'V': '🇻', 'W': '🇼', 'X': '🇽', 'Y': '🇾', 'Z': '🇿', 'a': '🇦', 'b': '🇧',
            'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭', 'i': '🇮', 
            'j': '🇯', 'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 
            'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹', 'u': '🇺', 'v': '🇻', 'w': '🇼',
            'x': '🇽', 'y': '🇾', 'z': '🇿', ' ': ' '}

    for l in enu:
        await message.add_reaction(enus[l])

    await ctx.send('<:sexaca_bydesh:761162679275618334>')



@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)), status=discord.Status.dnd)

@client.command(aliases=['пинг'])
async def ping(ctx):
    await ctx.send(f'Ping: `{round(client.latency*1000)} ms`')

@client.command()
@commands.check(isitme)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded.')
    print(f'{extension} loaded.')

@client.command()
@commands.check(isitme)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded.')
    print(f'{extension} unloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} loaded')

client.run('NzY2Mzg1NjgyMjMwNDExMzE0.X4imSQ.DS2v1agyaVzsClg_TMKNcp3P40A')
