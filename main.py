from discord.ext import commands, tasks
from __future__ import print_function
import discord
import asyncio
import datetime
import os
import pingus

client = commands.AutoShardedBot(command_prefix='meow!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Ready! {client.user}')

pingus.up()
client.run(os.environ('TOKEN'))