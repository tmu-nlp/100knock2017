from nltk.corpus import stopwords
from nltk import stem
import pickle
from collections import defaultdict

def stop_word_check(word):
    stop_word_list = set(stopwords.words('english'))
    if word in stop_word_list:
        return True
    else:
        return False

def make_feature(f, flag):
    with open(file_name) as f:
        feature = defaultdict(int)
        for i,line in enumerate(f):
            print(i)
            y,x = line.split('\t')
            y = int(y)
            words = x.split()
            for word in words:
                if stop_word_check(word) == False:
                    word = stem.PorterStemmer().stem(word)
                    if flag == 0:
                        feature[word] += 1
                    elif flag == 1:
                        if y == 1:
                            feature[word] += 1
                        elif y == -1:
                            feature[word] -= 1
    return feature

def good_feature_get(feature, th):
    good_feature_ids = defaultdict(lambda:len(good_feature_ids))
    for word, num in feature.items():
        if abs(num) >= th:
            good_feature_ids[word]
    return good_feature_ids

def make_sentence_feature(sen, ids):
    sentence_feature = [0 for i in range(len(ids))]
    words = sen.split()
    for word in words:
        word = stem.PorterStemmer().stem(word)
        if word in ids:
            sentence_feature[ids[word]] += 1
    return sentence_feature

def make_sentence_feature_list(file_name, feature_ids, test = 0):
    with open(file_name) as f:
        sentence_list = []
        label_list = []
        for line in f:
            if test == 0:
                y, sen = line.split('\t')
            else:
                sen = line
            sentence_feature = make_sentence_feature(sen, feature_ids)
            sentence_list.append(sentence_feature)
            label_list.append(int(y))
        sentences = (sentence_list, label_list)
    return sentences

def file_extend(file_name):
    feature_ids = good_feature_get(make_feature(file_name,1),2)
    sen_feature = make_sentence_feature_list(file_name, feature_ids)
    with open('feature.ids','wb') as ids, open('sen_list.feature', 'wb') as sen:
        pickle.dump(dict(feature_ids), ids)
        pickle.dump(sen_feature, sen)

if __name__ == '__main__':
    file_name = 'sentiment.txt'
    file_extend(file_name)
