
# coding: utf-8

# In[12]:


import os,random,pickle
from pprint import pprint
from collections import defaultdict
import nltk
lemma = nltk.wordnet.WordNetLemmatizer()


# In[4]:


stopwords=open("./stopwords.txt","r",encoding="utf-8").readlines()


# In[5]:


def isstopword(w):
    if w in stopwords:
        return True
    else:
        return False


# In[20]:


features=[]
labels=[]


# In[21]:


for line in open("./sentiment.txt","r",encoding="utf-8"):
    feature=defaultdict(int)
    label=line[:2]
    sentence=line[3:]
    for w in line.split():
        feature[lemma.lemmatize(w)]+=1
    features.append(feature)
    labels.append(label)


# In[22]:


pickle.dump((labels,features),file=open("features.pkl","wb"))


# In[ ]:




