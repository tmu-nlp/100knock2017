from xml.etree.ElementTree import *
from collections import defaultdict
 
def dump(node):
    global filecnt
    for c in node:
        if c.tag == "dependencies":
            if c.get('type') == 'collapsed-dependencies':
                svo_cand_defdict = defaultdict(dict)
                for dep, govword, depword in zip(c.getiterator('dep'),\
                    c.getiterator('governor'), c.getiterator('dependent')):
                    t = dep.get("type")
                    if t == 'nsubj':
                        # keyに述語候補、valueのdictのkey:Sに主語候補を入れる。
                        svo_cand_defdict[govword.text]['S'] = depword.text
                    if t == 'dobj':
                        # keyに述語候補、valueのdictのkey:Oに目的語候補を入れる。
                        svo_cand_defdict[govword.text]['O'] = depword.text

                for key_V, val_SO in svo_cand_defdict.items():
                    if len(val_SO) == 2:
                        print('S:{}\tV:{}\tO:{}'.format(val_SO['S'], key_V,val_SO['O']))
        dump(c)

tree = parse("nlp.txt.xml")
root = tree.getroot()
dump(root)
