
# coding: utf-8

# In[27]:

def n_gram(string,n):
    return list(zip(*[string[i:] for i in range(n)]))


# In[30]:

a=set(n_gram('paraparaparadise',2))
b=set(n_gram('paragraph',2))


# In[32]:

print('X|Y\t'+str(a|b))
print('X&Y\t'+str(a&b))
print('X-Y\t'+str(a-b))
print('Y-X\t'+str(b-a))


# In[ ]:



