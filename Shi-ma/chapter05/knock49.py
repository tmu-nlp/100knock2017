from knock41 import Chunk, cabocha_chunk_data
import collections

def make_path(phrase, line, path):
    if phrase.dst == -1:
        yield path
    else:
        path.append(line[phrase.dst])
        yield from make_path(line[phrase.dst], line, path)

def make_paths(line):
    for phrase in line[:-1]:
        if '名詞' in phrase.get_phrase_pos():
            path = [phrase]
            for i in make_path(phrase, line, path):
                yield i

def print_IJ(I, J, data_out):
    I_txt = I[0].get_phrase_XY('X')
    if len(I) >= 2:
        I_txt += ' -> '
        I_txt += ' -> '.join([each_I.get_phrase_txt() for each_I in I[1:]])
    J_txt = J.get_phrase_XY('Y')
    print(I_txt + ' -> ' + J_txt, file=data_out)

def print_IJK(I, J, K, data_out):
    I_txt = I[0].get_phrase_XY('X')
    if len(I) >= 2:
        I_txt += ' -> '
        I_txt += ' -> '.join([each_I.get_phrase_txt() for each_I in I[1:]])
    J_txt = J[0].get_phrase_XY('Y')
    if len(J) >= 2:
        J_txt += ' -> '
        J_txt += ' -> '.join([each_J.get_phrase_txt() for each_J in J[1:]])
    K_txt = K.get_phrase_txt()
    print(' | '.join([I_txt, J_txt, K_txt]), file=data_out)

def make_XY_paths(paths, data_out):
    for num_path, path_ in enumerate(paths[:-1]):
        for path__ in paths[num_path+1:]:
            I = []; J = []; K = []; flag = 0;
            if path__[0] in path_:
                I = path_[:path_.index(path__[0])]
                J = path__[0]
                print_IJ(I, J, data_out)
                flag = 1
                continue
            for chunk_path__ in path__[1:]:
                if '名詞' in chunk_path__.get_phrase_pos() and chunk_path__ != path_[-1]:
                    continue
                if chunk_path__ in path_:
                    if flag == 1:
                        I = path_[:path_.index(path__[0])]
                    else:
                        I = path_[:path_.index(chunk_path__)]
                    J = path__[:path__.index(chunk_path__)]
                    K = chunk_path__
                    print_IJK(I, J, K, data_out)
                    break

if __name__ == '__main__':
    with open('../data/neko.txt.cabocha', 'r') as data_in:
        with open('result/knock49.txt', 'w') as data_out:
            for num_line, line in enumerate(cabocha_chunk_data(data_in)):
                print('[{}行目]'.format(num_line+1), file=data_out)
                temp_paths = []
                for temp_path in make_paths(line):
                    temp_paths.append(temp_path)
                make_XY_paths(temp_paths, data_out)

# 参考 #
# 再帰構造
# return や yield は一つの関数に必ず一つなければならず、ある条件に達したときのみ変数を返したい場合は、yield と yield from を駆使して、ある条件のときのみ print のような表現を実装する。
