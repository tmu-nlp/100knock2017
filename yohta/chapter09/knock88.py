import pickle
import numpy as np
from knock87 import cos_similarity

with open('data/answer85','rb') as i_f:
    words,vector = pickle.load(i_f)

def similarity_rank(target,words,matrix):
    vec_t = vector[words[target]]
    rank_list = []
    for word in words:
        if word == target:
            continue
        vec_w = vector[words[word]]
        rank_list.append((word,cos_similarity(vec_t,vec_w)))
    rank_list.sort(key=lambda x:x[1],reverse = True)
    return rank_list

if __name__ == '__main__':
    rank = 10
    i = 1
    for word,score in similarity_rank('England',words,vector):
        if i <= rank:
            print('{}\t{}\t{}'.format(i,word,score))
        i += 1
