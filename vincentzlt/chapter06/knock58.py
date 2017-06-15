
# coding: utf-8

# In[95]:

import sys,re,pdir
from lxml import etree
from collections import defaultdict


# In[115]:

def dep_pred_tuples(f_name):
    tree = etree.parse(f_name)
    root = tree.getroot()

    sentences = root.xpath("/root/document/sentences/sentence")

    for idx, sentence in enumerate(sentences):
        words=[]
        result=[]
        basic_dependencies = sentence.xpath(
            "./dependencies[@type='basic-dependencies']/dep")
        
        dobj=""
        pred=""
        nsubj=""
        
        for dep in basic_dependencies:

            father = dep[0].text
            child = dep[1].text
            dep_relation= dep.get("type")
            words.append((father,child,dep_relation))
        print("------sentence:{idx}-------------".format(idx=idx))
            
        for  (father,child,dep_relation) in words:
            if dep_relation=="nsubj":
                print("nsubj:{f:10}{c:10}".format(f=father,c=child))
                for (father_,child_,dep_relation_) in words:
                    
                    if father==child_:
                        print("dobj?:{f:10}{c:10}{re:10}".format(f=father_,c=child_,re=dep_relation_))
                        if dep_relation_=="dobj":
                            nsubj=father
                            pred=child
                            dobj=child_
                print()
        result.append((nsubj,pred,dobj))
        
    print(result)


# In[116]:

if __name__=="__main__":
    xml_path="./nlp_sentence_break.txt.xml"
    dep_pred_tuples(xml_path)


# In[ ]:



