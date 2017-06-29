from nltk.corpus import stopwords
def check_stopwords(sentence):
    stop_words = set(stopwords.words('english'))
    s = set(sentence.lower().strip().split(" "))
    for x in s:
        if x in stop_words:
            return True
    return False
if __name__ == '__main__':
    for line in open("sentiment.txt"):
        print(line)
        print(check_stopwords(line))
    
    
