
# coding: utf-8

# In[1]:


import word2vec


# In[2]:


word2vec.word2phrase("./enwiki-20150112-400-r10-105752.txt.strip","./enwiki-20150112-400-r10-105752.phrase.txt",verbose=True)


# In[3]:


word2vec.word2vec("./enwiki-20150112-400-r10-105752.phrase.txt","./enwiki-20150112-400-r10-105752.bin",size=300,verbose=True)


# In[4]:


model=word2vec.load("./enwiki-20150112-400-r10-105752.bin")


# In[7]:


model["dog"].shape

