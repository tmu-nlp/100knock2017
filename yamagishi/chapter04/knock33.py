from knock30 import get_morphs

if __name__ == '__main__':
    for sentence in get_morphs('./neko.txt.mecab'):
        for word in sentence:
            if word['pos1'] == 'サ変接続':
                print(word['surface'])
