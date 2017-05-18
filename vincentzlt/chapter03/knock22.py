
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[10]:

cat_all_re=re.compile("^.+?Category:(.+?)\]\]$")


# In[12]:

for line in open("./UK.txt","r"):
    match=cat_all_re.match(line)
    if match:
        print(match.groups()[0])


# In[ ]:



