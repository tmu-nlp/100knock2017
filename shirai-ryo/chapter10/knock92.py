from gensim.models import word2vec
import numpy as np
from scipy import spatial
import pickle
from collections import defaultdict

# 例外を発生しうるコードをtry:で括ります。そして例外が発生した場合の処理をexcept 例外の種類 :で括ります。
# 参考：http://qiita.com/Usek/items/53527feba2adcb386aa8

with open("../chapter09/85.pickle", "rb") as data:
    model = pickle.load(data)
with open("91_family.txt", "r") as fami_91, open("92_family85.txt", "w") as fami_92:
    for line in fami_91:
        words = line.split()
        try:
            result = defaultdict(float)
            vec = (np.array(model[words[1]]) - np.array(model[words[0]]) + np.array(model[words[2]])).tolist()
            for cos in model.keys():
                result[cos] = spatial.distance.cosine(vec,model[cos])
            for cos, val in sorted(result.items(), key=lambda x:x[1]):
                fami_92.write("{} {} {}\n".format(line.strip(), cos , 1-val))
                break
        except:
            fami_92.write("{} {} {}\n".format(line.strip(), 'nodata', 0))


model = word2vec.Word2Vec.load('91.model')
with open("91_family.txt", "r") as fami_91, open("92_family", "w") as fami_92:
    for line in fami_91:
        words = line.split()
        try:
            result = model.most_similar(positive=[words[1],words[2]],negative=[line[0]],topn=1)
        except:
            result[0] = ('nodata',0)
        fami_92.write('{} {} {}\n'.format(line.strip(),result[0][0],result[0][1]))
