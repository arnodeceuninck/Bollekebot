import discord
from answer_config import answers
from message import Message
from util import get_motivational_quote
from discord_util import get_message, get_my_user_id
from config import TOKEN

client = discord.Client()


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
    message = Message(message)
    for answer in answers:
        await answer.answer_message(message, client)


@client.event
async def on_reaction_add(reaction, user):
    if not user.bot and reaction.message.content == "try me":
        await reaction.remove(user)
        await reaction.message.add_reaction(reaction.emoji)


@client.event
async def on_raw_reaction_add(reaction):
    if reaction.emoji.name == '🚣‍♂️' and reaction.user_id == get_my_user_id():  # emoji is man rowing boat
        await get_message(reaction.channel_id, reaction.message_id, client).reply(get_motivational_quote())


client.run(TOKEN)
