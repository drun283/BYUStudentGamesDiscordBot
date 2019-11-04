from pathlib import Path

from discord.ext import commands
from sarpboi.helper.add_game import add_game_helper

TOKEN = Path('token').read_text()
GUILD = 'BYU Student Games'


commandString = '!'
description = '''Bot for BYU Student Games server'''
bot = commands.Bot(command_prefix=commandString, description=description)


@bot.event
async def on_ready():
    print('Bot is connected')


@bot.check
async def global_check(ctx):
    return 'bot' in ctx.message.channel.name


#@bot.on_command_error
#async def on_command_error(exception):
#    print('error')


@bot.command(name='add_game')
@commands.has_role('Admin')
async def add_game(ctx, *args):
    '''
    Creates channels and roles for new games. This can only be called by an Admin.
    '''
    game_name = ' '.join(args)
    await add_game_helper(ctx, game_name)


@bot.command(name='clear')
@commands.has_role('Admin')
async def clear(ctx):
    await ctx.channel.purge()


bot.run(TOKEN)
