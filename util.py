from random import random, choice
from config import quotes
from config import letter_emojis
import string
import discord
from client import client
from config import letter_emojis


def get_motivational_quote():
    """
    :return: A random quote from the quotes list or a cute gif
    """
    if random() < 0.2:
        return "https://tenor.com/view/motivation-motivational-penguin-gif-14021416"
    elif random() < 0.1:
        return "https://tenor.com/view/polar-bear-cute-ice-bear-gif-19566864"
    else:
        return choice(quotes)


def split_words_phrases(dictionary):
    """
    Splits the dictionary from the config into a dictionary containing words and a dictionary containing phrases
    """
    words = dict()
    phrases = dict()
    for key in dictionary:
        if ' ' in key:
            phrases[key] = dictionary[key]
        else:
            words[key] = dictionary[key]
    return words, phrases


def multi_replace(string, replace):
    for char in replace:
        string = string.replace(char, '')
    return string


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


async def react_emoji(channel_id, message_id, emoji):
    channel = client.get_channel(channel_id)
    message = channel.get_partial_message(message_id)
    await message.add_reaction(emoji)


async def react_winak_emoji(channel_id, message_id):
    await react_emoji(channel_id, message_id, get_winak_emoji())


def get_winak_emoji():
    winak_guild = client.get_guild(693029155398221864)
    emoji = winak_guild.emojis[3]
    assert emoji.name == 'WINAK'
    return emoji


def is_me(user):
    return user.display_name == "Arno Deceuninck"

def letter_reaction(alphabet, letter):
    if letter == "W":
        return get_winak_emoji()
    letter = letter.lower()
    letter_occurances = alphabet[letter]
    possible_letters = letter_emojis[letter]
    if len(possible_letters) > letter_occurances:
        letter_emoji = possible_letters[letter_occurances]
    else:
        return None
    alphabet[letter] += 1
    return letter_emoji



