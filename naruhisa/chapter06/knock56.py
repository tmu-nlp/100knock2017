import xml.etree.ElementTree as et
from collections import defaultdict
import re

with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    core = defaultdict(tuple)
    for coreference in par.iter('coreference'):
        for coreference2 in coreference.iter('coreference'):
            text2 = list()
            for men in coreference.iter('mention'):
                if len(men.attrib) != 0:
                    text1 = men.find('text').text
                else:
                    text2.append(men.find('text').text)
            core[int(men.find('sentence').text) - 1] = (text1, text2)

    for id_s, sentence in enumerate(par.iter('sentence')):
        text = ''
        for token in sentence.iter('token'):
            word = token.find('word').text
            text += word + ' '
        if len(core[id_s]) > 0:
            for match in core[id_s][1]:
                text = re.sub(match, core[id_s][0] + '(' + match + ')', text)
        print(text)
