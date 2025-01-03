from react_answer import ReactAnswer

always_react = [("p leave", "👋"),
                ("good bot", "😘"),
                ("tea", "🍵"),
                ("cupcake", "🧁"),
                ("bollekebot", "👀"),
                ("bolleke", "🟠"),
                ("cara", "🍻"),
                ("dorien", "🍻"),
                ("alexander", "🥴"),
                ("f", "f"),
                ("repost", "😱"),
                ("ping", "pong"),
                ("sleepy", "😴"),
                ("mila", "😻"),
                ("lies", "🐱"),
                ("¯\_(ツ)_/¯", "🤗"),
                ("hanne", "😄"),
                ("tim", "🚆"),
                ("tjenne", "🪴"),
                (['bad bot', 'kutbot', 'stoeme bot', 'stomme bot'], "😠"),
                (['pussy', '50 shades'], "😏"),
                (['birthday', "verjaardag"], "🥳"),
                (['love', 'liefde', 'hou van'], "😍"),
                (['dead', 'dood'], "🔫"),
                (['king', 'mking', 'deceuninck', 'koning'], "👑"),
                (['sneeuw', 'sneeuwman', 'sneeuwt', 'sneeuwen'], "☃"),
                ('pauze', "⏸"),
                (['slaapwel', "slapen", "dutje", "moe"], "💤"),
                (['eten', 'lunchen', 'dinner', 'voedsel', 'lunch', 'ontbijt', 'breakfast', 'brunch', 'snack', 'snacken',
                'eeten', 'ete', 'etenstijd', 'food', 'lunchables', 'ontbijten'], "🧀")]

sometimes_react = [(["succes", "success"], "❤"),
                   ("studenten", "🥣"),
                   ("69", "nice"),
                   ("lockdown", "🔒⬇"),
                   ("sad", "😢"),
                   ("windows", "🪟💩"),
                   ("linux", "🐧"), ]

rare_react = [("nice", "♋"),
              (['corona', 'covid'], "🤧"),
              ("zevensprong", "🐻🍺"), ]

react_answers = []

for key, value in always_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key))

for key, value in sometimes_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key, prob=0.5))

for key, value in rare_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key, prob=0.1))
