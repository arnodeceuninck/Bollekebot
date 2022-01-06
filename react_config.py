from react_answer import ReactAnswer

always_react = [("p leave", "👋"),
                ("good bot", "😘"),
                ("tea", "🍵"),
                ("cupcake", "🧁"),
                ("lockdown", "🔒⬇"),
                ("se", "🤮"),
                ("bollekebot", "👀"),
                ("bolleke", "🟠"),
                ("sad", "😢"),
                ("cara", "🍻"),
                ("anne marie", "❤"),
                ("dorien", "🍻"),
                ("gitte", "💜"),
                ("alexander", "🥴"),
                ("f", "f"),
                ("69", "nice"),
                ("windows", "🪟💩"),
                ("linux", "🐧"),
                ("repost", "😱"),
                ("ping", "pong"),
                ("sleepy", "😴"),
                ("mila", "😻"),
                ("lies", "🐱"),
                ("¯\_(ツ)_/¯", "🤗"),
                ("zevensprong", "🐻🍺"),
                ("studenten", "🥣"),
                ("hanne", "😄"),
                ("tim", "🚆"),
                ("tjenne", "🪴"),
                (['bad bot', 'kutbot', 'stoeme bot', 'stomme bot'], "😠"),
                (['pussy', '50 shades'], "😏"),
                (['birthday', "verjaardag"], "🥳"),
                (['love', 'liefde', 'hou van'], "😍"),
                (['dead', 'dood'], "🔫"),
                (['corona', 'covid'], "🤧"),
                (['king', 'mking', 'deceuninck', 'koning'], "👑"),
                (['sneeuw', 'sneeuwman', 'sneeuwt', 'sneeuwen'], "☃")]

sometimes_react = [(["succes", "success"], "❤")]

rare_react = [("nice", "♋")]

react_answers = []

for key, value in always_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key))

for key, value in sometimes_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key, prob=0.5))

for key, value in rare_react:
    react_answers.append(ReactAnswer(value, words_substr_triggers=key, prob=0.1))