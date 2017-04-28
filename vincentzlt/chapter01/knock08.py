
# coding: utf-8

# In[12]:

def cipher(input_str):
    output=""
    for i in input_str:
        #print(i)
        if i.islower():
            output+=chr(219-ord(i))
        else:
            output+=i
    return output


# In[13]:

def decipher(input_str):
    output=""
    for i in input_str:
        _=chr(219-ord(i))
        if _.islower():
            output+=_
        else:
            output+=i
    return output


# In[15]:

input_str="asdfaJKLEdasd"
print(input_str)
print(cipher(input_str))
print(decipher(cipher(input_str)))


# In[ ]:



