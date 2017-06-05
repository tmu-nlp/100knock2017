import CaboCha
import re
import sys
from xml.etree.ElementTree import *
import pydot

p = re.compile(r'^(.*?)\t(.*?)\n', re.M)
b = re.compile(r'^\n', re.M)

parser = CaboCha.Parser('-f1')
morph_list = []
input_sentence = sys.argv[1]

if b.match(input_sentence):
    sys.exit(1)

tree = parser.parse(input_sentence)
#s = tree.toString(CaboCha.FORMAT_LATTICE)
s = tree.toString(CaboCha.FORMAT_XML)
print(s)

elem = fromstring(s)

edge_list = list()
src_chunk_iter = elem.getiterator('chunk')
for src_chunk in src_chunk_iter:
    cur_chunk_link = src_chunk.get('link')
    if int(cur_chunk_link) < 0:
        break
    cur_chunk_id = src_chunk.get('id')
    # tok_iter = chunk.getiterator('tok')
    src_token = ''
    for tok in src_chunk.getiterator('tok'):
        src_token += tok.text
    # print("checking link:{} word:{}".format(cur_chunk_link, src_token) )
    for dest_cand in elem.getiterator('chunk'):
        cand_id = dest_cand.get('id')
        if not int(cand_id) > int(cur_chunk_id):
            continue
        if cand_id == cur_chunk_link:# 対応するidのchunkを見つけたら、そのチャンクを構成するtokenを構成してループ終了.（対応する文節は単一を過程）
            dest_token = ''
            for tok in dest_cand.getiterator('tok'):
                dest_token += tok.text
            edge_list.append([src_token, dest_token])

for e in edge_list:
    print('src: {} -> dest: {}'.format(e[0],e[1]))

g = pydot.graph_from_edges(edge_list, directed=True)
# g.write('./pydot{0:02d}.png'.format(filecnt), prog='dot', format='png')
graph_filename = 'hoge.png'
g.write(graph_filename, prog='dot', format='png')

import subprocess
subprocess.call('imgcat '+ graph_filename, shell=True)

