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

Note: Be careful with imports. 

## TODO's
- Roll a dice of specified size
- Numbers in add_reactions
- Automatic deployment on raspberry pi

## Sources
- Old Quotes: https://www.oberlo.com/blog/motivational-quotes
- New Quotes: https://examstudyexpert.com/study-motivation-quotes/, https://liamporritt.com/blog/100-inspirational-study-quotes, https://owlcation.com/academia/Good-luck-messages-for-exams-and-tests-All-the-best-wishes-for-friends-and-family