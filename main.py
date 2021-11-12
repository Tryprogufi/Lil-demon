import os
import discord
from discord.ext import commands
import sys
import sqlite3
def cursor():
    return sqlite3.connect('main.sqlite').cursor()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    c = cursor()
    c.execute('CREATE TABLE IF NOT EXISTS welcome (guild_id TEXT, msg TEXT, channel_id TEXT)')
    c.connection.close()
    print(f'{bot.user} has just logged on!')

initial_extentions = ['cogs.welcome', 'cogs.moderation', 'cogs.leveling']

if __name__ == '__main__':
    for extention in initial_extentions:
        try:
            bot.load_extension(extention)
        except Exception as e:
            print(f'Failed to load extention {extention}', file=sys.stderr)

@bot.command() 
async def hello(ctx):
    await ctx.send('Hello')


bot.run(os.environ['TOKEN']) #You can put you token here
