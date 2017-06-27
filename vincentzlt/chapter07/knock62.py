
# coding: utf-8

# In[57]:


import redis,json,gzip
from pprint import pprint


# In[59]:


r=redis.StrictRedis(host="127.0.0.1",port=6379,db=0)


# In[98]:


for line in open("./artist.json", "r", encoding="utf-8"):
    band_info=json.loads(line)
    if 'area' in band_info:
        r.hset(name='area',key=band_info['name'],value=band_info["area"])


# In[94]:


def search_band(place_name):
    for band, place in r.hscan_iter(name='area'):
        if place==place_name.encode():
            yield band.decode()


# In[ ]:


for band in search_band("Japan"):
    print(band)


# In[ ]:




