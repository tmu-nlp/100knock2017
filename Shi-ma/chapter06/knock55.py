import xml.etree.ElementTree as ET

def make_corenlp_Person(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.iter('sentence'):
        for token in sentence.iter('token'):
            if token.find('NER').text == 'PERSON':
                print(token.find('word').text, file=data_out)

if __name__ == '__main__':
    with open('knock55_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_corenlp_Person(data_in_path, data_out)
