
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


# In[8]:

def wc(filename):
    n=0
    with open(filename,"r") as input_f:
        while True:
            _=input_f.readline()
            if not _:
                break
            n+=1
    return n


# In[9]:

if __name__=="__main__":
    try:
        print(wc(sys.argv[1]))
    except FileNotFoundError:
        print(wc("hightemp.txt"))


# In[ ]:



