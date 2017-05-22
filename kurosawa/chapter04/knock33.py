from knock30 import make_list
import sys

def pick_n_sa(r_file_name):
        line_list = make_list(r_file_name)
        n_list = []
        for i in range(len(line_list)):
            for j in range(len(line_list[i])):
                if line_list[i][j]['pos1'] == 'サ変接続':
                    n_list.append(line_list[i][j]['surface'])
        return set(n_list)


if __name__ == '__main__':
    print(pick_n_sa(sys.argv[1]))
