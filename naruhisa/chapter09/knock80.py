import re

with open('enwiki-20150112-400-r100-10576.txt', 'r') as i_f, open('tokens.txt', 'w') as o_f:
    for i, line in enumerate(i_f):
        text = list()
        words = line.split()
        for word in words:
            word = re.sub('[\.\,\!\?\;\:\(\)\[\]\'\"]', '', word)
            if len(word) > 0:
                text.append(word)
        o_f.write(' '.join(text))
