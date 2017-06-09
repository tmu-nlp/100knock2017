import re

def make_corenlp_Person(data_in):
    pettern_word = re.compile(r'(?<=<word>).+?(?=</word>)')
    pettern_NER = re.compile(r'(?<=<NER>).+?(?=</NER>)')
    for line in data_in:
        if pettern_word.search(line):
            word = pettern_word.search(line).group()
        if pettern_NER.search(line) and pettern_NER.search(line).group() == 'PERSON':
            yield word

if __name__ == '__main__':
    with open('../data/nlp.txt.xml', 'r') as data_in:
        with open('knock55_result.txt', 'w') as data_out:
            for word in make_corenlp_Person(data_in):
                print(word, file=data_out)
