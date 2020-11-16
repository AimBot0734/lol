import discord
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='')

status = ['with a girl','Happy diwali', 'eating','sleeping']

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')
    
@client.command(name='Hallo', help='this command returns a random welcome message' )
async def Hallo(ctx):
    responses = ('**Sir,** why did you wake me up', 'i am ready to do your work')
    await ctx.send(choice(responses))

@client.command(name='Die', help='this give you reason for nor dieing')
async def die(ctx):
    responses = ('No, i had my familly', 'Sorry if i did something wrong')
    await ctx.send(choice(responses))

@client.command(name='credits', help='this command show you credits')
async def credits(ctx):
    await ctx.send('Made by MEGABOT')
    await ctx.send('Thanks to PIKACHU  for coming with this idea')
    await ctx.send('Thanks to MEGABOT for building me' )

@client.command(name='ping', help='this command return the latency')
async def ping(ctx):
    await ctx.send(f'**pong!** Ping: {round(client.latency * 1000)}ms')



@client.command()
async def command(ctx):
    await ctx.send('''Hallo\nDie\ncredits\nping\nHii\nhowareyou\nxd''' )


@client.command()
async def Hii(ctx):
    await ctx.send('Hallo')


@client.command()
async def xd(ctx):
    await ctx.send('Haso sab 😊😂')


@client.command()
async def howareyou(ctx):
    await ctx.send('I am fine, What about you')

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('NzcxNDM2MzM1ODUxODk2ODUz.X5sGEw.QQiIJX5aWTf3ecwhkCUwZvyi_jE')
