
# coding: utf-8

# In[270]:

from pprint import pprint
from IPython.display import Image
from collections import defaultdict
import pdir,pydot,itertools
import sys,copy
print(sys.getdefaultencoding())


# In[143]:

def gen_sent_cabocha(f_name):
    with open(f_name, "r", encoding="utf-8") as f:
        output = []
        for line in f:
            if line.startswith("EOS"):

                if len(output) > 0:
                    yield output
                output = []
            else:
                output.append(line)
        yield output


# In[144]:

class Word():
    def __init__(self, line):
        self.surface, attr = line.split("\t")
        self.pos, self.pos1, self.pos2, self.pos3, self.hy1, self.hy2, self.rt, *self.rd = attr.split(
            ",")
    def __repr__(self):
        return str(self.__dict__)
    def __str__(self):
        return self.surface


# In[145]:

class Phrase():
    def __init__(self, lines):
        self.words = []
        self.childs = []
        
        for line in lines:
            if line.startswith("*"):
                _, self.index, father, head_func, self.dep_value = line.split()
                self.father = int(father[:-1])
                self.head_id, self.particle_id = (
                    int(i) for i in head_func.split("/"))
            else:
                self.words.append(Word(line))
        
        self.str="".join(w.surface for w in self.words)
        self.str_="".join(w.surface for w in self.words if w.pos!="記号")
        
    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        if self.words[-1].pos=="記号":
            return self.str[:-1]
        else:
            return self.str


# In[146]:

class Sentence():
    def __init__(self, lines):
        phrase_lines = []
        self.phrases = []
        self.temp = 1
        

        for line in lines:
            if line.startswith("*"):
                if len(phrase_lines) == 0:
                    phrase_lines.append(line)
                else:
                    #pprint(phrase_lines)
                    self.phrases.append(Phrase(phrase_lines))
                    phrase_lines = []
                    phrase_lines.append(line)
            else:
                phrase_lines.append(line)
        #pprint(phrase_lines)
        self.phrases.append(Phrase(phrase_lines))
        for ind, p in enumerate(self.phrases):
            if p.father != -1:
                self.phrases[p.father].childs.append(ind)
        
        self.str="".join(p.str for p in self.phrases)
        
    def __repr__(self):
        return str(self.__dict__)


    def __str__(self):
        return self.str


# In[147]:

def knock_40(Sent):
    # print morpheme list of a sentence with pos information
    for p in Sent.phrases:
        for w in p.words:
            print("{surface}:\tbase:\t{base}\tpos:\t{pos}\tpos1\t{pos1}".
                  format(surface=w.surface, base=w.rt, pos=w.pos, pos1=w.pos1))


# In[148]:

def knock_41(Sent):
    # print the father_id and phrase
    for p in Sent.phrases:
        father_id = p.father
        phrase = p.str_
        print("father_id:", str(father_id), "phrase:", phrase, sep="\t")


# In[149]:

def knock_42(Sent):
    for p in Sent.phrases:
        if p.father!=-1:
            print(p,Sent.phrases[p.father],sep="\t\t\t")


# In[150]:

def knock_43(Sent):
    for p in Sent.phrases:
        if p.father!=-1:
            father_node=Sent.phrases[p.father]
            if p.words[p.head_id].pos=="名詞" and father_node.words[father_node.head_id].pos=="動詞":
                print(p,father_node,sep="\t")
                


# In[151]:

def knock_44(Sent):
    tree_graph=pydot.Dot(graph_type='digraph',fontname="Microsoft YaHei")
    nodes=[]
    for ind, p in enumerate(Sent.phrases):
        nodes.append(pydot.Node(p.str,fontname="Microsoft YaHei"))
        tree_graph.add_node(nodes[ind])
    for ind, p in enumerate(Sent.phrases):
        if p.father!=-1:
            tree_graph.add_edge(pydot.Edge(nodes[ind],nodes[p.father]))
    tree_graph.write_png("knock_44.png")


# In[152]:

def knock_45(Sent):
    for p in Sent.phrases:
        if p.words[p.head_id].pos=="動詞":
            print(p,end="\t")
            for child_id in p.childs:
                print(Sent.phrases[child_id].words[Sent.phrases[child_id].particle_id], end=" ")
            print()


# In[153]:

def knock_46(Sent):
    for p in Sent.phrases:
        if p.words[p.head_id].pos=="動詞":
            print(p,end="\t")
            for child_id in p.childs:
                print(Sent.phrases[child_id].words[Sent.phrases[child_id].particle_id], end=" ")
            print("\t",end="")
            for child_id in p.childs:
                print(Sent.phrases[child_id], end=" ")
            print()


