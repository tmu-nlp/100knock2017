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
    with open('word_context_freq.dump','rb') as i_f:
        co_occur, count_word, count_context, N = pickle.load(i_f)
    """
    for i, word in enumerate(count_word.keys()):
        if i%100==0:
            print (i)
        word_dict = dict() #そのwordの素性が入る
        word_name[word] = i #そのwordのindexが入る
        for c in count_context.keys():
            if not '{}\t{}'.format(word, c) in co_occur:
                continue
            if co_occur['{}\t{}'.format(word, c)] < 10:
                continue
            word_dict[c] = getPpmi(word, c)
        feature_list.append(word_dict)    
    """
    print ('word_context_dict')
    #ある単語と狂喜しているcontextを辞書で記憶する
    co_words_dict = defaultdict(list)
    for word in co_occur.keys():
        if co_occur[word] < 10:
            continue
        w,c = word.split('\t')
        co_words_dict[w].append(c)
    print ('start to summarize feature')
    #それぞれの単語に対してkeyをcontext,valueをppmiにした辞書を作成する 
    word_name = dict()
    counter = 0
    for word, co_words in co_words_dict.items():
        if counter%10000==0:
            print (counter)
        word_name[word] = counter #その単語のindexが入る
        word_dict = dict() #その単語の素性が入る
        for c in co_words:
            word_dict[c] = getPpmi(word, c)
        feature_list.append(word_dict)
        counter += 1

    print ('finish to make the list')
    #print (vectorizer.fit_transform(feature_list).toarray())
    with open('word_context_matrix.dump', 'wb') as o_f:
        pickle.dump((word_name,vectorizer.fit_transform(feature_list)), o_f)
