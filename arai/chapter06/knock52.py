from nltk.stem import PorterStemmer

with open('knock51file.txt') as text:
    stemmer = PorterStemmer()
    for word in text:
        #stemmer.stem(word.strip('.'))
        #stemmer.stem(word.strip(','))
        print(word.strip() + '\t' + stemmer.stem(word.strip()))
        
        
