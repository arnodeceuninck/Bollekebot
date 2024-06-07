import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Used when adding letter-per-letter emoji reactions on a message
letter_emojis = {"a": "🇦🅰🔼👖🙈🩳🦑", "b": "🇧🅱️", "c": "🇨◀️", "d": "🇩▶👂🦻", "e": "🇪💶🎼📧🟦", "f": "🇫🤏",
                 "g": "🇬",
                 "h": "🇭🦕", "i": "🇮ℹ❕️❗", "j": "🇯☂️", "k": "🇰◀️🎋", "l": "🇱🦾💪📃", "m": "🇲📧👑", "n": "🇳🟦📰",
                 "o": "🇴🅾⭕🟠", "p": "🇵", "q": "🇶", "r": "🇷🎗🎋", "s": "🇸🪱", "t": "🇹✝️", "u": "🇺👅",
                 "v": "🇻🔽🔻🥇🥈🥉", "w": "🇼🗑️", "x": "🇽", "y": "🇾", "z": "🇿"}

# A list containing motivational quotes
with open("quotes.txt") as f:
    quotes = f.read().splitlines()

# A list containing motivational quotes
with open("motivation.txt") as f:
    motivation = f.read().splitlines()

# A list containing cute pictures
with open("cute.txt", encoding="utf8") as f:
    cute_pictures = f.read().splitlines()

# A list containing cute pictures made ourselves
with open("own_cute.txt", encoding="utf8") as f:
    own_cute_pictures = f.read().splitlines()
