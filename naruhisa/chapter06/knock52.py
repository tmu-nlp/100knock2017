import nltk
from knock50 import get_sentence

stmr = nltk.PorterStemmer()

for line in get_sentence():
    for word in line.strip().split(' '):
        word = word.replace(',', '').replace('.', '')
        print(word + '\t' + stmr.stem(word))
    print()
