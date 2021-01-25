import re
import discord
from random import random, randint
from config import emojis, responses

TOKEN = "ENTER YOUR DISCORD TOKEN HERE"
client = discord.Client()


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
        try:
            await message.add_reaction(reaction)
        except discord.errors.HTTPException:
            print(f"Unknown emoji {reaction}")


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


def is_me(user):
    return user.display_name == "Arno Deceuninck"


def should_react(message):
    return not (message.channel.name != "pomodoro" or
                (is_me(message.author) and message.guild.name != "Bot Tests" and not "x" in message.content) or
                message.author == client.user)


@client.event
async def on_message(message):
    # Whoever you are, wherever you are, never say WINAK with lowercase letters
    if "winak" in message.content:
        await message.reply("*WINAK")

    if is_me(message.author):
        await check_manual_commands(message)

    # Don't react to my own messages (except in my own bot test channel), only react to messages in the Pomodoro channel
    # and don't react to messages from this bot
    if not should_react(message):
        return

    if message.author.bot:
        return await bot_only_reactions(message)

    # Get the lowercase message without special symbol
    lower_message = multi_replace(message.content.lower(), ",!?.*")
    # Get the words (split the spaces), a set is faster to search in
    words = set(lower_message.split())

    await react_configured_cases(lower_message, message, words)

    # Special cases
    await react_special_cases(lower_message, message, words)


async def check_manual_commands(message):
    if pattern := re.match("-say (.*)", message.content):
        await message.delete()
        await message.channel.send(pattern.group(1))
    if pattern := re.match("-react (.*)", message.content):
        await message.delete()
        await add_reactions(message.reference.resolved, pattern.group(1).replace(' ', ''))
    return


async def bot_only_reactions(message):
    if "you have been unsubscribed due to inactivity!" in message.content:
        await message.add_reaction("😢")
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
