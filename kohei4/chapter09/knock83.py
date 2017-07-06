"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語ttと文脈語ccの共起回数
f(t,∗): 単語ttの出現回数
f(∗,c): 文脈語ccの出現回数
NN: 単語と文脈語のペアの総出現回数
"""

import bz2
import re
import random
from collections import Counter
import pickle


    #print(country)

if __name__ == "__main__":

    f_t_c = Counter()
    f_t_ = Counter()
    f__c = Counter()
    NN = 0

    with open('80corpus_context_2.txt','r') as ff:
        for ii, line in enumerate(ff):
            #if ii >= 0 and ii <= 10:
                word, context = line.strip().split('\t')
                #print(word, context)
                f_t_c[word,context] += 1
                f_t_[word] += 1
                f__c[context] += 1
                NN += 1


    with open('80corpus_f_t_c_','wb') as f_t_c_file:
        pickle.dump([f_t_c,f_t_,f__c,NN],f_t_c_file)
    #print(f_t_c)
    #print(f_t_)
    #print(f__c)
    #print(NN)
