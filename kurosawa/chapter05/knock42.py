from knock41 import make_chank

def make_str(morph_use):
    str_make = ''
    for morph_print in morph_use.get_morphs():
        if morph_print.get_pos() != '記号':
            str_make += morph_print.get_surface()
    return str_make

if __name__ == '__main__':
    for line_main in make_chank():
        lines_main = []
        for j in range(len(line_main)):
            lines_main.append(line_main[j])
        for k in range(j):
            dst_print = int(lines_main[k].get_dst())
            if dst_print != -1:
                str1 = make_str(lines_main[k])
                str2 = make_str(lines_main[dst_print])
                print('{}\t{}'.format(str1,str2))
