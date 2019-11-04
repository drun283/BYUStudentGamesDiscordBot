async def add_game_helper(ctx, game_name):
    name = format_game_name(game_name)
    if not is_game_new(ctx, name):
        return

    # get confirmation from user that name is correct
    await ctx.channel.send('are you sure you want to add {}'.format(name))
    # TODO get confirmation
    confirmation = True

    if confirmation:
        create_roles(name)
        create_announcement_channel(name)
        create_general_channel(name)
        create_feedback_channel(name)


def format_game_name(game_name):
    words = []
    for word in game_name.split():
        words.append(word)

    return '_'.join(words).lower()


def is_game_new(ctx, game_name):
    for channel in ctx.guild.channels:
        if game_name in channel.name:
            return False

    return True


def create_roles(game_name):
    pass    # TODO


def create_announcement_channel(game_name):
    pass    # TODO


def create_general_channel(game_name):
    pass    #TODO


def create_feedback_channel(game_name):
    pass    #TODO
