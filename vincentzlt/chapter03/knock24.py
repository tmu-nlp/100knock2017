
# coding: utf-8

# In[6]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[21]:

file_links_all=re.compile("^\[\[File:.+?\]\]$")

file_links_only=re.compile("^\[\[File:(.+?)\|.+?\]\]$")


# In[22]:

for line in open("./UK.txt","r"):
    match=file_links_all.match(line)
    match_only=file_links_only.match(line)
    if match or match_only:
        try:
            pass
            #5print(match.string)
        except:
            pass
        try:
            print(match_only.group(1))
        except:
            pass


# In[ ]:



