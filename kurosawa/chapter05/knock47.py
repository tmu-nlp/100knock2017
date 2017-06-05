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
    flag_sa = 0
    for morph_print in morph_use.get_morphs():
        if morph_print.get_pos() == '助詞':
            if morph_print.get_base() == 'を' and flag_sa == 1:
                flag_sa = 0
                return morph_print.get_base(),3
            else:
                return morph_print.get_base(),1
        elif morph_print.get_pos() == '動詞':
            return morph_print.get_base(),2
        elif morph_print.get_pos1() == 'サ変接続':
            flag_sa = 1
    return morph_print.get_base(),0

if __name__ == '__main__':
    for i,line_main in enumerate(make_chank()):
#        print('-----{}行目-----'.format(i))
        dst_list_temp = defaultdict(list)
        dst_list = defaultdict(list)
        flag = 0
        lines_main = []
        for j in range(len(line_main)):
            lines_main.append(line_main[j])
        for k in range(j):
            verv_ = defaultdict(list)
            dst_print = int(lines_main[k].get_dst())
            if dst_print != -1:
                str1,flag1 = pos_check(lines_main[k])
                if flag1 == 1:
                    str1_1 = make_str(lines_main[k])
                if flag1 == 3:
                    flag = 1
                    str1_1 = make_str(lines_main[k])
                str2,flag2 = pos_check(lines_main[dst_print])
                if flag1 == 1 and flag2 == 2:
                    dst_list_temp[str2].append((str1,str1_1))
                elif flag1 == 3 and flag2 == 2:
                    str_v_new = str1_1 + str2
                    str_v_temp = str2
        if flag == 1 and len(dst_list_temp[str_v_temp]) > 0:
            dst_list[str_v_new] = dst_list_temp[str_v_temp]
            for v,list_ in dst_list.items():
                str1_list = []
                str1_1_list = []
                for l in range(len(list_)):
                    str1_, str1_1_ = list_[l]
                    str1_list.append(str1_)
                    str1_1_list.append(str1_1_)
                str_01 = ' '.join(str1_list)
                str_01_1 = ' '.join(str1_1_list)
                print('{}\t{}\t{}'.format(v,str_01,str_01_1))

