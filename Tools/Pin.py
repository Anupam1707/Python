from random import *
import os
from time import *

pwd = input("Enter a Password : ")

def generate_words(characters, current_word, all_words, length, target_word):
    if length == 0:
        all_words.append(current_word)
        print(current_word)
        if current_word == target_word:
            print("Password found:", current_word)
            print("Your password is among top",len(all_words),"passwords used")
            sleep(15)
            return True
        return False

    for i in range(len(characters)):
        if generate_words(characters, str(current_word) + str(characters[i]), all_words, length - 1, target_word):
            return True
    return False

characters = [0,1,2,3,4,5,6,7,8,9]
all_words = []
word_length = len(pwd)
target_word = pwd

if generate_words(characters, "", all_words, word_length, target_word):
    print("Password found in generated words.")
else:
    print("Password not found in generated words.")
