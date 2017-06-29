"""
ストップワード除去->stemming->単語(uni)の頻度？
"""
from collections import defaultdict
from nltk.corpus import stopwords
import nltk
import pickle
stemmer = nltk.PorterStemmer()

def excludeStop(sentence):
   word_list = list()
   for word in sentence.split():
        if not word.lower() in stopwords.words('english'):
            word_list.append(word)
   return word_list

def stemming(input_list):
    word_list = list()
    for word in input_list:
        word_list.append(stemmer.stem(word))    
    return word_list

def create_feature(input_list):
    phi = defaultdict(int)
    for word in input_list:
        phi[word.lower()] += 1    
    return phi

if __name__ == '__main__':
    phi = dict()
    """
    with open('sentiment.txt') as i_f:
        for line in i_f:
            tag, x = line.strip().split(' ', 1)
            for word in stemming(excludeStop(x)):
                phi[word] = 0
    print ('make feature')
    """
    feature_list = list()
    with open('sentiment.txt') as i_f:
        for line in i_f:
            phi = dict()
            tag, x = line.strip().split(' ', 1)
            phi = create_feature(stemming(excludeStop(x)))
            feature_list.append([tag, x, dict(phi)]) 
    with open('features.dump', 'wb') as f_f:
        pickle.dump(feature_list, f_f)
