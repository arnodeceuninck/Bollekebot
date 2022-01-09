from config import letter_emojis


def letter_reaction(alphabet, letter, client):
    """
    Given a letter, this returns an emoji representing the letter
    :param alphabet: an array of length 26 containing how much each letter has already been used
    :param letter:
    :return:
    """
    if letter == "W":
        return get_winak_emoji(client)
    letter = letter.lower()
    letter_occurances = alphabet[letter]
    possible_letters = letter_emojis[letter]
    if len(possible_letters) > letter_occurances:
        letter_emoji = possible_letters[letter_occurances]
    else:
        return None
    alphabet[letter] += 1
    return letter_emoji


def get_message(channel_id, message_id, client):
    channel = client.get_channel(channel_id)
    message = channel.get_partial_message(message_id)
    return message


async def react_emoji(channel_id, message_id, emoji, client):
    message = get_message(channel_id, message_id, client)
    await message.add_reaction(emoji)


def get_winak_emoji(client):
    winak_guild = client.get_guild(693029155398221864)
    emoji = winak_guild.emojis[3]
    assert emoji.name == 'WINAK'
    return emoji


def get_my_user_id():
    return 224550208053313536


async def message_myself(msg, client):
    me = await client.fetch_user(get_my_user_id())
    await client.wait_until_ready()
    await me.send(msg)
