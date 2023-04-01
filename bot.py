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

    if message.from_me(client):
        return

    if message.is_dm():
        await message.log(client)

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

@client.event
async def on_voice_state_update(member, before, after):

    bibvriendjes_voice = 1055831367495196722
    bibvriendjes_chat = 1091843831768555570

    bottest_voice = 802509903540912192
    bottest_chat = 802509903540912191

    channels = {bottest_voice: bottest_chat, bibvriendjes_voice: bibvriendjes_chat}

    # if a user joins voice channel 802509903540912192 and is alone there, send a message in text channel 802509903540912191
    if after.channel is not None and len(after.channel.members) == 1 and after.channel.id in channels:
        text_channel = client.get_channel(channels[after.channel.id])
        await text_channel.send(f"{member.display_name} is studying. Feel free to join!")


client.run(TOKEN)
