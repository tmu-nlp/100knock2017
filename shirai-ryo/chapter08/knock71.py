import nltk
from nltk.corpus import stopwords

"""
参考
http://qiita.com/HirofumiYashima/items/e588ea80deac090bc4b3
もっといいところありそう
"""

# print(stopwords.words('english'))

def search_stopwords(word):
    if word in stopwords.words("english"):
        return True
    else:
        return False


if __name__ == "__main__":
    test = "i"
    print(search_stopwords(test))
