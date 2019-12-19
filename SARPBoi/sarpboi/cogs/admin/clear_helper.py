from global_vars import COMMAND_STRING


async def clear_helper(ctx):
    await ctx.channel.purge(check=is_bot)
    await ctx.channel.purge(check=is_command)


def is_bot(m):
    return m.author.bot


def is_command(m):
    return m.content.startswith(COMMAND_STRING)
