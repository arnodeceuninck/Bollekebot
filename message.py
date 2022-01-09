from util import multi_char_remove
import discord


class Message:
    def __init__(self, discord_message):
        self.discord_message = discord_message
        self.lower_message = None
        self.words = None

    def get_exact_content(self) -> str:
        return self.discord_message.content

    def get_lower_message(self):
        if self.lower_message is None:
            self.lower_message = multi_char_remove(self.get_exact_content().lower(), ",!?.*\"'")
        return self.lower_message

    def get_word_list(self):
        if self.words is None:
            self.words = set(self.get_lower_message().split())
        return self.words

    def contains_word(self, word):
        return word in self.get_word_list()

    def contains_substring(self, substring, match_case=False):
        if match_case:
            check_string = self.get_exact_content()
        else:
            check_string = self.get_lower_message()
            substring = substring.lower()

        return substring in check_string

    def is_exact(self, string):
        return self.get_exact_content() == string

    def get_discord_message(self):
        return self.discord_message

    def get_reference_discord_message(self):
        return self.get_discord_message().reference.resolved

    def react(self, reaction, on_replied=False):
        if not on_replied:
            discord_message = self.get_discord_message()
        else:
            discord_message = self.get_reference_discord_message()

        return discord_message.add_reaction(reaction)

    def from_bot(self):
        return self.get_author().bot

    def get_guild_name(self):
        pass  # TODO

    def get_channel_id(self):
        pass  # TODO

    def get_author(self):
        return self.get_discord_message().author

    def log(self):
        user = self.get_author()
        print(f"{user.display_name}({user.id}): {self.get_exact_content()}")

    def get_user_name(self):
        return self.get_author().display_name

    def delete(self):
        return self.get_discord_message().delete()

    def is_dm(self):
        return self.get_discord_message().channel.type == discord.ChannelType.private
