from gensim.models import word2vec
import pickle
from scipy import spatial
from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    with open('../chapter09/85_feature','rb') as data:
        model = pickle.load(data)
    with open('family.txt') as data, open('family_92_85.txt','w') as data_after:
        for i,line in enumerate(data):
            print(i)
            line_s = line.split()
            try:
                result = defaultdict(float)
                vec = (np.array(model[line_s[1]]) - np.array(model[line_s[0]]) + np.array(model[line_s[2]])).tolist()
                for co in model.keys():
                    result[co] = spatial.distance.cosine(vec,model[co])
                for co,val in sorted(result.items(),key=lambda x: x[1]):
                    data_after.write('{} {} {}\n'.format(line.strip(),co,1-val))
                    break
            except:
                data_after.write('{} {} {}\n'.format(line.strip(),'NoData',-1))

    print('90_data')
    model = word2vec.Word2Vec.load('knock90.model')
    with open('family.txt') as data, open('family_92.txt','w') as data_after:
        for line in data:
            line_s = line.split()
            try:
                result = model.most_similar(positive=[line_s[1],line_s[2]],negative=[line[0]],topn=1)
            except:
                result[0] = ('NoData',-1)
            data_after.write('{} {} {}\n'.format(line.strip(),result[0][0],result[0][1]))
