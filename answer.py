import re
from random import random
from util import to_list, split_words_phrases


class Answer:
    def __init__(self, prob=1.0, words_substr_triggers=None, words_trigger=None, exact_trigger=None,
                 substrings_trigger=None, custom_trigger=None,
                 bot_only=False, active_guild=None, active_channel=None, active_users=None, regex_trigger=None,
                 delete_message=False, log=False):
        if words_trigger is None:
            words_trigger = []
        if exact_trigger is None:
            exact_trigger = []
        if substrings_trigger is None:
            substrings_trigger = []
        if words_substr_triggers is None:
            words_substr_triggers = []

        if regex_trigger is not None:
            regex_trigger = re.compile(regex_trigger)

        words_trigger = to_list(words_trigger)
        exact_trigger = to_list(exact_trigger)
        substrings_trigger = to_list(substrings_trigger)
        active_guild = to_list(active_guild)
        active_channel = to_list(active_channel)
        active_users = to_list(active_users)
        words_substr_triggers = to_list(words_substr_triggers)

        extra_words, extra_substr = split_words_phrases(words_substr_triggers)
        words_trigger += extra_words
        substrings_trigger += extra_substr

        self.prob = prob
        self.words_trigger = words_trigger
        self.exact_trigger = exact_trigger
        self.substrings_trigger = substrings_trigger
        self.custom_trigger = custom_trigger
        self.bot_only = bot_only  # If False, won't react to bots, if True will react only to bots
        self.active_guilds = active_guild  # List of guild name in which it can get triggered
        self.active_channels = active_channel  # List of channel ids in which it can get triggered
        self.active_users = active_users
        self.regex_trigger = regex_trigger
        self.delete_message = delete_message
        self.log = log

    def should_answer(self, message):

        if self.bot_only and not message.from_bot():
            return False

        if not self.bot_only and message.from_bot():
            return False

        if self.active_guilds is not None and message.get_guild_name() not in self.active_guilds:
            return False

        if self.active_channels is not None and message.get_channel_id() not in self.active_channels:
            return False

        if self.active_users is not None and message.get_user_name() not in self.active_users:
            return False

        for text in self.exact_trigger:
            if message.is_exact(text):
                return True

        if not random() < self.prob:
            return False

        for word in self.words_trigger:
            if message.contains_word(word):
                return True

        for substr in self.substrings_trigger:
            if message.contains_substring(substr):
                return True

        if self.custom_trigger is not None and self.custom_trigger(message):
            return True

        if self.regex_trigger is not None and self.regex_trigger.match(message.get_exact_content()):
            return True

        return False

    async def answer_message(self, message, client):
        if self.should_answer(message):
            if self.log or self.delete_message:
                await message.log(client)

            if self.delete_message:
                await message.delete()

            await self.send_answer(message, client)

    async def send_answer(self, message, client):
        raise Exception("Method not implemented")
