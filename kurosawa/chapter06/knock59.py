import xml.etree.ElementTree as ET
from collections import defaultdict
from knock53 import xml_parse

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    for sen in list(root.getiterator('sentence')):
        word_list = defaultdict(list)
        parse_list = []
        parse_text = sen.findtext('parse')
        if not(parse_text is None):
            parse_text = parse_text.split()
            flag = 0
            for x in parse_text:
                if x == '(NP':
                    flag += 1
                if flag >= 1:
                    if x.startswith('('):
                        parse_list.append(x.replace('(',''))
                    else:
                        y = parse_list.pop()
                        word_list[flag].append(x.replace(')',''))
                        if x.count(')') >1:
                            for i in range(x.count(')')-1):
                                if parse_list.pop() == 'NP':
                                    print(' '.join(word_list[flag]))
                                    word_list[flag-1].extend(word_list[flag])
                                    word_list[flag] = []
                                    flag -= 1
                                    if flag == 0:
                                        word_list = defaultdict(list)
                                        break


