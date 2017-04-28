
# coding: utf-8

# In[1]:

import random


# In[15]:

def Typoglycemia_word(input_str):
    _=list(input_str)[1:-1]
    random.shuffle(_)
    return input_str[0]+"".join(_)+input_str[-1]


# In[29]:

def Typoglycemia(input_str):
    _=input_str.strip().split()
    delim=",.;:\""
    result=""
    for i in _:
        ending=i[-1]
        word_len=len(i)
        if ((ending in delim) and (word_len>5)):
            w=Typoglycemia_word(i[:-1])+ending
        elif (not(ending in delim) and (word_len)>4):
            w=Typoglycemia_word(i)
        else:
            w=i
        result+=w+" "
    return result
            


# In[28]:

input_str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(Typoglycemia(input_str))


# In[ ]:



