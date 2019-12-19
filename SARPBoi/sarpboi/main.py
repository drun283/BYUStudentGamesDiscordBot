from pathlib import Path

from discord.ext import commands

from global_vars import COMMAND_STRING

TOKEN = Path('token').read_text()

description = '''Bot for BYU Student Games server'''
bot = commands.Bot(command_prefix=COMMAND_STRING, description=description)


@bot.event
async def on_ready():
    print('Bot is connected')


@bot.check
async def global_check(ctx):
    return 'bot' in ctx.message.channel.name


# @bot.on_command_error
# async def on_command_error(exception):
# have this handle error from the global check
#    print('error')

# load in cogs
print('Loading in cogs')
bot.load_extension("cogs.admin.admin_cog")

#start bot
print('Starting bot')
bot.run(TOKEN)
