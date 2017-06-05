from knock41 import Chunk, cabocha_chunk_data
import collections

with open('../data/neko.txt.cabocha', 'r') as data_in:
    with open('result/knock47.txt', 'w') as data_out:
        for i, line in enumerate(cabocha_chunk_data(data_in)):
            for j, phrase in enumerate(line):
                verb_pattern = ''
                temp_src = collections.defaultdict(lambda: '')
                if len(phrase.get_phrase_list()) == 2 and phrase.get_phrase_pos1()[0] == 'サ変接続' and phrase.get_phrase_list()[1] == 'を':
                    temp_dst = line[phrase.dst]
                    if '動詞' in temp_dst.get_phrase_pos():
                        verb_pattern += phrase.get_phrase_txt()
                        verb_pattern += temp_dst.get_phrase_list()[temp_dst.get_phrase_pos().index('動詞')] + '\t\t'
                        temp_srcs = phrase.srcs
                        temp_srcs.extend(line[phrase.dst].srcs)
                        temp_srcs.remove(j)
                        for src in temp_srcs:
                            if '助詞' in line[src].get_phrase_pos():
                                if '格助詞' in line[src].get_phrase_pos1():
                                    temp_index = max([k for k, y in enumerate(line[src].get_phrase_pos1()) if y == '格助詞'])
                                    temp_src[line[src].get_phrase_txt()] = line[src].get_phrase_list()[temp_index]
                                else:
                                    temp_index = max([k for k, y in enumerate(line[src].get_phrase_pos()) if y == '助詞'])
                                    temp_src[line[src].get_phrase_txt()] = line[src].get_phrase_list()[temp_index]
                            else:
                                continue
                        if len(temp_src) == 0:
                            continue
                        temp_src = sorted(temp_src.items(), key=lambda x: x[1], reverse=0)
                        verb_pattern += ' '.join([value for key, value in temp_src]) + '\t\t' + ' '.join([key for key, value in temp_src])
                    if verb_pattern != '':
                        print(verb_pattern, file=data_out)
