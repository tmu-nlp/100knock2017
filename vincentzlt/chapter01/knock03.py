
# coding: utf-8

# In[5]:

sent="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


# In[8]:

sent.replace(',','').replace('.','')


# In[16]:

sent_split=sent.split(' ')


# In[17]:

output=[len(_) for _ in sent_split]
print(output)


# In[ ]:



