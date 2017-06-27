from nltk import stem
from nltk.corpus import stopwords
from collections import defaultdict
import numpy as np
import pickle


def preprocessor_words(words):
    stopwords_set = set(stopwords.words('english'))
    stemmer = stem.LancasterStemmer()

    words_preprocessed = []
    for word in words:
        if word in stopwords_set:
            continue
        lemmatized = stemmer.stem(word)
        words_preprocessed.append(lemmatized)

    return words_preprocessed


def preprocessor_data(data, ids, test=0):
    stopwords_set = set(stopwords.words('english'))
    stemmer = stem.LancasterStemmer()

    data_in_preprocessed = []
    labels = []

    for line in data:
        words_preprocessed = []
        line.lower()
        label, words = line.split()[0], line.split()[1:]
        labels.append(int(label))

        for word in words:
            if word in stopwords_set:
                continue
            lemmatized = stemmer.stem(word)
            if test == 0:
                ids[lemmatized]
            words_preprocessed.append(lemmatized)
        data_in_preprocessed.append(words_preprocessed)

    return data_in_preprocessed, labels


def create_feature(words, ids, test=0):
    feature = np.zeros(len(ids))
    for word in words:
        if test == 1:
            if word not in ids.keys():
                continue
        feature[ids[word]] += 1

    return feature

if __name__ == '__main__':
    ids = defaultdict(lambda: len(ids))
    with open('result/sentiment.txt', 'r') as data_in:
        data_in_preprocessed, labels = preprocessor_data(data_in, ids)

    with open('result/feature.txt', 'w') as data_out:
        for words in data_in_preprocessed:
            print(create_feature(words, ids), file=data_out)

    with open('result/ids.dump', 'wb') as data_ids_out:
        pickle.dump(dict(ids), data_ids_out)
