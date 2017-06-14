import xml.etree.ElementTree as ET

def xml_parse(f_name):
    with open(f_name) as xml:
        root = ET.fromstring(xml.read())
    return root

if __name__ == '__main__':
    root = xml_parse('nlp.txt.xml')
    for word_ in root.getiterator('word'):
        print(word_.text)
