import nltk
from nltk.corpus import stopwords

def search_stopword(word):
    return word in stopwords.words('english')

if __name__ == '__main__':
    with open('sentiment.txt', 'r') as f:
        for line in f:
            words = line.split()
            del words[0]
            for word in words:
                if search_stopword(word):
                    print(word)
