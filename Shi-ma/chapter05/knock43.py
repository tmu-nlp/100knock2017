from knock41 import Chunk, cabocha_chunk_data

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        with open('result/knock43.txt', 'w') as data_out:
            for line in cabocha_chunk_data(data_in):
                for phrase in line:
                    if phrase.dst == -1:
                        continue
                    if '名詞' in phrase.get_phrase_pos() and '動詞' in line[phrase.dst].get_phrase_pos():
                        data_out.write(phrase.get_phrase_txt() + '\t\t' + line[phrase.dst].get_phrase_txt() + '\n')
