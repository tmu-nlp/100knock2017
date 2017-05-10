from knock30 import get_morphs

if __name__ == '__main__':
    for sentence in get_morphs('./neko.txt.mecab'):
        for word in sentence:
            if word['pos'] == '動詞':
                print(word['surface'])
