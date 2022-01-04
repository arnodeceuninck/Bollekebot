import sys
import re
from random import random, randint

from config import *
from util import get_motivational_quote, add_reactions, split_words_phrases

import discord

async def check_manual_commands(message):
    """"
    Reaction that only work for me
    """
    if pattern := re.match("-say (.*)", message.content):
        print(f"{message.author.display_name}: {message.content}")
        await message.delete()
        await message.channel.send(pattern.group(1))
    elif message.content == "-flush":
        sys.stdout.flush()
        await message.add_reaction("👌")
    return


async def bot_only_reactions(message):
    """
    Reactions that only work on bots
    """
    if message.content == "Catoe moet pottoe!":
        await add_reactions(message, "fact")
    if "you have been unsubscribed due to inactivity!" in message.content:
        await message.add_reaction("😢")
    if "you will be unsubscribed on the next stage if you do not reply or react to this message." in message.content:
        for user in message.mentions:
            if user.display_name == "Lies":
                await add_reactions(message, "lies")
    return


async def react_configured_cases(lower_message, message, words):
    """"
    Reactions defined in the config file (work on all user messages)
    """
    if random() < 0.8:
        return
    global phrase_responses, emoji_reactions, word_responses, emoji_reactions_phrases
    # Phrase responses
    for key in phrase_responses:
        if key in lower_message:
            await message.reply(phrase_responses[key])
    # word responses
    for word in words:
        if word in word_responses:
            if word_responses[word] == "Smakelijk!" and random() < 0.5:
                continue
            await message.reply(word_responses[word])
        if word in emoji_reactions:
            await add_reactions(message, emoji_reactions[word])
    # emoji reactions
    for key in emoji_reactions_phrases:
        if key in lower_message:
            await add_reactions(message, emoji_reactions_phrases[key])
            # await message.add_reaction(emoji_reactions[key])


async def react_special_cases(lower_message, message, words):
    """
    Reactions not defined in the config
    TODO: Some of those can be removed if I let users specify a chance in the config or a reaction function
    """
    if ("motivatie" in words or "depressief" in words) or message.content in ["!ikwilwenen", "!ikziehetnietmeerzitten",
                                                                              "!fokdeblok", "!ikkanhetnimeeraan",
                                                                              "!mijnburenzijnaanhetborenindegemeenschappelijkemuur",
                                                                              "!concentratieop"]:
        if message.content == "!ikwilwenen" and random() < 1:
            await message.reply(
                "Das oke, iedereen moet soms z'n gevoelens uiten, je geraakt wel door deze examenperiode, YOU CAN DO THIS!")
        await message.reply(get_motivational_quote())
    if message.content == "Catoe moet pottoe!":
        await message.reply("factsssssssss")
    if ("help" in words or "helpen" in words or "fix" in message.content) and "?" in message.content:
        await message.reply("Have you tried turning it off and on again?")
    if pattern := re.match("[iI]?k[ ]?ben (.*)", message.content):
        if random() < 0.2:
            await message.reply(f"Hey {pattern.group(1)}, ik ben Bollekebot!")
    if message.author.display_name == "Alexander" and random() < 0.1:
        await message.add_reaction("🥴")
    if "mateo" in lower_message and message.guild.name == "WINAK" and random() < 0.2:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="mateo"))
    if "lmao" in words or "lmfao" in words and message.guild.name == "WINAK" and random() < 0.2:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="lmfao"))
    if ("adios" in words or "zateo" in words) and message.guild.name == "WINAK" and random() < 0.2:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="zateo"))
    if "punten" in lower_message:
        await message.reply(f"Je hebt {randint(0, 20)}/20")
    if message.content == "420":
        await message.reply(
            f"NEE IK HEB NOGSTEEDS NIETS VOOR 420 ERIN GEZET, HOE VAAK GA JE DA NOG PROBEREN {message.author.display_name.upper()}?!")
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
    if "winak" in message.content or "Winak" in message.content:
        await message.reply("*WINAK")
    if pattern := re.match("-react (.*)", message.content):
        print(f"{message.author.display_name}: {message.content}")
        await message.delete()
        await add_reactions(message.reference.resolved, pattern.group(1).replace(' ', ''))
    if "boommarter" in words:
        await message.reply(file=discord.File('boommarter.png'))

# Preprocess the words and phrases
word_responses, phrase_responses = split_words_phrases(responses)
emoji_reactions, emoji_reactions_phrases = split_words_phrases(emojis)