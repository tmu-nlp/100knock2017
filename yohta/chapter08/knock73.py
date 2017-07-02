from knock72 import pn_list,word_id
from sklearn.linear_model import LogisticRegression
#from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
import numpy as np


lr = LogisticRegression()
#stem_vec = DictVectorizer().fit_transform(stem_list)
#print(stem_vec)
lr.fit(word_id, pn_list)
joblib.dump(lr, 'lr.pkl')
#joblib.dump(stem_vec, 'vector.pkl')
#print(np.shape(pn_list))
