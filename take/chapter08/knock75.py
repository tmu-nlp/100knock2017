from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import numpy as np
import dill
from pprint import pprint
from collections import defaultdict

ids = defaultdict(lambda:len(ids))

try:
    with open('ids.dill', 'rb') as f:
        ids = dill.load(f)
    print("Load ids file succeeded.")
except:
    print("Load ids file failed.")
    
pprint(ids)
try:
    lr = joblib.load('lr.pkl')
    print("Load Model succeeded.")
except:
    print("Load Model Failed.")

import numpy as np
w = np.array(lr.coef_)
sort_index = np.argsort(w)

weight_top10_word = []
weight_bottom10_word = []

weight_top10_ids = sort_index[0][0:10]
weight_bottom10_ids = sort_index[0][-1:-11:-1]

for w, _id in ids.items():
    if _id in weight_top10_ids:
        weight_top10_word.append(w)
    elif _id in weight_bottom10_ids:
        weight_bottom10_word.append(w)

# for v in sort_index[0][0:10]:
#     for _word, _id in ids.items():
#         if int(v) == _id:
#             # weight_top10_word.append(_word)
#             print(_word)
#             break

print('\n------- knock75 -------\n top 10')
pprint(weight_top10_word)
print('\nbottom 10')
pprint(weight_bottom10_word)
