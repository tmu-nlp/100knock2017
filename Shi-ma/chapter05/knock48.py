from knock41 import Chunk, cabocha_chunk_data
import collections

def make_path(phrase, line, path):
    if phrase.dst == -1:
        yield path
    else:
        path.append(line[phrase.dst].get_phrase_txt())
        yield from make_path(line[phrase.dst], line, path)

def make_paths(line):
    for phrase in line[:-1]:
        if '名詞' in phrase.get_phrase_pos():
            path = [phrase.get_phrase_txt()]
            for i in make_path(phrase, line, path):
                yield i

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        with open('result/knock48.txt', 'w') as data_out:
            for i, line in enumerate(cabocha_chunk_data(data_in)):
                print('[{}行目]'.format(i+1), file=data_out)
                for j in make_paths(line):
                    print(' -> '.join(j), file=data_out)

# 参考 #
# 再帰構造
# return や yield は一つの関数に必ず一つなければならず、ある条件に達したときのみ変数を返したい場合は、yield と yield from を駆使して、ある条件のときのみ print のような表現を実装する。
