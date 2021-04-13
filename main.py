from discord.ext import commands, tasks
from conwech.functions import nameperiod, number2text
from math import *
import discord
import asyncio
import random
import datetime
import os
import pingus

# Hello! Welcome to the official GitHub repository of Greyson Bot. 

client = commands.AutoShardedBot(command_prefix='*',intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Ready! {client.user}')

@client.event
async def on_member_join(m):
    if m.guild.id == 828581824711753738:
        await asyncio.sleep(0.01)
        await m.add_roles(m.guild.get_role(828659697170907166))
        await m.guild.get_channel(831034662167904326).send(f'Welcome {m.mention} to {m.guild.name}!')

@client.event
async def on_message(m):
    if m.guild.id == 828581824711753738 and m.channel.id == 828581824711753741 and random.randint(1,5) == 1:
        await m.channel.send(random.choice(['meow','meow!','Meow!','Meow','*Meow!*','meaw','Meaw!']))

@client.event
async def on_command_error(ctx,e):
    await ctx.send(f'An unexpected error has occurred. Details below.\n{str(e)}')
    raise e

@client.command()
async def ping(ctx):
    # This tells us the bot's ping.
    await ctx.send(f'Pong! {round(client.latency*1000,2)}')

@client.command(name='bignum',aliases=['getperiod','period','nameperiod','pow1000'])
async def period(ctx,power:int=0):
    try:
        await ctx.send(f'1,000^{power} = 1 {nameperiod(power)}')
    except:
        await ctx.send('Your number was too big!')

@client.command()
async def meow(ctx):
    await ctx.send(random.choice(['meow','meow!','Meow!','Meow','*Meow!*','meaw','Meaw!']))

@tasks.loop(seconds=15)
async def meow_task():
    if random.randint(1,1024) == 1:
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