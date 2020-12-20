import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import command
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Tools(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    @command()
    @commands.has_role(789893475268165642)
    # @commands.is_owner()
    async def overwritescopy(self, ctx, channel1: discord.TextChannel, channel2: discord.TextChannel):
        try:
            await channel2.edit(overwrites=channel1.overwrites)
            await ctx.send(f':white_check_mark: overwrites copied from {channel1} to {channel2}')
        
        except Exception as e:
            await ctx.send(e)
            

    # @command()
    # # @commands.has_role(789893475268165642)
    # @commands.is_owner()
    # async def overwriteset(self, ctx, obj, channel: discord.TextChannel, overwrite, handler):
    #     try:
    #         tf = None
    #         if handler == 't' or handler == 'true':
    #             tf = True
    #         elif handler == 'f' or handler == 'false':
    #             tf = False

    #         overwrites = {obj: discord.PermissionOverwrite(f'{overwrite}'=tf)}
                
    #         await eval(f'self.client.get_channel({channel.id}).edit(overwrites={overwrites})')
    #         await ctx.send(f':white_check_mark: overwrite {overwrite} has been set to {handler} for {obj} in {channel}')
        
    #     except Exception as e:
    #         await ctx.send(e)

    
    @command()
    # @commands.has_permissions(manage_channels=True)
    @commands.has_role(789893475268165642)
    async def typechannel(self, ctx, chtype: str, channel: discord.TextChannel):
        role = ctx.guild.get_role(767023676712681493)
        try:
            if chtype == 'normal':
                overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                role: discord.PermissionOverwrite(read_messages=True, send_messages=False, add_reactions=False)}

            elif chtype == 'unnormal':
                overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                role: discord.PermissionOverwrite(read_messages=False, send_messages=False, add_reactions=False)}

            await channel.edit(overwrites=overwrites)
            await ctx.send(f':white_check_mark: {channel} type has been set to {chtype}')
        except Exception as e:
            await ctx.send(e)



    @command(aliases=['выговор'])
    @commands.has_role(789893475268165642)
    async def infraction(self, ctx, what: str, mod: discord.Member, *, reason: str):
        inf_gmod_channel = self.client.get_channel(789897693086089256)
        inf_dmod_channel = self.client.get_channel(789912278861873152)

        if what == 'gmod':
            embed = discord.Embed(
                title = '❗ Выговор ❗',
                description = f'{mod.mention} получает выговор от {ctx.author.mention}.\nПричина: `{reason}`',
                color = discord.Color.from_rgb(180,0,10),
                timestamp = datetime.now()
            )
            await inf_gmod_channel.send(f'{mod.mention}', embed=embed)

        elif what == 'dmod':
            embed = discord.Embed(
                title = '❗ Выговор ❗',
                description = f'{mod.mention} получает выговор от {ctx.author.mention}.\nПричина: `{reason}`',
                color = discord.Color.from_rgb(180,0,10),
                timestamp = datetime.now()
            )
            await inf_dmod_channel.send(f'{mod.mention}', embed=embed)

        else:
            pass











def setup(client):
    client.add_cog(Tools(client))