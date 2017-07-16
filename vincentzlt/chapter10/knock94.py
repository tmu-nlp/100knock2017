
# coding: utf-8

# In[14]:


import word2vec
from pprint import pprint
from scipy import spatial


# In[5]:


model=word2vec.load("./enwiki-20150112-400-r10-105752.bin")


# In[13]:


analogies=[]
correct=[]
for idx,line in enumerate(open("./wordsim353/combined.tab","r",encoding="utf-8")):
    if idx>0:
        w1,w2,score=line.split("\t")
        score=float(score)
        try:
            sim_cosine=1 - spatial.distance.cosine(model[w1], model[w2])
        except KeyError:
            sim_cosine="not found in w2v vocabs"
        print(w1,w2,score,sim_cosine,sep="\t",file=open("./sim_cosine.tab","a",encoding="utf-8"))
        print()

