import asyncio
import discord
from discord.ext import commands 
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Stafflist(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.me = 616691484057534465
        self.second_me = 647735617496547330
        self.stafflists = {}
        self.stafflist_role_members = {}

    
    @commands.command(aliases=['стаффлист'])
    async def stafflist(self, ctx, handler: str, schannel: discord.TextChannel, sroles: commands.Greedy[discord.Role]):
        try:
            if ctx.author.id == self.me or ctx.author.id == self.second_me:

                if handler == 'add':
                    for srole in sroles:
                        self.stafflist_role_members.update({srole.id: srole.members})
                        embed = discord.Embed(
                            title = f'{srole}',
                            description  = ', '.join([member.name for member in srole.members]),
                            color = srole.color
                        )
                        smessage = await schannel.send(embed=embed)
                        self.stafflists.update({srole.id: smessage})
        except Exception as e:
            print(e)
            



    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.guild.id == 650023366220316702:
            if before.roles != after.roles:
                try:

                    for role in before.roles:
                        if role.id in self.stafflists:
                            smessage = self.stafflists[role.id]

                            embed = discord.Embed(
                                title = f'{role}',
                                description = ', '.join([member.name for member in role.members]),
                                color = role.color
                            )
                            await smessage.edit(embed=embed)

                    for role in after.roles:
                        if role.id in self.stafflists:
                            smessage = self.stafflists[role.id]

                            embed = discord.Embed(
                                title = f'{role}',
                                description = ', '.join([member.name for member in role.members]),
                                color = role.color
                            )
                            await smessage.edit(embed=embed)

                except Exception as e:
                    print(e)

            







def setup(client):
    client.add_cog(Stafflist(client))