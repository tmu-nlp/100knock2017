from knock30 import get_morphs

def ngram(sentence, n):
    return list(zip(*[sentence[i:] for i in range(n)]))

if __name__ == '__main__':
    for sentence in get_morphs('./neko.txt.mecab'):
        trigrams = ngram(sentence, 3)
        for first, second, third in trigrams:
            if first['pos'] == '名詞' and second['surface'] == 'の' and third['pos'] == '名詞':
                print('{}\t{}\t{}'.format(first['surface'], second['surface'], third['surface']))
