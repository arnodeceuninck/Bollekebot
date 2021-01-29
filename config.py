linux_copy_pasta = "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called \"Linux\", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\nThere really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called \"Linux\" distributions are really distributions of GNU/Linux."

# Non case sensitive, keys must be words
responses = {"slapen": "Slaapwel!",
             "kat": "Miauw",
             "hond": "Woef",
             "haan": "Kukeleku",
             "vis": "Blub",
             "linux": linux_copy_pasta,
             "slok of gene slok": "WINOK",
             "water": "WATER?! Wil je me soms vergiftigen ofzo?",
             "anne-marie": "*Anne Marie",
             "i'm blue": "Da ba dee da ba da"
             }
# Multiple keys with same value
responses.update(dict.fromkeys(
    ['eten', 'lunchen', 'dinner', 'voedsel', 'lunch', 'ontbijt', 'breakfast', 'brunch', 'snack', 'snacken', 'eeten',
     'ete', 'etenstijd', 'food', 'lunchables', 'ontbijten'],
    "Smakelijk!"))
responses.update(dict.fromkeys(['vos', 'fox'], "Ring-ding-ding-ding-dingeringeding!"))
responses.update(dict.fromkeys(['aescu', 'aesculapia'], "ieuw"))

emojis = {"p leave": "👋",
          "good bot": "😘",
          "tea": "🍵",
          "cupcake": "🧁",
          "lockdown": "🔒⬇",
          "se": "🤮",
          'bollekebot': "👀",
          "weyts": "💩",
          "bolleke": "🟠",
          "sad": "😢",
          "cara": "🍻",
          "anne marie": "❤",
          "dorien": "🍻",
          "gitte": "💜",
          "alexander": "🥴",
          "f": "f",
          "nice": "♋",
          "69": "nice",
          "windows": "🪟💩",
          "linux": "🐧",
          "repost": "😱",
          "ping": "pong",
          "sleepy": "😴",
          "mila": "😻",
          "lies": "🐱",
          "¯\_(ツ)_/¯": "🤗",
          "zevensprong": "🐻🍺",
          "studenten": "🥣",
          "hanne": "😄",
          "tim": "🚆",
          "tjenne": "🪴"
          }

emojis.update(dict.fromkeys(['bad bot', 'kutbot', 'stoeme bot', 'stomme bot'], "😠"))
emojis.update(dict.fromkeys(['pussy', '50 shades'], "😏"))
emojis.update(dict.fromkeys(['birthday', "verjaardag"], "🥳"))
emojis.update(dict.fromkeys(['love', 'liefde', 'hou van'], "😍"))
emojis.update(dict.fromkeys(['dead', 'dood'], "🔫"))
emojis.update(dict.fromkeys(['corona', 'covid'], "🤧"))
emojis.update(dict.fromkeys(['king', 'mking', 'deceuninck', 'koning'], "👑"))
emojis.update(dict.fromkeys(['sneeuw', 'sneeuwman', 'sneeuwt', 'sneeuwen'], "☃"))
emojis.update(dict.fromkeys(["succes", "success"], "❤"))
