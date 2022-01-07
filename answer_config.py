import re

from reply_answer import ReplyAnswer
from react_answer import ReactAnswer
from util import get_motivational_quote, get_alphabet_str
from random import choice, randint, random
from react_config import react_answers
from reply_config import reply_answers

answers = [ReplyAnswer(lambda m: get_motivational_quote(),
                       substrings_trigger=["depressi", "motivati"],
                       words_trigger=["dieptepunt"],
                       exact_trigger=["!ikwilwenen", "!ikziehetnietmeerzitten", "!fokdeblok",
                                      "!ikkanhetnimeeraan",
                                      "!mijnburenzijnaanhetborenindegemeenschappelijkemuur",
                                      "!concentratieop", "!hetluktnimeer"]),

           ReplyAnswer(lambda m: choice(['!ikook',
                                         "Das oke, iedereen moet soms z'n gevoelens uiten, je geraakt wel door deze examenperiode, YOU CAN DO THIS!",
                                         "Je gaat de examens knallen!",
                                         "https://tenor.com/view/mochi-peachcat-mochi-peachcat-hug-pat-gif-19092449",
                                         "Je bent ni alleen, we zitten allemaal samen in de Discord om er samen door te geraken!",
                                         "Da komt allemaal wel goed!",
                                         "Zou je je niet vervelen met 3 maanden vakantie?",
                                         "YES WE CAN! Probeer da luidop te zeggen, da geeft echt extra motivatie #marathonradio"]),
                       exact_trigger=["!ikwilwenen"]),

           ReplyAnswer(lambda m: re.match("-say (.*)", m.get_exact_content()).group(1), regex_trigger="-say (.*)", as_reply=False, delete_message=True),

           ReplyAnswer(
               lambda m: f"Hey {re.match('[iI]?k[ ]?ben (.*)', m.get_exact_content()).group(1)}, ik ben Bollekebot!",
               regex_trigger="[iI]?k[ ]?ben (.*)", prob=0.2),

           ReactAnswer(lambda m: re.match("-react (.*)", m.get_exact_content()).group(1), regex_trigger="-react (.*)", on_replied=True, delete_message=True),

           ReactAnswer("fact", exact_trigger="Catoe moet pottoe!", bot_only=True),
           ReactAnswer("😢", substrings_trigger="you have been unsubscribed due to inactivity!", bot_only=True),

           ReactAnswer("lies",
                       substrings_trigger="you will be unsubscribed on the next stage if you do not reply or react to this message.",
                       active_users="Lies"),

           ReplyAnswer("Have you tried turning it off and on again?",
                       custom_trigger=lambda m: (m.contains_substring("help") or m.contains_substring("fix"))
                                                and m.contains_substring("?", match_case=True)),

           ReactAnswer("🥴", active_users="Alexander", prob=0.1),
           ReplyAnswer(lambda m: f"Je hebt {randint(0, 20)}/20", words_trigger="punten", prob=0.3),
           ReplyAnswer(lambda m: get_alphabet_str(), exact_trigger="-alphabet"),

           ReplyAnswer(lambda m: "NEGATIEF" if random() > 0.5 else "POSITIEF",
                       custom_trigger=lambda m: m.contains_word("coronatest") or (
                               m.contains_word("corona") and m.contains_word("test"))),
           ReplyAnswer("*WINAK", words_trigger=["winak", "Winak"]),
           ReplyAnswer("", image="boommarter.png", words_trigger="boommarter")
           ]

answers += react_answers
answers += reply_answers