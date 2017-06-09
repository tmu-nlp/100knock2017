import sys
from knock50 import separate_sentence

def separate_word():
    for line in separate_sentence():
        line = line.split(' ')
        for word_sep in line:
            yield word_sep

if __name__ == '__main__':
    for word in separate_word():
        print(word)
