
# coding: utf-8

# In[71]:

import sys,re,pydot
from lxml import etree


# In[90]:

def visualize_tree(f_name,number_trees=3):
    tree = etree.parse(f_name)
    root = tree.getroot()

    sentences = root.xpath("/root/document/sentences/sentence")

    for idx, sentence in enumerate(sentences):
        tree_graph = pydot.Dot(graph_type='digraph')

        basic_dependencies = sentence.xpath(
            "./dependencies[@type='basic-dependencies']/dep")
        for dep in basic_dependencies:

            father = "{no}_{word}".format(
                no=dep[0].get("idx"), word=dep[0].text)
            child = "{no}_{word}".format(
                no=dep[1].get("idx"), word=dep[1].text)
            tree_graph.add_node(pydot.Node(father))
            tree_graph.add_node(pydot.Node(child))
            tree_graph.add_edge(pydot.Edge(child, father))
        tree_graph.write_png("sentence_{no}.png".format(no=idx))

        if idx > number_trees-1:
            break


# In[91]:

if __name__=="__main__":
    xml_path="./nlp_sentence_break.txt.xml"
    visualize_tree(xml_path,6)


# In[ ]:



