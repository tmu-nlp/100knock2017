from nltk.corpus import stopwords
from stemming.porter2 import stem
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
import pickle
def create_feature():
    stop_words = set(stopwords.words('english'))
    labels = []
    stems = []
    for line in open("sentiment.txt"):
        label, content = line.strip().split("\t")
        words = content.lower().split(" ")
        s = [x for x in words if x not in stop_words]
        stems.append(s)
        labels.append(int(label))
    
    features = []
    for s in stems:
        features.append(to_feature_dict(s))
        
    return features, labels, dict_to_vector(features)
def dict_to_vector(d):
    v = DictVectorizer(sparse=False)
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
