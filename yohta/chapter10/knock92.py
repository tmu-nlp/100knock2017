import pickle
import numpy as np
from gensim.models import word2vec

def similarity_rank_vec(target_vec,words,matrix):
    vec_t = target_vec
    rank_list = []
    for word in words:
#        if word == target:
#            continue
        vec_w = vector[words[word]]
        rank_list.append((word,cos_similarity(vec_t,vec_w)))
    rank_list.sort(key=lambda x:x[1],reverse = True)
    return rank_list

def cos_similarity(vec1, vec2):
    if (np.linalg.norm(vec1) * np.linalg.norm(vec2) == 0):
        return 0
    else:
        return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

if __name__ == '__main__':
    with open('../chapter09/data/answer85','rb') as a85,open('data/answer91.txt') as i_f,open('data/answer92_85.txt','w') as o_85_f:
        words,vector = pickle.load(a85)
        for i,line in enumerate(i_f):
            best = 0
            line = line.lower()
            tokens = line.split()
            try:
                tar_vec = vector[words[tokens[1]]] - vector[words[tokens[0]]] + vector[words[tokens[2]]]
            #    print(tokens[1],tokens[0],tokens[2])
                for word in words:
                    vec_w = vector[words[word]]
                    if best <= cos_similarity(tar_vec,vec_w):
                        best = cos_similarity(tar_vec,vec_w)
                        best_word = word
                o_85_f.write('{}\t{}\t{}\n'.format(i+1,best_word,best))
            except:
                o_85_f.write("{}\tNone\t-1\n".format(i+1))
                continue
    with open('data/answer91.txt') as i_f,open('data/answer92_90.txt','w') as o_90_f:
        model = word2vec.Word2Vec.load('knock90.model')
        for i,line in enumerate(i_f):
            line = line.lower()
            try:
                tokens = line.strip().split()
                x = model.most_similar(positive=[tokens[1],tokens[2]],negative=[tokens[0]],topn=1)
                o_90_f.write('{}\t{}\t{}\n'.format(i+1,x[0][0],x[0][1]))
            except:
                o_90_f.write('{}\t{}\t{}\n'.format(i+1,None,-1))
