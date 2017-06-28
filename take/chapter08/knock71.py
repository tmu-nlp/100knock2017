from nltk.corpus import stopwords

stoplist = stopwords.words('english')

def is_stopword(word:str):
    if not len(word) > 0:
        raise TypeError("Required argument not found")
    return word in stoplist

