
# coding: utf-8

# In[1]:


import redis,json,gzip
from pprint import pprint


# In[2]:


r=redis.StrictRedis(host="127.0.0.1",port=6379,db=0)


# In[7]:


for idx,line in enumerate(open("./artist.json", "r", encoding="utf-8")):
    band_info=json.loads(line)
    if 'tags' in band_info:
        pprint(band_info["tags"])
        for tag in band_info['tags']:
            r.hset(name='tags',value=tag,key=band_info['name'])


# In[4]:


def search_tag(band_name):
    tags=r.hget(name='tags',key=band_name)
    pprint(tags)


# In[109]:


search_tag("Domination")


# In[ ]:




