
# coding: utf-8

# In[1]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[3]:


lg_model=pickle.load(open("./lg_model.pkl","rb"))


# In[4]:


w_ids=pickle.load(open("./w_ids.pkl","rb"))


# In[5]:


def predict_sentence(sent):
    array=np.zeros(len(w_ids))
    for w in sent.split():
        w=lemma.lemmatize(w)
        if w in w_ids:
            array[w_ids[w]]+=1
    return lg_model.predict(array)
    


# In[15]:


sentence="In the experiment of 76-77,  the  rate, relevance rate, recall rate, and F1 score of polarity classification by 5-way cross validation test."
predict_sentence(sentence)

