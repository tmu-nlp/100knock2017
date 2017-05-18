
# coding: utf-8

# In[6]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[19]:

cat_all_re=re.compile("^=+?[^=]+?=+?$")


# In[20]:

for line in open("./UK.txt","r"):
    match=cat_all_re.match(line)
    if match:
        print(match.string)


# In[ ]:



