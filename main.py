from discord.ext import commands, tasks
import discord
import asyncio
import random
import datetime
import os
import pingus

# Hello! Welcome to the official GitHub repository of Greyson Bot. 

client = commands.AutoShardedBot(command_prefix='meow!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Ready! {client.user}')

@client.command()
async def ping(ctx):
    # This tells us the bot's ping.
    await ctx.send(f'Pong! {client.latency}')

@tasks.loop(seconds=12)
async def meow_task():
    if random.randint(1,32) == 1:
        # Gets Greyson's server
        greyson_groop = client.get_guild(828581824711753738)
        # Gets the proper channel
        gg_channel = greyson_groop.get_channel(828581824711753741)
        # Sends the message!
        # We need to check if the channel is active or not.
        await gg_channel.send(random.choice(['meow','meow!','Meow!','Meow','*Meow!*','meaw','Meaw!']))

meow_task.start()


pingus.up()
client.run(os.getenv('TOKEN'))