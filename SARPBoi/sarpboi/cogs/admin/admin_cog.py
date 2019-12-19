from discord.ext import commands

from cogs.admin.add_game_helper import add_game_helper
from cogs.admin.clear_helper import clear_helper
from global_vars import ADMIN


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        for role in ctx.author.roles:
            if role.name == ADMIN:
                return True

        return False

    async def cog_command_error(self, ctx, error):
        # TODO add a check to only send this if they failed the check
        await ctx.channel.send('{} only admins can use this command'.format(ctx.author.mention))

    @commands.command(name='add_game')
    async def add_game(self, ctx, *args):
        """
        Creates channels and roles for new games. Can only be called by an Admin.
        """
        game_name = ' '.join(args)
        await add_game_helper(ctx, game_name)

    @commands.command(name='clear')
    async def clear(self, ctx):
        """
        Clears commands and bot messages in this channel. Can only be called by an Admin.
        """
        await clear_helper(ctx)


def setup(bot):
    bot.add_cog(AdminCog(bot))
