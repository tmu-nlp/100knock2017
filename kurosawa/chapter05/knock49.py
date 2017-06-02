from knock41 import make_chank
from collections import defaultdict

def make_str(morph_u,mode_u = 0):
    str_u = ''
    flag = 0
    for morph_p in morph_u.get_morphs():
        pos = morph_p.get_pos()
        if pos != '記号':
            if pos == '名詞':
                if mode_u == 1 and flag == 0:
                    str_u += 'X'
                    flag = 1
                elif mode_u == 2 and flag == 0:
                    str_u += 'Y'
                    flag = 1
                elif mode_u == 0:
                    str_u += morph_p.get_surface()
            else:
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
        print('-----{}行目-----'.format(i))
        dst_list_temp = defaultdict(list)
        dst_list = defaultdict(list)
        flag = 0
        lines_main = []
        for j in range(len(line_main)):
            lines_main.append(line_main[j])
        for k in range(j):
#            n = defaultdict(list)
            flag = pos_check(lines_main[k])
            if flag == 1:
                n.append(k)
        if len(n) >= 2:
#            print(n)
            for l in range(len(n)-1):
                for m in range(l+1,len(n)):
                    flag_back = 0
                    dst_print_temp = -1
                    str_list = list()
                    str_list.append(make_str(lines_main[n[l]],1))
                    dst_print = int(lines_main[n[l]].get_dst())
                    while 1:
#                        print('{} {} start'.format(dst_print,n[m]))
                        if dst_print > n[m] and flag_back == 0:
                            str_list.append('|')
                            dst_print_temp = dst_print
                            dst_print = n[m]
                            flag_back = 1
#                            print('{} back'.format(dst_print))
                        if dst_print >= dst_print_temp and flag_back == 1:
                            str_list.append('|')
                            dst_print = dst_print_temp
                            flag_back = 2
#                            print('{} back after'.format(dst_print))
                        if dst_print == n[m]:
                            str_list.append(make_str(lines_main[dst_print],2))
#                            print('{} same'.format(dst_print))
                            if flag_back == 0:
                                break
                        else:
                            str_list.append(make_str(lines_main[dst_print]))
#                            print('{} append'.format(dst_print))
                        dst_print = int(lines_main[dst_print].get_dst())
                        if dst_print == -1 :
                            break
                    str_print = ' -> '.join(str_list)
                    str_print = str_print.replace('-> | ->','|')
                    print(str_print)

