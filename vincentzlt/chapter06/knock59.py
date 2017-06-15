
# coding: utf-8

# In[118]:

import sys,re,pdir
from nltk.tree import *
from lxml import etree
from collections import defaultdict


# In[174]:

def print_NP(tree):
    sub_trees=list(tree.subtrees())
    if len(sub_trees)>0:
        for sub_tree in sub_trees:
            if sub_tree.label()=="NP":
                tokens= list(sub_tree.leaves())
                print(" ".join(tokens))
    


# In[175]:

def s_expression(f_name):
    tree = etree.parse(f_name)
    root = tree.getroot()

    s_exps = root.xpath("/root/document/sentences/sentence/parse/text()")
    for s_exp in s_exps:
        tree=ParentedTree.fromstring(s_exp)
        print_NP(tree)


# In[176]:

if __name__=="__main__":
    xml_path="./nlp_sentence_break.txt.xml"
    s_expression(xml_path)


# In[ ]:




# In[ ]:



