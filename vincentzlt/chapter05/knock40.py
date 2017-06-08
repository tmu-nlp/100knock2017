
# coding: utf-8

# In[1]:

import sys,pprint


# In[27]:


class cabocha_tree(object):
    r"""parse the cabocha_tree
    input:
        input_str:    the cabocha f1 result block. starting with * and end with EOS
    output:
        class of pased tree structure with pos taggings
        """

    def __init__(self, input_str_list):
        self.tree_d = dict()

        for line in input_str_list:
            if line.startswith("*"):
                _, constituent_num, father_num, head_func_num, dep_score = line.split(" ")
                self.tree_d[int(constituent_num)] = {
                    "father": father_num,
                    "head/func": head_func_num,
                    "dep_score": dep_score,
                    "words":{},
                    "children":[]
                }
                word_num = 0
            elif line.startswith("EOS"):
                pass
            elif line=="":
                pass
            else:
                surface_form, att = line.split("\t")
                pos, pos1, pos2, pos3, hy1, hy2, rt, rd1, rd2 = att.split(",")
                self.tree_d[int(constituent_num)]["words"][word_num] = {
                    "表層形": surface_form,
                    "品詞": pos,
                    "品詞細分類1": pos1,
                    "品詞細分類2": pos2,
                    "品詞細分類3": pos3,
                    "活用型": hy1,
                    "活用形": hy2,
                    "原形": rt,
                    "読み": rd1,
                    "発音": rd2
                }
                word_num += 1
        for w in self.tree_d:
            _father = int(self.tree_d[w]["father"][:-1])
            if _father!= -1:
                self.tree_d[_father]["children"].append(w)

    def print_tree_dict(self):
        pprint.pprint(self.tree_d)

    def print_knock40(self):
        for p in self.tree_d:
            print("dst: "+str(p),end='\t')
            for w in self.tree_d[p]["words"]:
                print(self.tree_d[p]["words"][w]['原形'],end='')
            print()


# In[8]:


# In[23]:

def gen_sent_cabocha(f_name):
    with open(f_name,"r",encoding="utf-8") as f:
        output=[]
        for line in f:
            if line.startswith("EOS"):
                output.append(line)
                if len(output)>1:
                    yield output
                output=[]
            else:
                output.append(line)
            


# In[31]:

for ind,sent_list in enumerate(gen_sent_cabocha("./neko.txt.cabocha")):
    if ind==2:
        print("sentence "+str(ind+1)+":")
        parse_=cabocha_tree(sent_list)
        parse_.print_knock40()
        break

