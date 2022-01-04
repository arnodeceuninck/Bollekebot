import discord
from config import emojis, responses
from reactions import react_special_cases, react_configured_cases, bot_only_reactions, check_manual_commands
from util import split_words_phrases, multi_replace
from client import client
from util import get_motivational_quote, react_winak_emoji, is_me

TOKEN = "ENTER YOUR DISCORD TOKEN HERE"

@client.event
async def on_ready():
    # Print all the guilds the bot is active in
    print(f'Active on: ')
    for guild in client.guilds:
        print(f'- {guild.name}')

    # Change the bot status to Watching ...
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="everyone study :)"))


@client.event
async def on_message(message):
    # Get the lowercase message without special symbol
    lower_message = multi_replace(message.content.lower(), ",!?.*")
    # Get the words (split the spaces), a set is faster to search in
    words = set(lower_message.split())

    if is_me(message.author):
        await check_manual_commands(message)
    if message.author.bot:
        return await bot_only_reactions(message)
    await react_configured_cases(lower_message, message, words)
    await react_special_cases(lower_message, message, words)


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot and reaction.message.content == "try me":
        await reaction.remove(user)
        await reaction.message.add_reaction(reaction.emoji)


@client.event
async def on_raw_reaction_add(reaction):
    if reaction.emoji.name == 'Fabiant':
        await react_winak_emoji(reaction.channel_id, reaction.message_id)
    print(reaction.emoji.name, reaction.member.display_name)
    if reaction.emoji.name == '🚣‍♂️' and reaction.member.display_name == 'Arno Deceuninck':  # emoji is man rowing boat
        channel = client.get_channel(reaction.channel_id)
        message = channel.get_partial_message(reaction.message_id)
        await message.reply(get_motivational_quote())


client.run(TOKEN)

