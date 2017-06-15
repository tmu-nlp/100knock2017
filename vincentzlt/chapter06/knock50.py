
# coding: utf-8

# In[2]:

import sys,re


# In[60]:

def sentence_break(f_name):
    for line in open(f_name, "r",encoding="utf-8"):
        #print(line)
        rg_str=r"([\.\;\:\?\!]) ([A-Z])"
        subbed_line=re.sub(rg_str,r"\1\n\2",line)
        for l in subbed_line.split("\n"):
            if l:
                yield l





# In[95]:

for ind,sent in enumerate(sentence_break("./nlp.txt")):
    print(sent)


# In[ ]:



