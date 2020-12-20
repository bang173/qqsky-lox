import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import command
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Collabs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.category_id = 783008035094003722
        self.logchannel_id = 783038231025156136



    @command(name='new-collab',aliases=['новый-коллаб'])
    @commands.cooldown(1, 3600*24, commands.BucketType.member)
    async def clb(self, ctx, collab_name: str, *members: discord.Member):
        try:
            role = ctx.guild.get_role(783012302814838844)
            logchannel = self.client.get_channel(self.logchannel_id)
            if not role in ctx.author.roles:
                await ctx.author.add_roles(role)

                overwrites = {ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True), 
                            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                            ctx.guild.me: discord.PermissionOverwrite(manage_channels=True, manage_permissions=True, read_messages=True, send_messages=True, manage_messages=True)}

                for member in members:
                    overwrites.update({member: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True)})

                category = self.client.get_channel(self.category_id)

                collab_channel = await ctx.guild.create_text_channel(collab_name, topic=ctx.author.id, overwrites=overwrites, category=category)

                mbrs = ', '.join([member.name for member in members])

                await collab_channel.send(embed=discord.Embed(description=f':white_check_mark: Коллаб {collab_name} создан участником {ctx.author.mention}\nУчастники: {mbrs}'))
                await logchannel.send(embed=discord.Embed(description=f':white_check_mark: Коллаб {collab_name} создан участником {ctx.author.mention}\nУчастники: {mbrs}'))
            else:
                await ctx.send(embed=discord.Embed(description=':x: Вы уже организовали 1 коллаб.'))
        except Exception as e:
            await ctx.send(e)


    @command(name='end-collab', aliases=['закончить-коллаб'])
    async def clb_d(self, ctx):
        try:
            role = ctx.guild.get_role(783012302814838844)
            logchannel = self.client.get_channel(self.logchannel_id)

            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                category = self.client.get_channel(self.category_id)
                if ctx.channel.category == category:
                    await logchannel.send(embed=discord.Embed(description=f'Коллаб {ctx.channel.name} был окончен участником {ctx.author}'))
                    await ctx.channel.delete()
        except Exception as e:
            await ctx.send(e)

















def setup(client):
    client.add_cog(Collabs(client))