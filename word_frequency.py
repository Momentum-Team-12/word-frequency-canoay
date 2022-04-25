from pickle import STOP
from pprint import pprint


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# PUNCTUATION = [",", ".", "-", "!", "?", "'"]



def print_word_freq(file):
    """Read in `file` and print out the 
    frequency of words in that file."""
    import string
    from collections import Counter
    from nltk import FreqDist
    # import numpy as np
    # import pandas as pd
    # 'r' is for read only mode, 'w' would be for write
# 'yourfile.txt' should be the relative path to your file
    with open(file, 'r') as f:
    # code to read and process the file goes here, where the file is referred to as f.
    # when the indented code block stops, Python will close the file, and f will no longer be defined
    # read() converts the file to a string
        file_string = f.read()
    # splitlines() will return a list with each element being a line in the file
        removed_punctuation_file_string = file_string.translate(str.maketrans('', '', string.punctuation)) 
        file_lowercase = removed_punctuation_file_string.lower()
        file_lowercase_list = file_lowercase.split()
        result_list  = [word for word in file_lowercase_list if word not in STOP_WORDS]
        result = ' '.join(result_list)
        word_list = result.split()
        # print(word_list)
        # word_count =set()
        # for item in result:
        #     word_count.add((item, string.count(item)))
        # print(word_count)
        fdist1 = FreqDist(word_list)
        # print(fdist1)
        print(fdist1.most_common())
#         file_list = file_string.splitlines()
#     # strip() and split() can also be helpful in this process.

# # this will print out one line at a time
#     for line in file_list:   
#         line.pop(PUNCTUATION)
#         print(line)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
