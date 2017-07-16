import pickle
import numpy as np
from gensim.models import word2vec


def cos_similarity(vec1, vec2):
    if (np.linalg.norm(vec1) * np.linalg.norm(vec2) == 0):
        return 0
    else:
        return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

if __name__ == '__main__':
    with open('data/wordsim353/combined.tab') as i_f,open('../chapter09/data/answer85','rb') as a85,open('data/answer94_85.txt','w') as o_f:
    #    print('model-85')
        words,vector = pickle.load(a85)
        for i,line in enumerate(i_f):
            if i == 0:
                continue
            line = line.lower()
            elements = line.strip().split()
            word1 = elements[0]
            word2 = elements[1]
            num = elements[2]
            try:
                vec1 = vector[words[word1]]
                vec2 = vector[words[word2]]
                score = cos_similarity(vec1,vec2)
                o_f.write('{}\t{}\t{}\t{}\n'.format(word1,word2,num,score))
            except:
                o_f.write('{}\t{}\t{}\t-1\n'.format(word1,word2,num))
    with open('data/wordsim353/combined.tab') as i_f,open('data/answer94_90.txt','w') as o_f:
    #    print('\nmodel-90')
        model = word2vec.Word2Vec.load('knock90.model')
        for i,line in enumerate(i_f):
            if i == 0:
                continue
            line = line.lower()
            elements = line.strip().split()
            word1 = elements[0]
            word2 = elements[1]
            num = elements[2]
            try:
                score = model.similarity(word1,word2)
                o_f.write('{}\t{}\t{}\t{}\n'.format(word1,word2,num,score))
            except:
                o_f.write('{}\t{}\t{}\t-1\n'.format(word1,word2,num))
