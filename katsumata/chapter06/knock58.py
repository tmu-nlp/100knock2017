from xml.etree.ElementTree import *

tree = parse('nlp.txt.xml')
elem = tree.getroot()
doc = elem.find('document')
sentences = doc.find('sentences')

for child_sentence in sentences.findall('sentence'):
    id_num = int(child_sentence.get('id'))
    print (id_num)

    for depends in child_sentence.findall('dependencies'):
        if depends.get('type') == 'collapsed-dependencies':
            v_nsu = 0
            v_do = 1
            s = 1
            o = 0
            for dep in depends.findall('dep'):
                if dep.get('type') == 'nsubj':
                    v_nsu = dep.find('governor').text
                    s = dep.find('dependent').text
                if dep.get('type') == 'dobj':
                    v_do = dep.find('governor').text
                    o = dep.find('dependent').text
            if v_nsu == v_do:
                print ('述語:{}'.format(v_nsu)) 
                if s != 1:
                    print ('主語:{}'.format(s))
                else:
                    print('主語は見つからなかったみたいです...')
                if o != 0:    
                    print ('目的語:{}'.format(o))
                else:
                    print ('目的語は見つからなかったみたいです...')
            else:
                print ('述語は見つからなかったみたいです...')
                print ('主語と目的語も定義できませんでした') 
