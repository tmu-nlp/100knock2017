
# coding: utf-8

# In[22]:


import os,random
from pprint import pprint


# In[19]:


path_pos="/Users/zhanglongtu/study_group/100knock_jupyter/mix20_rand700_tokens_cleaned/tokens/pos/"
path_neg="/Users/zhanglongtu/study_group/100knock_jupyter/mix20_rand700_tokens_cleaned/tokens/neg/"


# In[31]:



output_lines=[]
print("read files...")
for root,dirs,files in os.walk(path_pos):
    for file in files:
        with open(os.path.join(root,file),"r",encoding="cp1252") as f_in:
            print(file)
            text=f_in.read()
            output_lines.append("+1 {}".format(text))
for root,dirs,files in os.walk(path_neg):
    for file in files:
        print(file)
        with open(os.path.join(root,file),"r",encoding="cp1252") as f_in:
            text=f_in.read()
            output_lines.append("-1 {}".format(text))
print("shuffle lines...")
random.shuffle(output_lines)
print("save file...")
with open("sentiment.txt","w",encoding="utf-8") as f:
    f.writelines(output_lines)

