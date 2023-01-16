import re
import sys

from reply_answer import ReplyAnswer
from react_answer import ReactAnswer
from voice_answer import VoiceAnswer
from function_answer import FunctionAnswer
from util import get_motivational_quote, get_alphabet_str, get_punten
from random import choice, randint, random
from react_config import react_answers
from reply_config import reply_answers
from config import cute_pictures, own_cute_pictures

answers = [ReplyAnswer(lambda m: get_motivational_quote(),
                       substrings_trigger=["depressi", "motivati"],
                       words_trigger=["dieptepunt"],
                       exact_trigger=["!ikwilwenen", "!ikziehetnietmeerzitten", "!fokdeblok",
                                      "!ikkanhetnimeeraan",
                                      "!mijnburenzijnaanhetborenindegemeenschappelijkemuur",
                                      "!concentratieop", "!hetluktnimeer"]),

           ReplyAnswer(lambda m: choice(['!ikook',
                                         "Das oke, iedereen moet soms z'n gevoelens uiten, je geraakt wel door deze examenperiode, YOU CAN DO THIS!",
                                         "https://tenor.com/view/mochi-peachcat-mochi-peachcat-hug-pat-gif-19092449",
                                         "https://discord.com/channels/@me/822251746448900137/932300948670398574",
                                         "https://tenor.com/view/hugs-heart-love-sending-virtual-hug-gif-17607943",
                                         "https://tenor.com/view/virtual-hug-penguin-love-heart-gif-14712845",
                                         "https://tenor.com/view/milk-and-mocha-upset-dont-cry-im-here-gif-13765448",
                                         "https://tenor.com/view/crying-thats-ok-dont-cry-gif-14087354"
                                         ]),
                       exact_trigger=["!ikwilwenen"]),

           ReplyAnswer(lambda m: re.match("-say (.*)", m.get_exact_content()).group(1), regex_trigger="-say (.*)",
                       as_reply=False, delete_message=True, log=True),

           ReplyAnswer(
               lambda m: f"Hey {re.match('[iI]?k[ ]?ben (.*)', m.get_exact_content()).group(1)}, ik ben Bollekebot!",
               regex_trigger="[iI]?k[ ]?ben (.*)", prob=0.05),

           ReactAnswer(lambda m: re.match("-react (.*)", m.get_exact_content()).group(1), regex_trigger="-react (.*)",
                       on_replied=True, delete_message=True, log=True),

           ReactAnswer("fact", exact_trigger="Catoe moet pottoe!", bot_only=True),
           ReactAnswer("😢", substrings_trigger="you have been unsubscribed due to inactivity!", bot_only=True),

           ReactAnswer("lies",
                       substrings_trigger="you will be unsubscribed on the next stage if you do not reply or react to this message.",
                       active_users="Lies"),

           ReplyAnswer("Have you tried turning it off and on again?",
                       custom_trigger=lambda m: (m.contains_substring("help") or m.contains_substring("fix"))
                                                and m.contains_substring("?", match_case=True), prob=0.4),

           ReactAnswer("🥴", active_users="Alexander", prob=0.1),

           ReplyAnswer(lambda m: get_punten(), words_trigger="punten", exact_trigger=["punten", "!punten", "-punten"],
                       prob=0.3),

           ReplyAnswer(lambda m: get_alphabet_str(), exact_trigger="-alphabet"),

           ReplyAnswer(lambda m: "NEGATIEF" if random() > 0.5 else "POSITIEF",
                       custom_trigger=lambda m: m.contains_word("coronatest") or (
                               m.contains_word("corona") and m.contains_word("test"))),
           ReplyAnswer("*WINAK",
                       custom_trigger=lambda m: m.contains_substring("winak", match_case=True) or m.contains_substring(
                           "Winak", match_case=True)),
           ReplyAnswer("", image="boommarter.png", words_trigger="boommarter"),
           FunctionAnswer(lambda m: sys.stdout.flush(), exact_trigger="-flush"),

           ReplyAnswer(lambda m: choice(cute_pictures) if random() > 0.2 else choice(own_cute_pictures),
                       words_trigger=["panda", "cute"],
                       exact_trigger=["!cute", "!panda", "!schattig", "!animal", "!dier"], prob=0.5),

           ReplyAnswer("Hey dad, ik ben Bollekebot!", bot_only=True, regex_trigger="Hello (.*), I'm dad", prob=0.2),

           ReplyAnswer("Zoals een wijs man ooit zei: \"Als een pauze ni uitloopt, is het dan wel een pauze?\"",
                       custom_trigger=lambda m: m.contains_substring("pauze") and
                                                (m.contains_substring("lopen") or m.contains_substring(
                                                    "loop") or m.contains_substring("liep"))
                                                and m.contains_substring("uit")),
           ReactAnswer("🤮", custom_trigger=lambda m: m.contains_word("SE", match_case=True)),
           VoiceAnswer("yeswecan.mp3", exact_trigger=["!yeswecan", "!barackske"]),
           VoiceAnswer("youcandoit.mp3", exact_trigger=["!youcandoit"])
           ]

answers += react_answers
answers += reply_answers
