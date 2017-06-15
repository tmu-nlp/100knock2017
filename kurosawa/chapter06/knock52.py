import sys
from nltk import stem
from knock51 import separate_word

def stemming_porter():
    for word_stem in separate_word():
        stemmer = stem.PorterStemmer()
        yield (word_stem,stemmer.stem(word_stem))

if __name__ == '__main__':
    for word,stemming in stemming_porter():
        print('{}\t{}'.format(word,stemming))

