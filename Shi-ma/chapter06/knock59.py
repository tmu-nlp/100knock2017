import xml.etree.ElementTree as ET
import re

def search_sexp_NPs(parse_txt):
    pettern_NP = re.compile(r'\(NP.+')
    if pettern_NP.search(parse_txt):
        flag_pare = 0
        for num_char, char in enumerate(pettern_NP.search(parse_txt).group()):
            if char == '(':
                flag_pare += 1
            elif char == ')':
                flag_pare -= 1
            if flag_pare == 0:
                sexp_NP = pettern_NP.search(parse_txt).group()[:num_char+1]
                break
        yield sexp_NP
        next_pase_txt = pettern_NP.search(parse_txt).group()[4:]
        if '(NP' in next_pase_txt:
            yield from search_sexp_NPs(pettern_NP.search(parse_txt).group()[4:])

def make_NP_text(sexp_NP, data_out):
    NP_text = []
    for sexp_NP_part in sexp_NP.split():
        if sexp_NP_part[0] == '(':
            continue
        else:
            NP_text.append(sexp_NP_part.replace(')', ''))
    print(' '.join(NP_text), file=data_out)

def make_corenlp_NP_text(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for parse in root.iter('parse'):
        for sexp_NP in search_sexp_NPs(parse.text):
            make_NP_text(sexp_NP, data_out)
        print('', file=data_out)


if __name__ == '__main__':
    with open('knock59_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_corenlp_NP_text(data_in_path, data_out)
