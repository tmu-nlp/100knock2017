from knock71 import return_TF
from collections import defaultdict
import nltk
import pickle

stemmer = nltk.PorterStemmer()

pn_list = []
stem_list = []
word_ids = defaultdict(lambda :len(word_ids))
def pre(sentence):
    sentence = sentence.replace('-',' ')
    sentence = sentence.replace('[',' ')
    sentence = sentence.replace(']',' ')
    sentence = sentence.replace('\'',' ')
    return sentence

def stemming(word):
    stem_word = stemmer.stem(word)
    create_word_ids(stem_word)
#        stem.append(stem_word)
    return stem_word

def create_word_ids(word):
    word_ids[word]


with open('sentiment.txt','r') as i_f:
    for line in i_f:
        stemmed_sentence = []
        pn,sentence = int(line[:2]),line[3:]
        sentence = pre(sentence)
        words = sentence.split()
        for word in words:
            if return_TF(word):
                continue
            if len(word) <= 1:
                continue
            stemmed_word = stemming(word)
            stemmed_sentence.append(stemmed_word)

        pn_list.append(pn)
        stem_list.append(stemmed_sentence)

with open('sentiment.txt','r') as i_f:
    word_id = []
    for line in i_f:
        sent_word_id = [0] * len(word_ids)
        pn,sentence = int(line[:2]),line[3:]
        sentence = pre(sentence)
        words = sentence.split()
        for word in words:
            if return_TF(word):
                continue
            if len(word) <= 1:
                continue
            stemmed_word = stemming(word)
            sent_word_id[word_ids[stemmed_word]] += 1
        word_id.append(sent_word_id)

with open('word_ids.pkl','wb') as id_f:
    pickle.dump(dict(word_ids),id_f)

if __name__ == "__main__":
    for i in range(len(pn_list)):
        print("{}\t{}".format(pn_list[i], stem_list[i]))

"""
    with open('feature.txt','w') as o_f:
        for i in range(len(stem_list)):
            o_f.write(stem_list[i])
            o_f.write('\n')
"""
