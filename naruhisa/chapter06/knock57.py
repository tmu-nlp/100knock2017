import xml.etree.ElementTree as et
i = 0
with open('nlp.txt.xml') as i_f:
    par = et.parse(i_f)
    for dpdcs in par.iter('dependencies'):
    #    if dpdcs.attrib == 'collapsed-dependencies':
            i += 1
            with open('GRAPH/graph{}.dot' .format(i), 'w') as o_f:
                o_f.write('digraph g{\n')
                for line in dpdcs.iter('dep'):
                    gov = line.find('governor').text
                    dpt = line.find('dependent').text
                    o_f.write('\"' + gov + '\"' + '->' + '\"' + dpt + '\"\n')
                o_f.write('}')

#dot -T png GRAPH/graph7.dot -o graph7.out.png
