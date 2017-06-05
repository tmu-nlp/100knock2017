from knock41 import make_chank
from collections import defaultdict

def make_str(morph_u):
    str_u = ''
    for morph_p in morph_u.get_morphs():
        if morph_p.get_pos() != '記号':
            str_u += morph_p.get_surface()
    return str_u

def pos_check(morph_use):
    str_make = ''
    for morph_print in morph_use.get_morphs():
        if morph_print.get_pos() == '名詞':
            return 1
    return 0

if __name__ == '__main__':
    for i,line_main in enumerate(make_chank()):
        n = list()
#        print('-----{}行目-----'.format(i))
        dst_list_temp = defaultdict(list)
        dst_list = defaultdict(list)
        flag = 0
        lines_main = []
        for j in range(len(line_main)):
            lines_main.append(line_main[j])
        for k in range(j):
#            n = defaultdict(list)
            dst_print = int(lines_main[k].get_dst())
            if dst_print != -1:
                flag = pos_check(lines_main[k])
                if flag == 1:
                    n.append(k)
        for l in range(len(n)):
            str_list = []
            str_list.append(make_str(lines_main[n[l]]))
            dst_print = int(lines_main[l].get_dst())
            while dst_print != -1:
                str_list.append(make_str(lines_main[dst_print]))
                dst_print = int(lines_main[dst_print].get_dst())
            str_print = ' -> '.join(str_list)
            print(str_print)

