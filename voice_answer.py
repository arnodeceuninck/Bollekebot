from answer import Answer
import discord


class VoiceAnswer(Answer):
    """
    If activated, the voice channel the user is in will be joined and the bot will play the audio file.
    """
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)

        self.file_path = file_path

    async def send_answer(self, message, client):
        author = message.get_discord_message().author
        author_voice = author.voice

        if author_voice is None:
            await message.get_discord_message().reply("You are not in a voice channel!")
            return

        voice_channel = author_voice.channel

        voice_client = await voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(self.file_path))

        while voice_client.is_playing():
            pass

        await voice_client.disconnect()
