from answer import Answer
import discord
import asyncio
import audioread


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

        audio_source = discord.FFmpegPCMAudio(self.file_path)

        voice_client = await voice_channel.connect()
        voice_client.play(audio_source)

        with audioread.audio_open(self.file_path) as f:
            # solution based on https://github.com/YorbenJoosen/Gerbinbot_3000/blob/88f78fd1ddf5f4492bab1fcdf8b91d45fa3aec24/Useful/messagereply.py#L26
            await asyncio.sleep(f.duration)

        await voice_client.disconnect()

