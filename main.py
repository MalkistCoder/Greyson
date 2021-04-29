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


@client.command()
async def animate(ctx):
    m = await ctx.send('Meow!')
    for i in range(30):
        await m.edit(content='o/')
        await asyncio.sleep(0.75)
        await m.edit(content='o7')
        await asyncio.sleep(0.75)
    await m.delete()
    mm = await ctx.send('Animation test finished!')
    await asyncio.sleep(10)
    await mm.delete()
    

pingus.up()
client.run(os.environ['TOKEN'])