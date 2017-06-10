import discord
from discord.ext import commands
import random

description = '''Me making a bot because I don't want to study normally.'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 5:
        await bot.say('Stop breaking my please.')
        return
    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool."""
    test = random.randint(0, 1)
    if test == 0:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))
    else:
        await bot.say('Yes, {0.subcommand_passed} is cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run('MzIzMTExNzMzNjIxMjkzMDU2.DB2Y0A.EWpkMQkzUURhPXb9Q7owIsA8Z9w')
