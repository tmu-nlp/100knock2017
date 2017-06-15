import nltk
from knock51 import split_word
stemmer = nltk.PorterStemmer()

for word in split_word():
    word = word.strip(',')
    word = word.strip('.')
    print('{}\t{}'.format(word, stemmer.stem(word)))
