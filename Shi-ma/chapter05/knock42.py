from knock41 import Chunk, cabocha_chunk_data

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        with open('result/knock42.txt', 'w') as data_out:
            for line in cabocha_chunk_data(data_in):
                    for phrase in line:
                        if phrase.get_phrase_txt() == '' or line[phrase.dst].get_phrase_txt() == '':
                            continue
                        if phrase.dst == -1:
                            if phrase.srcs == []:
                                data_out.write(phrase.get_phrase_txt() + '\n')
                            else:
                                continue
                        else:
                            data_out.write(phrase.get_phrase_txt() + '\t\t' + line[phrase.dst].get_phrase_txt() + '\n')
                    data_out.write('\n')
