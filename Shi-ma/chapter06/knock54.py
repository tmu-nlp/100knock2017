import xml.etree.ElementTree as ET

def make_corenlp_wlP(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.iter('sentence'):
        for token in sentence.iter('token'):
            word = token.find('word').text
            lemma = token.find('lemma').text
            POS = token.find('POS').text
            print('\t'.join([word, lemma, POS]), file=data_out)
        print('', file=data_out)

if __name__ == '__main__':
    with open('knock54_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_corenlp_wlP(data_in_path, data_out)
