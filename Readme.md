## Structure
- [react_anwer.py](react_anwer.py): Configure automatic reactions on messages
- [reply_config.py](reply_answer.py): Configure automatic replies on messages
- [answer_config.py](answer_config.py): Brings all automatic messages together and contains a list of special message replies/reactions
- [bot.py](bot.py): Main script to run the bot. You should update the token here.
- [config.py](config.py): Shouldn't contain any imports. Contains some config variables.
- [message.py](message.py): Wrapper around Discord message, so e.g. the message doesn't have to be splitted again in words each time.
- [answer.py](answer.py): Superclass for handling a message
- [reply_answer.py](reply_answer.py): Class for a reply on a message
- [react_answer.py](react_answer.py): Class for a reaction on a message
- [discord_util.py](discord_util.py): Contains some Discord related util functions
- [util.py](util.py): Contains some util functions
- [text_parser.py](text_parser.py): Extracts all specific regex matches from a file, e.g. for extracting quotes from a html page

Note: Be careful with imports. 

## TODO's
- Roll a dice of specified size
- Numbers in add_reactions
- Automatic deployment on raspberry pi

## More Bollekebot
There are multiple instances of Bollekebot running. You might be looking for this code:
- message-scheduler: Sadly I can't currently find this code. This schedules messages. 
- [komida-registration-bot](https://github.com/arnodeceuninck/komida-registration-bot): Automatically does the registration at the Komida restaurants for you
- [results-online-sisa](https://github.com/arnodeceuninck/results-online-sisa): Checks whether the results of the exams are online

## Sources
- Old Quotes: https://www.oberlo.com/blog/motivational-quotes
- New Quotes: https://examstudyexpert.com/study-motivation-quotes/, https://liamporritt.com/blog/100-inspirational-study-quotes, https://owlcation.com/academia/Good-luck-messages-for-exams-and-tests-All-the-best-wishes-for-friends-and-family, https://blendtw.com/motivational-quotes-for-exams/, https://www.elle.be/nl/83935-20-motiverende-blokquotes.html, https://sowiso.nl/blog/20-quotes-voor-docenten-en-studenten/, https://sillidria.wixsite.com/priscilla/single-post/2017/10/09/motivatie-quotes, https://worldscholarshipforum.com/nl/45-powerful-motivational-quotes-students/, https://www.designwizard.com/blog/inspirational-quotes-for-students
- Cute animals: https://unsplash.com/s/photos/cute-animal