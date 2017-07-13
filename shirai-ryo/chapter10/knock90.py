from gensim.models import word2vec
import numpy as np
from scipy import spatial

"""
# # 参考 http://m0t0k1ch1st0ry.com/blog/2016/08/28/word2vec/
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentence = word2vec.Text8Corpus("../chapter09/corpus81.txt")
# sentence = word2vec.LineSentence("../chapter09/corpus81.txt")
# どっちがいいの
model = word2vec.Word2Vec(sentence)
model.save("91.model")

81なのに間違えて91っていう名前にしてしまったけど時間かかるのであとで直す余裕があったら改名する

時間かかるので一回やったあとコメントアウトした

"""

x = word2vec.Word2Vec.load('91.model')

#knock86
print("knock86")
print(x["United_States"])
print()
#knock87
print("knock87")
america1 = x["United_States"]
america2 = x["US"]
result = 1 - spatial.distance.cosine(america1, america2)
print(result)
print()
#knock88
print("knock88")
result_2 = x.most_similar(positive=['England'])
i = 0
for j in result_2:
    print(j)
    i += 1
    if i == 10:
        break
print()
#knock89
print("knock89")
vec = (np.array(x['Spain']) - np.array(x['Madrid']) + np.array(x['Athens'])).tolist()
result_3 = x.most_similar(positive=['Spain','Athens'], negative=['Madrid'])
i = 0
for j in result_3:
    print(j)
    i += 1
    if i >= 10:
        break
