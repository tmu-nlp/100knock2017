from knock41 import Chunk, cabocha_chunk_data
import collections

with open('../data/neko.txt.cabocha', 'r') as data_in:
    with open('result/knock46.txt', 'w') as data_out:
        for i, line in enumerate(cabocha_chunk_data(data_in)):
            print('[{}行目]'.format(i+1), file=data_out)
            for phrase in line:
                verb_pattern = ''
                temp_src = collections.defaultdict(lambda: '')
                if '動詞' in phrase.get_phrase_pos():
                    verb_pattern += phrase.get_phrase_list()[phrase.get_phrase_pos().index('動詞')] + '\t'
                    for src in phrase.srcs:
                        if '助詞' in line[src].get_phrase_pos():
                            if '格助詞' in line[src].get_phrase_pos1():
                                temp_index = max([k for k, y in enumerate(line[src].get_phrase_pos1()) if y == '格助詞'])
                                temp_src[line[src].get_phrase_txt()] = line[src].get_phrase_list()[temp_index]
                            else:
                                temp_index = max([k for k, y in enumerate(line[src].get_phrase_pos()) if y == '助詞'])
                                temp_src[line[src].get_phrase_txt()] = line[src].get_phrase_list()[temp_index]
                            # if line[src].get_phrase_pos()[-1] == '助詞':
                            #     temp_src[line[src].get_phrase_txt()] = line[src].get_phrase_list()[-1]
                        else:
                            continue
                    if len(temp_src) == 0:
                        continue
                    temp_src = sorted(temp_src.items(), key=lambda x: x[1], reverse=0)
                    verb_pattern += ' '.join([value for key, value in temp_src]) + '\t\t' + ' '.join([key for key, value in temp_src])
                if verb_pattern != '':
                    print(verb_pattern, file=data_out)
