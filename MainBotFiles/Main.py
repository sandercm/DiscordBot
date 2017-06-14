import discord
from discord.ext import commands
import random
from riotwatcher import RiotWatcher
from riotwatcher import EUROPE_WEST
import requests
import json

euw = RiotWatcher('RGAPI-ff834936-b418-4711-8042-e81b804a8441', default_region=EUROPE_WEST)

description = '''Me making a bot because I don't want to study normally.'''
bot = commands.Bot(command_prefix='?', description=description)
brent = bot.get_user_info("superscheire#2467")
toetoet = bot.get_server("235869503521685504")
forVal = 0
againstVal = 0
votingActive = False


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def vote(topic:str):
    await bot.say("now voting on " + str(topic))
    global votingActive
    votingActive = True
    global forVal
    forVal = 0
    global againstVal
    againstVal = 1
    await bot.say("type ?yes for or ?no against")


@bot.command()
async def yes():
    global forVal
    forVal = forVal + 1
    await bot.say("current score is for: " + str(forVal) + " against: " + str(againstVal))


@bot.command()
async def no():
    global againstVal
    againstVal = againstVal + 1
    await bot.say("current score is for: " + str(forVal) + " against: " + str(againstVal))


@bot.command()
async def mastery(user: str, champ: str):
    """"type username in 1 word gives mastery"""
    try:
        user_id = euw.get_summoner(name=user).get('id')
        champName = champ[0].upper() + champ[1:].lower()
        champInfo = euw.static_get_champion_list().get('data').get(champName)
        dictJson = requests.get(
            "https://euw1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + str(
                user_id) + "/by-champion/" + str(
                champInfo.get('id')) + "?api_key=RGAPI-ff834936-b418-4711-8042-e81b804a8441")
    except:
        bot.say("invalid username or champion")
        return
    name = json.loads(dictJson.content.decode("utf-8")).get("championLevel")
    if name == None:
        await bot.say("No mastery.")
    else:
        await bot.say("Mastery level = " + str(name))


@bot.command()
async def brent():
    await bot.say("Fuck " + "<@!231101437206069248>" + " .", tts=True)


@bot.command()
async def robin():
    await bot.say("Fuck " + "<@!200915533942620160>" + " .", tts=True)


@bot.command()
async def barry():
    await bot.say("Please ride me " + "<@!120252230560514051>" + " .", tts=True)


@bot.command()
async def kathy():
    await bot.say("<@!270223269964021761>" + " still " + str(random.randint(0, 99)) + "% hardcore.", tts=True)


@bot.command()
async def sendNudes1():
    await bot.say(
        "https://images.discordapp.net/attachments/319527831837343746/323150297646104576/XayahxRiven.jpg?width=313&height=407")


@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 5:
        await bot.say('Stop breaking my please.')
        return
    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member: discord.Member):
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
