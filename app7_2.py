import requests
import random

full_word = input("word: ")
list_of_letters = list(full_word)

def get_words(letter):
    word_list = set()
    request = requests.get(f"https://api.datamuse.com/words?sp={letter}*")
    response_body = request.text
    res = response_body.split('"')
    for i in res:
        if i.startswith(letter):
            word_list.add(i)
    print(random.choice(tuple(word_list)))
    return


def foreach(get_words, list_of_letters):
    for letter in list_of_letters:
        get_words(letter)
    return

foreach(get_words, list_of_letters)

