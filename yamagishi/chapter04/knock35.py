from knock30 import get_morphs

if __name__ == '__main__':
    phrase_list = list()
    for sentence in get_morphs('./neko.txt.mecab'):
        noun_phrase = list()
        for word in sentence:
            if word['pos'] == '名詞':
                noun_phrase.append(word['surface'])
            else:
                if len(noun_phrase) > 1:
                    phrase_list.append(noun_phrase)
                noun_phrase = list()

    for phrase in sorted(phrase_list, key=lambda x: len(x)):
        print(''.join(phrase))
