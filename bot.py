import re
import discord
from random import random, randint

TOKEN = "ENTER YOUR DISCORD TOKEN HERE"
client = discord.Client()

linux_copy_pasta = "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called \"Linux\", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\nThere really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called \"Linux\" distributions are really distributions of GNU/Linux."

# Non case sensitive, keys must be words
responses = {"slapen": "Slaapwel!",
             "kat": "Miauw",
             "hond": "Woef",
             "haan": "Kukeleku",
             "vis": "Blub",
             "linux": linux_copy_pasta,
             "slok of gene slok": "WINOK",
             "water": "WATER?! Wil je me soms vergiftigen ofzo?",
             "anne-marie": "*Anne Marie",
             }
# Multiple keys with same value
responses.update(dict.fromkeys(
    ['eten', 'lunchen', 'dinner', 'voedsel', 'lunch', 'ontbijt', 'breakfast', 'brunch', 'snack', 'snacken', 'eeten', 'ete'],
    "Smakelijk!"))
responses.update(dict.fromkeys(['vos', 'fox'], "Ring-ding-ding-ding-dingeringeding!"))
responses.update(dict.fromkeys(['aescu', 'aesculapia'], "ieuw"))

emojis = {",p leave": "👋",
          "good bot": "😘",
          "bad bot": "😠",
          "tea": "🍵",
          "cupcake": "🧁",
          "lockdown": "🔒⬇",
          "se": "🤮",
          'bollekebot': "👀",
          "weyts": "💩",
          "bolleke": "🟠",
          "sad": "😢",
          "cara": "🍻",
          "anne marie": "❤",
          "dorien": "🍻",
          "gitte": "💜",
          "alexander": "🥴"
          }
emojis.update(dict.fromkeys(['pussy', '50 shades'], "😏"))
emojis.update(dict.fromkeys(['birthday', "verjaardag"], "🥳"))
emojis.update(dict.fromkeys(['love', 'liefde', 'hou van'], "😍"))
emojis.update(dict.fromkeys(['dead', 'dood', 'die'], "🔫"))
emojis.update(dict.fromkeys(['corona', 'covid'], "🤧"))
emojis.update(dict.fromkeys(['king', 'mking', 'deceuninck', 'koning'], "👑"))
emojis.update(dict.fromkeys(['sneeuw', 'sneeuwman'], "☃"))
emojis.update(dict.fromkeys(["succes", "success"], "❤"))


def split_words_phrases(dictionary):
    words = dict()
    phrases = dict()
    for key in dictionary:
        if ' ' in key:
            phrases[key] = dictionary[key]
        else:
            words[key] = dictionary[key]
    return words, phrases


word_responses, phrase_responses = split_words_phrases(responses)
emoji_reactions, emoji_reactions_phrases = split_words_phrases(emojis)


async def add_reactions(message, reactions):
    for reaction in reactions:
        await message.add_reaction(reaction)


@client.event
async def on_ready():
    print(f'Active on: ')
    for guild in client.guilds:
        print(f'- {guild.name}')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Mateo climb up the leaderboard"))

def multi_replace(string, replace):
    for char in replace:
        string = string.replace(char, '')
    return string

@client.event
async def on_message(message):
    # Whoever you are, wherever you are, never say WINAK with lowercase letters
    if "winak" in message.content:
        await message.reply("*WINAK")

    if pattern := re.match("-say (.*)", message.content):
        await message.delete()
        await message.channel.send(pattern.group(1))

    # Don't react to my own messages (except in my own bot test channel), only react to messages in the Pomodoro channel
    # and don't react to messages from this bot
    if message.channel.name != "pomodoro" or \
            (message.author.display_name == "Arno Deceuninck" and message.guild.name != "Bot Tests") or \
            message.author == client.user:
        return

    if message.author.bot:
        if "you have been unsubscribed due to inactivity!" in message.content:
            await message.add_reaction("😢")
        return

    # Get the lowercase message without special symbol
    lower_message = multi_replace(message.content.lower(), ",!?.*")
    # Get the words (split the spaces), a set is faster to search in
    words = set(lower_message.split())

    global phrase_responses, emoji_reactions, word_responses, emoji_reactions_phrases

    # Phrase responses
    for key in phrase_responses:
        if key in lower_message:
            await message.reply(phrase_responses[key])

    # word responses
    for word in words:
        if word in word_responses:
            await message.reply(word_responses[word])
        if word in emoji_reactions:
            await add_reactions(message, emoji_reactions[word])

    # emoji reactions
    for key in emoji_reactions_phrases:
        if key in lower_message:
            await add_reactions(message, emoji_reactions_phrases[key])
            # await message.add_reaction(emoji_reactions[key])

    # Special cases
    if ("help" in words or "helpen" in words or "fix" in message.content) and "?" in message.content:
        await message.reply("Have you tried turning it off and on again?")
    if pattern := re.match("[iI]k ben (.*)", message.content):
        await message.reply(f"Hey {pattern.group(1)}, ik ben Bollekebot!")
    if message.author.display_name == "Alexander" and random() < 0.1:
        await message.add_reaction("🥴")
    if "69" in message.content and not message.author.bot:
        await add_reactions(message, "🇳🇮🇨🇪")
    if "mateo" in lower_message and message.guild.name == "WINAK" and not message.author.bot:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="mateo"))
    if "adios" in lower_message and message.guild.name == "WINAK" and not message.author.bot:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="zateo"))
    if "punten" in lower_message:
        await message.reply(f"Je hebt {randint(0, 20)}/20")
    if "haha" in lower_message:
        await message.add_reaction("😆")


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot and reaction.message.content == "try me":
        await reaction.remove(user)
        await reaction.message.add_reaction(reaction.emoji)


client.run(TOKEN)
