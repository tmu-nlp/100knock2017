from nltk.corpus import stopwords
#print (stopwords.words('english')) #今回nltkのstopword listを使用した
def isStop(sentence):
    for word in sentence.strip().split():
        if word.lower() in stopwords.words('english'):
            return True
    return False

if __name__ == '__main__':
    x = 'I am NLPer .'
    print (isStop(x))
