import xml.etree.ElementTree as ET
from knock53 import xml_parse

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    for sen in list(root.getiterator('sentence')):
        nsubj = {}
        dobj = {}
        for dependencies in list(sen.getiterator('dependencies')):
#            print(dependencies.get('type'))
            if dependencies.get('type') == 'collapsed-dependencies':
                for dep in list(dependencies.getiterator('dep')):
#                    if dep.get('type') != 'punct':
#                    print(dep.get('type'))
                    if dep.get('type') == 'nsubj':
                        nsubj[dep.find('governor').get('idx')] = dep.find('dependent').get('idx')
#                        print('nsubj',nsubj)
                    elif dep.get('type') == 'dobj':
                        dobj[dep.find('governor').get('idx')] = dep.find('dependent').get('idx')
#                        print('dobj',dobj)
                for nsubj_one in nsubj.keys():
                    if nsubj_one in dobj:
                        for words in sen.getiterator('token'):
                            if words.get('id') == nsubj[nsubj_one]:
                                s = words.findtext('word')
                            elif words.get('id') == nsubj_one:
                                v = words.findtext('word')
                            elif words.get('id') == dobj[nsubj_one]:
                                o = words.findtext('word')
                        print('{}\t{}\t{}'.format(s,v,o))

