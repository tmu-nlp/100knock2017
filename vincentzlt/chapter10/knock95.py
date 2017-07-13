
# coding: utf-8

# In[1]:


import word2vec
from pprint import pprint
from scipy import spatial
from scipy.stats import spearmanr


# In[6]:


scores=[]
sim_scores=[]
for idx,line in enumerate(open("./sim_cosine.tab","r",encoding="utf-8")):
    if idx>0:
        w1,w2,score,sim_score=line.split("\t")
        if sim_score!='not found in w2v vocabs\n':
            score=float(score)
            sim_score=float(sim_score)
            scores.append(score)
            sim_scores.append(sim_score)
spearmanr(scores,sim_scores)

