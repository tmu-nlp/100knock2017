
# coding: utf-8

# In[27]:

def n_gram(string,n):
    return list(zip(*[string[i:] for i in range(n)]))


# In[28]:

if __name__=='__main__':
    string='I am an NLPer'
    print(n_gram(string.strip().split(),2))
    print(n_gram(string.replace(' ','_'),2))


# In[ ]:



