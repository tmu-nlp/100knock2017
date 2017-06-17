import xml.etree.ElementTree as et
from collections import defaultdict

with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for dpdcs in par.iter('dependencies'):
        v_nsu = '**incorrect**'
        v_dob = 'mmmistakeeee'
        s = '~nothing~'
        o = 'kyabetsunochikara'
        if dpdcs.attrib['type'] == 'collapsed-dependencies':
            for line in dpdcs.iter('dep'):
                if line.attrib['type'] == 'nsubj':
                    v_nsu = line.find('governor').text
                    s = line.find('dependent').text
                elif line.attrib['type'] == 'dobj':
                    v_dob = line.find('governor').text
                    o = line.find('dependent').text
            if v_nsu == v_dob:
                print('{}\t{}\t{}'.format(s, v_dob, o))
