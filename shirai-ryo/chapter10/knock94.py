# 92と同じような感じでやればおkっぽい

from gensim.models import word2vec
import numpy as np
from scipy import spatial
import pickle
from collections import defaultdict

# 85のほう
with open('../chapter09/85.pickle', 'rb') as in_text, open('combined.tab', 'r') as text, open('94_combined85.txt', 'w') as out_text:
    model = pickle.load(in_text)
    for line in text:
        words = line.split('\t')
        try:
            val = spatial.distance.cosine(model[words[0]],model[words[1]])
            if val < 0:
                val = 0
                    # この値が1に近いほど類似度が高く、0に近いほど類似度が低いことを表します。
        except:
            val = 1
        out_text.write('{} {}\n'.format(line.strip(),1-val))


# 90のほう
#with open("91.model", 'r') as in_text,
model = word2vec.Word2Vec.load('91.model')
with open("combined.tab", 'r') as text, open("94_combined.txt", 'w') as out_text:
    # model = word2vec.Word2Vec.load(in_text)
    for line in text:
        words = line.split('\t')
        try:
            result = model.similarity(words[0],words[1])
            if result < 0:
                result = 0
        except:
            result = -1
        out_text.write('{} {}\n'.format(line.strip(),result))