# In[156]:

def knock_47(Sent):
    for ind_p_id,p in enumerate(Sent.phrases):
        if p.words[p.
                   head_id].pos1 == "サ変接続" and p.words[p.
                                                       particle_id].surface == "を":
            ws = []
            f_h_id = Sent.phrases[p.father].head_id
            father_pos = Sent.phrases[p.father].words[f_h_id].pos

            if father_pos == "動詞":
                print(p, end="")

                for ind, w in enumerate(Sent.phrases[p.father].words):

                    if ind < f_h_id:
                        ws.append(w.surface)
                    elif ind == f_h_id:
                        ws.append(w.rt)
                        break
                print("".join(ws),end="\t")
            particles=[]
            phrases=[]
            for other_child_id in Sent.phrases[p.father].childs:
                if other_child_id!=ind_p_id:
                    other_child=Sent.phrases[other_child_id]
                    particles.append(other_child.words[other_child.particle_id].surface)
                    phrases.append(other_child.str_)
            print(" ".join(particles)," ".join(phrases),sep="\t")
            


# In[244]:

def knock_48(Sent):
    for ind, p in enumerate(Sent.phrases):
        if p.words[p.head_id].pos == "名詞":
            nodes = get_path(ind, Sent)
            #print(nodes)
            if nodes:
                print(" --> ".join(Sent.phrases[p_id].str_ for p_id in nodes))


def get_path(p_id, Sent):
    #return a list of indexes
    path_nodes = []
    path_nodes += [p_id]
    p_father_id = Sent.phrases[p_id].father
    if p_father_id != -1:
        path_nodes += get_path(p_father_id, Sent)
    return path_nodes


# In[279]:

def knock_49(Sent_):
    np_inds = []
    Sent=copy.deepcopy(Sent_)
    for ind, p in enumerate(Sent.phrases):
        if p.words[p.head_id].pos == "名詞":
            np_inds.append(ind)
    np_ind_comb = itertools.combinations(np_inds, 2)
    #print(list(np_ind_comb))
    for n1_ind, n2_ind in np_ind_comb:
        #print(n1_ind,n2_ind)
        n1_path = get_path(n1_ind, Sent)
        if n2_ind in n1_path:
            Sent=copy.deepcopy(Sent_)
            print(get_print_path_str(n1_path,n2_ind,Sent))
        else:
            n2_path = get_path(n2_ind, Sent)
            joint_n3_ind=-1
            
            for i, j in zip(reversed(n1_path), reversed(n2_path)):
                if i==j:
                    joint_n3_ind=i
                else:
                    end_n1_ind=i
                    end_n2_ind=j
            Sent=copy.deepcopy(Sent_)
            str_n1=get_print_path_str(n1_path,end_n1_ind,Sent, replace_n2=False)
            Sent=copy.deepcopy(Sent_)
            str_n2=get_print_path_str(n2_path,end_n2_ind,Sent,replace_n1=False)
            str_joint_n3=Sent.phrases[joint_n3_ind].str_
            print(" | ".join([str_n1,str_n2,str_joint_n3]))

def get_print_path_str(n1_path, end_p, Sent, replace_n1=True, replace_n2=True):
    nodes = [Sent.phrases[p_id] for p_id in n1_path if p_id <= end_p]
    if replace_n1 and replace_n2:
        nodes[0].words[nodes[0].head_id].surface = "X"
        nodes[0].str_ = "".join(w.surface for w in nodes[0].words if w.pos != "記号")
        nodes[-1].words[nodes[-1].head_id].surface = "Y"
        nodes[-1].str_ = "".join(w.surface for w in nodes[-1].words
                             if w.pos != "記号")
    elif replace_n1:
        nodes[0].words[nodes[0].head_id].surface = "X"
        nodes[0].str_ = "".join(w.surface for w in nodes[0].words if w.pos != "記号")
    elif replace_n2:
        nodes[0].words[nodes[0].head_id].surface = "Y"
        nodes[0].str_ = "".join(w.surface for w in nodes[0].words if w.pos != "記号")
    return " --> ".join(n.str_ for n in nodes)


# In[283]:

for ind, sent in enumerate(gen_sent_cabocha("./neko.txt.cabocha")):
    if ind <1000:
        print("sentence {number}:".format(number=ind + 1), end="\n")
        _=Sentence(sent)
        print(_)
        knock_46(_)
        #Image("./knock_44.png")
        #tt=Sentence(sent)
        #tt.phrases

