import re
import discord
from random import random, randint
from config import emojis, responses
import string
import sys

TOKEN = "ENTER YOUR DISCORD TOKEN HERE"
client = discord.Client()

# String.fromCodePoint("R".codePointAt(0) - 65 + 0x1f1e6) kon ook
letter_emojis = {"a": "🇦🅰🔼👖🙈🩳🦑", "b": "🇧🅱️", "c": "🇨◀️", "d": "🇩▶👂🦻", "e": "🇪💶🎼📧🟦", "f": "🇫🤏", "g": "🇬",
                 "h": "🇭🦕", "i": "🇮ℹ❕️❗", "j": "🇯☂️", "k": "🇰◀️🎋", "l": "🇱🦾💪📃", "m": "🇲📧👑", "n": "🇳🟦📰",
                 "o": "🇴🅾⭕🟠", "p": "🇵", "q": "🇶", "r": "🇷🎗🎋", "s": "🇸🪱", "t": "🇹✝️", "u": "🇺👅",
                 "v": "🇻🔽🔻🥇🥈🥉", "w": "🇼🗑️", "x": "🇽", "y": "🇾", "z": "🇿"}


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
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    for reaction in reactions:
        try:
            if reaction.isalpha():
                reaction = letter_reaction(alphabet, reaction)
            if reaction:
                await message.add_reaction(reaction)
        except discord.errors.HTTPException:
            print(f"Unknown emoji {reaction}")


def letter_reaction(alphabet, letter):
    letter = letter.lower()
    letter_occurances = alphabet[letter]
    possible_letters = letter_emojis[letter]
    if len(possible_letters) > letter_occurances:
        letter_emoji = possible_letters[letter_occurances]
    else:
        return None
    alphabet[letter] += 1
    return letter_emoji


def multi_replace(string, replace):
    for char in replace:
        string = string.replace(char, '')
    return string


def is_me(user):
    return user.display_name == "Arno Deceuninck"


def should_react(message):
    # Don't react to my own messages (except in my own bot test channel), only react to messages in the Pomodoro channel
    # and don't react to messages from this bot
    # message.channel.name != "pomodoro" or
    return message.author != client.user


async def check_manual_commands(message):
    if pattern := re.match("-say (.*)", message.content):
        print(f"{message.author.display_name}: {message.content}")
        await message.delete()
        await message.channel.send(pattern.group(1))
    elif pattern := re.match("-run (.*)", message.content):
        # Warning: Dangerous code, anyone satisfying is_me can run any python code (TODO)
        print(f"{message.author.display_name}: {message.content}")
        exec(pattern.group(1))
        await message.reply("Done")
    elif message.content == "-flush":
        sys.stdout.flush()
        await message.add_reaction("👌")
    return


async def bot_only_reactions(message):
    if "you have been unsubscribed due to inactivity!" in message.content:
        await message.add_reaction("😢")
    if "you will be unsubscribed on the next stage if you do not reply or react to this message." in message.content:
        for user in message.mentions:
            if user.display_name == "Lies":
                await add_reactions(message, "lies")
    return


async def react_configured_cases(lower_message, message, words):
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


async def react_special_cases(lower_message, message, words):
    if ("help" in words or "helpen" in words or "fix" in message.content) and "?" in message.content:
        await message.reply("Have you tried turning it off and on again?")
    if pattern := re.match("[iI]?k[ ]?ben (.*)", message.content):
        await message.reply(f"Hey {pattern.group(1)}, ik ben Bollekebot!")
    if message.author.display_name == "Alexander" and random() < 0.1:
        await message.add_reaction("🥴")
    if "mateo" in lower_message and message.guild.name == "WINAK":
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="mateo"))
    if "lmao" in words or "lmfao" in words and message.guild.name == "WINAK":
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="lmfao"))
    if ("adios" in words or "zateo" in words) and message.guild.name == "WINAK":
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="zateo"))
    if "punten" in lower_message:
        await message.reply(f"Je hebt {randint(0, 20)}/20")
    if "haha" in lower_message:
        await message.add_reaction("😆")
    if message.content == "420":
        await message.reply(f"NEE IK HEB NOGSTEEDS NIETS VOOR 420 ERIN GEZET, HOE VAAK GA JE DA NOG PROBEREN {message.author.display_name.upper()}?!")
    if message.content == "-alphabet":
        reaction = ""
        for letter in letter_emojis:
            reaction += f"{letter_emojis[letter]}\n"
        await message.reply(reaction)
    if "mai pii" in lower_message:
        await message.add_reaction("🇻🇳")
    if "coronatest" in words or ("corona" in words and "test" in words):
        if random() > 0.5:
            result = "NEGATIEF"
        else:
            result = "POSITIEF"
        await message.reply(result)




@client.event
async def on_ready():
    print(f'Active on: ')
    for guild in client.guilds:
        print(f'- {guild.name}')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Mateo climb up the leaderboard"))

@client.event
async def on_message(message):
    # print(message.content)
    # Whoever you are, wherever you are, never say WINAK with lowercase letters
    if "winak" in message.content:
        await message.reply("*WINAK")
    if pattern := re.match("-react (.*)", message.content):
        print(f"{message.author.display_name}: {message.content}")
        await message.delete()
        await add_reactions(message.reference.resolved, pattern.group(1).replace(' ', ''))
    if is_me(message.author):
        await check_manual_commands(message)

    if not should_react(message):
        return

    if message.author.bot:
        return await bot_only_reactions(message)

    # Get the lowercase message without special symbol
    lower_message = multi_replace(message.content.lower(), ",!?.*")
    # Get the words (split the spaces), a set is faster to search in
    words = set(lower_message.split())

    await react_configured_cases(lower_message, message, words)
    await react_special_cases(lower_message, message, words)

@client.event
async def on_reaction_add(reaction, user):
    if not user.bot and reaction.message.content == "try me":
        await reaction.remove(user)
        await reaction.message.add_reaction(reaction.emoji)


client.run(TOKEN)
