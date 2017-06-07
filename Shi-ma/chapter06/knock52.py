from stemming.porter2 import stem

def make_word_stem(data_in):
    for word in data_in:
        word = word.strip()
        yield [word, stem(word)]

if __name__ == '__main__':
    with open('knock51_result.txt', 'r') as data_in:
        with open('knock52_result.txt', 'w') as data_out:
            for word_stem in make_word_stem(data_in):
                print('\t'.join(word_stem), file=data_out)
