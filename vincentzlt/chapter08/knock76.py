
# coding: utf-8

# In[67]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
from collections import Counter
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[68]:


lg_model=pickle.load(open("./lg_model.pkl","rb"))
labels,arrays=pickle.load(open("./arrays.pkl","rb"))


# In[69]:


predicted_labels=[]
predicted_proba=[]
for array in arrays:
    predicted_proba.append(lg_model.predict_proba(array.reshape(1,-1)))
    predicted_labels.append(lg_model.predict(array.reshape(1,-1)))


# In[70]:


with open("lg_output.txt","w",encoding="utf-8") as f:
    for idx,(label,pred_label,pred_prob) in enumerate(zip(list(labels),predicted_labels,list(predicted_proba))):
        if idx%100==0:
            print("processing sentence number {}.".format(idx))
        f.write("{}\t{}\t{},{}\n".format(label,pred_label[0],pred_prob[0][0],pred_prob[0][1]))


# In[ ]:




