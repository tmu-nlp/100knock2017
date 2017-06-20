from xml.etree import ElementTree

xmlfile = 'nlp.txt.xml'
tree = ElementTree.parse(xmlfile)
root = tree.getroot()
doc = root.find('document')
sents = doc.find('sentences')
corefer = doc.find('coreference')
sent = sents.findall('sentence')
line_list = []
for s in sent:
    word_list = []
    #line = ''
    for word in s.iter('word'):
        word_list.append(word.text)
        #line += word.text + ' '
    line_list.append(word_list)
#print(line_list)
for coreference in corefer.findall('coreference'):
    for mention in coreference.findall('mention'):
        if mention.get('representative') == 'true':
            rep = mention.findtext('.//text')
        else:
            sentence_id = mention.findtext('.//sentence')
            word_end = mention.findtext('.//end')
            line_list[int(sentence_id)-1][int(word_end)-2] += ' <' + rep + '>'
for line in line_list:
    print(' '.join(line))
