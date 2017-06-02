'''
以下を見つける
NN
NNP
NNS
NNPS
NN[PS]
'''

from xml.etree.ElementTree import *
from collections import defaultdict
import re

def dump(node):
    for c in node:
        if c.tag == "parse":
            rem = re.findall(r'\(NN[\sPS] (.+?)\)', c.text, flags= re.M | re.S)
            for i in rem:
                # print(c.text)
                print(i)
        dump(c)

tree = parse("nlp.txt.xml")
root = tree.getroot()
dump(root)
