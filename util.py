from random import random, choice
from config import quotes, letter_emojis, motivation
import numpy as np


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
    if random() < 0.5:
        return choice(motivation)
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


def get_punten():
    punten = -1
    while punten > 20 or punten < 0:
        punten = int(np.random.normal(9, 3))
    punten_message = f"Je hebt {punten}/20, "
    if punten <= 4:
        punten_message += "zet alles van afleidingen opzij en begin weer te studeren, ik geloof in jou, dus stel mij niet teleur!!!"
    elif punten <= 6:
        punten_message += "komaan, je hebt nog wat te doen, maar je kan het!"
    elif punten < 10:
        punten_message += "delibereerbaar, maar nog even op je tanden bijten! Komaan, YOU CAN DO THIS!!!"
    elif punten <= 13:
        punten_message += "das erdoor, maar het kan altijd zijn dat ik je punten fout inschat, dus nog even alles geven en je gaat da examen knallen!"
    else:
        punten_message += " goed bezig! Blijf goed doorstuderen en voor je het weet is dit effectief het aantal punten dat je op je examen krijgt!"
    return punten_message
