from answer import Answer
from util import to_list
from discord_util import letter_reaction
import string
import discord


class ReactAnswer(Answer):
    def __init__(self, reaction, **kwargs):
        super().__init__(**kwargs)

        self.reactions = reaction  # Warning: This is a string and not a list

    async def send_answer(self, message, client):
        alphabet = dict.fromkeys(string.ascii_lowercase, 0)

        reactions = self.reactions
        if not isinstance(self.reactions, str):
            reactions = reactions(message)

        for reaction in reactions:
            try:
                if reaction.isalpha():
                    reaction = letter_reaction(alphabet, reaction, client)
                if reaction:
                    await message.react(reaction)
            except discord.errors.HTTPException:
                # print(f"Unknown emoji {reaction}")
                pass

