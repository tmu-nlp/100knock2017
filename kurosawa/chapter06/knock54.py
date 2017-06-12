import xml.etree.ElementTree as ET
from knock53 import xml_parse

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    for word_ in list(root.getiterator('token')):
        print('{}\t{}\t{}'.format(word_.findtext('word'),word_.findtext('lemma'),word_.findtext('POS')))
