from knock41 import make_chank
from collections import defaultdict

def pos_check(morph_use):
    str_make = ''
    for morph_print in morph_use.get_morphs():
        if morph_print.get_pos() == '助詞':
            return morph_print.get_base(),1
        elif morph_print.get_pos() == '動詞':
            return morph_print.get_base(),2
    return morph_print.get_base(),0

if __name__ == '__main__':
    for i,line_main in enumerate(make_chank()):
        dst_list = defaultdict(list)
#        print('-----{}行目-----'.format(i+1))
        lines_main = []
        for j in range(len(line_main)):
            lines_main.append(line_main[j])
        for k in range(j):
            verv_ = defaultdict(list)
            dst_print = int(lines_main[k].get_dst())
            if dst_print != -1:
                str1,flag1 = pos_check(lines_main[k])
                str2,flag2 = pos_check(lines_main[dst_print])
                if flag1 == 1 and flag2 == 2:
                    dst_list[str2].append(str1)
        for v,list_ in dst_list.items():
            str_ = ' '.join(list_)
            print('{}\t{}'.format(v,str_))
