from random import random, choice
from config import quotes, letter_emojis


def multi_char_remove(string, chars_to_remove):
    """
    :param string: String to remove the characters from
    :param chars_to_remove: Characters you want to remove from the string
    :return: string with the specified characters removed
    """
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string


def to_list(obj):
    """
    Creates a list containing the object if the object is not yet a list
    """
    if obj is None:
        return None
    if not isinstance(obj, list):
        return [obj]
    return obj


def get_motivational_quote():
    """
    :return: A random quote from the quotes list or a cute gif
    """
    if random() < 0.2:
        return "https://tenor.com/view/motivation-motivational-penguin-gif-14021416"
    elif random() < 0.1:
        return "https://tenor.com/view/polar-bear-cute-ice-bear-gif-19566864"
    else:
        return choice(quotes)


def split_words_phrases(str_list):
    """
    Splits a list of strings into two lists: one containing words and a dictionary containing phrases
    """
    words = []
    phrases = []
    for word in str_list:
        if ' ' in word:
            phrases.append(word)
        else:
            words.append(word)
    return words, phrases


def get_alphabet_str():
    reaction = ""
    for letter in letter_emojis:
        reaction += f"{letter_emojis[letter]}\n"
    return reaction
