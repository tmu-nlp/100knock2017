import re

def make_corenlp_word(data_in):
    pettern = re.compile(r'(?<=<word>).+?(?=</word>)')
    for line in data_in:
        word = pettern.search(line)
        if word:
            yield word.group()

if __name__ == '__main__':
    with open('../data/nlp.txt.xml', 'r') as data_in:
        with open('knock53_result.txt', 'w') as data_out:
            for word in make_corenlp_word(data_in):
                print(word, file=data_out)
