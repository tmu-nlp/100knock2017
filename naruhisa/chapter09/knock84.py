import numpy as np
import pickle
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer

def getPpmi(word, context):
    pmi = np.log2(N*co_occur['{}\t{}'.format(word, context)]/count_word[word]/count_context[context])
    return max(pmi, 0)

if __name__ == '__main__':
    feature_list = list()
    word_name = dict() #単語自体が入る
    vectorizer = DictVectorizer()
    with open('f.dumps','rb') as i_f:
        co_occur, count_word, count_context, N = pickle.load(i_f)
    co_words_dict = defaultdict(list)
    for word in co_occur.keys():
        if co_occur[word] < 10:
            continue
        w,c = word.split('\t')
        co_words_dict[w].append(c)
    word_name = dict()
    counter = 0
    for word, co_words in co_words_dict.items():
        word_name[word] = counter
        word_dict = dict()
        for c in co_words:
            word_dict[c] = getPpmi(word, c)
        feature_list.append(word_dict)
        counter += 1
    with open('word_context_matrix.dump', 'wb') as o_f:
        pickle.dump((word_name,vectorizer.fit_transform(feature_list)), o_f)
