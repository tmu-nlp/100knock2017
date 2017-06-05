from xml.etree.ElementTree import *
import pydot

alllist=[]
filecnt = 0
def dump(node):
    global filecnt
    for c in node:
        if c.tag == "dependencies":
            if c.get('type') == 'collapsed-dependencies':
                filecnt += 1
                edge_list = []
                governor_iter = c.getiterator('governor')
                dependent_iter = c.getiterator('dependent')
                # for e in c.getiterator("governor"):
                #     print(e.tag)
                for governor, dependent in zip(governor_iter, dependent_iter):
                    print('{} {}'.format(governor.text, dependent.text))
                    edge_list.append([governor.text, dependent.text])
                # if c.tag == 'governor':
                #     print('governor:'.format(c.text))
                # elif c.tag == 'dependent':
                #     print('dependent:'.format(c.text))
                g = pydot.graph_from_edges(edge_list, directed=True)
                g.write('./pydot{0:02d}.png'.format(filecnt), prog='dot', format='png')
                edge_list.clear()
            # print(c.keys())
            # for i in c:
            #     if i.tag == 'word':
            #         who = i.text
            #     if i.tag == 'NER' and i.text == 'PERSON':
            #         print(who);who=''
        dump(c)

tree = parse("nlp.txt.xml")
root = tree.getroot()
dump(root)
