from knock30 import make_list
import sys

def pick_n_phrase_no(r_file_name):
        line_list = make_list(r_file_name)
        flag = 0
        phrase_list = []
        phrase_list_store = []
        for i in range(len(line_list)):
            for j in range(len(line_list[i])):
                if line_list[i][j]['pos'] == '名詞':
                    flag = 1
                    phrase_list_store.append(line_list[i][j]['surface'])
                elif flag == 1:
                    phrase_list.append(''.join(phrase_list_store))
                    phrase_list_store = []
                    flag = 0
        return set(phrase_list)

if __name__ == '__main__':
    print(pick_n_phrase_no(sys.argv[1]))
