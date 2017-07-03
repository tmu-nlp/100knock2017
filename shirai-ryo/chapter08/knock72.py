
from nltk.corpus import stopwords
# from stemming.porter2 import stem
# from nltk import stem
# stemmer = stem.PorterStemmer() でもいけるのかな？
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
import pickle
def create_feature():
    stop_words = set(stopwords.words('english'))
    labels = []
    stems = []
    for line in open("sentiment.txt"):
        label, content = line.strip().split("\t")
        # knock71でラベルをタグで分ける必要あり
        words = content.lower().split(" ")
        s = [x for x in words if x not in stop_words]
        # s = []
        # for x in words:
        #     if x not in stop_words:
        #         s.append(x)
        stems.append(s)
        labels.append(int(label))

    features = []
    for s in stems:
        features.append(to_feature_dict(s))

    return features, labels, dict_to_vector(features)

def dict_to_vector(d):
    v = DictVectorizer(sparse=False)
    # 下に解説をメモしてあリマスよ
    X = v.fit_transform(d)
    return X

def to_feature_dict(s):
    d = defaultdict(int)
    for w in s:
        d[w] += 1
    return d

if __name__ == '__main__':
    data = create_feature()
    pickle.dump(data, open("data.pickle", "wb" ) )



# ちなみに最近Pythonの機械学習ライブラリであるscikit-learnを使っているのですが、
# DictVectorizerというのを使うと二値化もやってくれるみたいです。


"""

from sklearn.feature_extraction import DictVectorizer
Transforms lists of feature-value mappings to vectors.

〜〜example〜〜
>>> from sklearn.feature_extraction import DictVectorizer
>>> v = DictVectorizer(sparse=False)
>>> D = [{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}]
>>> X = v.fit_transform(D)
>>> X
array([[ 2.,  0.,  1.],
       [ 0.,  1.,  3.]])
>>> v.inverse_transform(X) ==         [{'bar': 2.0, 'foo': 1.0}, {'baz': 1.0, 'foo': 3.0}]
True
>>> v.transform({'foo': 4, 'unseen_feature': 3})
array([[ 0.,  0.,  4.]])

"""


"""

scikit-learnでは学習する場合にはfit、
推定する場合にはpredictというように、
アルゴリズムに関わらず統一されたインターフェースになっているそうです。

"""




"""
import nltk
from nltk.corpus import stopwords
from nltk import stem

stemmer = stem.PorterStemmer()

with open("sentiment.txt") as text, open("sosei.txt", "w") as s_text:
    for line in text:
        new_list = []
        words = line.split()
        new_list.append(words[0])
        del words[0]
        for word in words:
            if word in stopwords.words("english"):
                pass
            else:
                new_list.append(stemmer.stem(word))
        s_text.write(" ".join(new_list) + "\n")

            # if word in stopwords.words('english'):
            #     del
"""
