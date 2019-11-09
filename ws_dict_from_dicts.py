from collections import defaultdict
import logging

# CREATE PYTHON DICT FROM ENGLISH DICT
# Open dictionary txt file
# Read in each word
# Get a set of the unqiue letters per word
# Save both to dict with set letters as key
# Using collections allows for multiple values per key
# Also find the longest word in list to set permutation length (actually no, not using)

logging.info("in wordscramble-dict_from_dicts.py")


def main():
    dict_list = defaultdict(list)
    word_length = 0

    #with open("/home/fred/my_app/aa_python/static/eng_dict.txt") as f:
    with open("/home/fred/my_app/aa_python/static/sowpods.txt") as f:  # scrabble dictionary
        for row in f:
            word = row.rstrip("\n\r")
            set_letters = set(word)
            set_concat_into_string = ''.join(set_letters).upper()
            dict_list[set_concat_into_string].append(word)

            if len(word) > word_length:
                word_length = len(word)

    return dict_list
    #print dict_list
    #print "WORD LENGTH", word_length

    #return dict_list

    #logging.info("WORD LIST", dict_list)