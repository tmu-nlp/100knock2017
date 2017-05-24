from knock30 import make_list
import sys

def pick_v(r_file_name):
        line_list = make_list(r_file_name)
        v_list = []
        for i in range(len(line_list)):
            for j in range(len(line_list[i])):
                if line_list[i][j]['pos'] == '動詞':
                    v_list.append(line_list[i][j]['surface'])
        return set(v_list)


if __name__ == '__main__':
    print(pick_v(sys.argv[1]))
