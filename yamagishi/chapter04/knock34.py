from knock30 import get_morphs

def ngram(sentence, n):
    return list(zip(*[sentence[i:] for i in range(n)]))

if __name__ == '__main__':
    for sentence in get_morphs('./neko.txt.mecab'):
        trigrams = ngram(sentence, 3)
        for trigram in trigrams:
            if trigram[0]['pos'] == '名詞' and trigram[1]['surface'] == 'の' and trigram[2]['pos'] == '名詞':
                print('{}\t{}\t{}'.format(trigram[0]['surface'], trigram[1]['surface'], trigram[2]['surface']))
