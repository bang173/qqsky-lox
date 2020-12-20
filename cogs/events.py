import asyncio
import discord
from discord.ext import commands 
import json 
import random
from random import choice
from datetime import datetime, timedelta



class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 764936371319341067:
            await message.add_reaction('✅')
            await message.add_reaction('❌')
    
    
    
    
    
def setup(client):
    client.add_cog(Events(client))
