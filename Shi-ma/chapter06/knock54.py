import re

def make_corenlp_w_l_P(data_in):
    word_w_l_P = []
    pettern_word = re.compile(r'(?<=<word>).+?(?=</word>)')
    pettern_lemma = re.compile(r'(?<=<lemma>).+?(?=</lemma>)')
    pettern_POS = re.compile(r'(?<=<POS>).+?(?=</POS>)')
    pettern_token_end = re.compile(r'</token>$')
    for line in data_in:
        if pettern_word.search(line):
            word_w_l_P.append(pettern_word.search(line).group())
        elif pettern_lemma.search(line):
            word_w_l_P.append(pettern_lemma.search(line).group())
        elif pettern_POS.search(line):
            word_w_l_P.append(pettern_POS.search(line).group())
        elif pettern_token_end.search(line):
            yield word_w_l_P
            word_w_l_P = []

if __name__ == '__main__':
    with open('../data/nlp.txt.xml', 'r') as data_in:
        with open('knock54_result.txt', 'w') as data_out:
            for word_w_l_P in make_corenlp_w_l_P(data_in):
                print('\t'.join(word_w_l_P), file=data_out)
