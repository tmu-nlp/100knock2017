from gensim.models import word2vec
import pickle
from scipy import spatial
from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    print('85_data')
    with open('../chapter09/85_feature','rb') as data:
        model = pickle.load(data)
    with open('combined.tab') as data, open('combined_94_85.txt','w') as data_after:
        for i,line in enumerate(data):
            print(i)
            line_s = line.split('\t')
            try:
                val = spatial.distance.cosine(model[line_s[0]],model[line_s[1]])
                if val < 0:
                    val = 0
            except:
                val = 1
            data_after.write('{} {}\n'.format(line.strip(),1-val))

    print('90_data')
    model = word2vec.Word2Vec.load('knock90.model')
    with open('combined.tab') as data, open('combined_94.txt','w') as data_after:
        for line in data:
            line_s = line.split('\t')
            try:
                result = model.similarity(line_s[0],line_s[1])
                if result < 0:
                    result = 0
            except:
                result = -1
            data_after.write('{} {}\n'.format(line.strip(),result))
