from itertools import combinations
from itertools import permutations
from random import shuffle
from collections import defaultdict
import time
from threading import Thread
import sys


# CREATE THE SCRAMBLE
# Turn the consonants and vowel strings into lists so picking random is easier
# Randomly choose x number of unique letters from each string
# Concatenate back into single string for easier evaluation against others

def main(dict_list):
    print "in new game main"
    dict_list = dict_list
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    vowels = "AEIOU"
    consonant_list = list(consonants)
    vowel_list = list(vowels)

    scramble_list = []
    scramble_length = 6

    shuffle(vowel_list)
    scramble_list.append(''.join(vowel_list[:2]))
    shuffle(consonant_list)
    scramble_list.append(''.join(consonant_list[:4]))

    scramble_string = ''.join(scramble_list)
    #print "SCRAMBLE STRING: ", scramble_string


    # CREATE PIECES OF WORDS
    # Not 100% sure how it works but creates all the possible 1-x letter combos of the words

    word_pieces = []

    for i in range(1, scramble_length + 1, 1):
        comb = combinations(scramble_string, i)
        for l in list(comb):
            word_pieces.append(''.join(l))

    #print "WORD PIECES: ", word_pieces

    # CREATE LIST OF ACCEPTABLE WORDS
    # Take the list of word pieces
    # Iterate through defaultdict keys
    # When there's a match, add all the values to the acceptable words list

    acceptable_words = []
    for word in word_pieces:
        for k, v in dict_list.iteritems():
            if sorted(word) == sorted(k):
               #print "Word = " + word + " key = " + str(k) + " values = " + str(v)
               acceptable_words.append(v)

    acceptable_list_long = [item for sublist in acceptable_words for item in sublist]


    # REMOVE WORD PIECES UNDER 3 CHAR
    # Probably could be done above, but I don't totally get that code
    acceptable_list = [word for word in acceptable_list_long if len(word) > 2]


    # SORT BY LENGTH THEN ALPHABETICALLY
    acceptable_list.sort()
    acceptable_list.sort(key=len)

    #print "ACCEPTABLE LIST POST SORT", acceptable_list


    number_of_answers = len(acceptable_list)
    #print "ACCEPTABLE WORDS", acceptable_list
    #print "LIST LENGTH = ", len(acceptable_list)

    new_game_dict = {
        "scramble_string": scramble_string,
        "acceptable_list": acceptable_list,
        "number_of_answers": number_of_answers
    }

    return new_game_dict  # dict

