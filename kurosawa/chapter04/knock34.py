from knock30 import make_list
import sys

def pick_n_phrase_no(r_file_name):
        line_list = make_list(r_file_name)
        phrase_list = []
        for i in range(len(line_list)):
            if len(line_list[i]) >= 3:
                for j in range(1,len(line_list[i])-1):
                    if line_list[i][j-1]['pos'] == '名詞' and line_list[i][j]['surface'] == 'の' and line_list[i][j+1]['pos'] == '名詞':
                        phrase_list.append(line_list[i][j-1]['surface']+'の'+line_list[i][j+1]['surface'])
        return set(phrase_list)


if __name__ == '__main__':
    print(pick_n_phrase_no(sys.argv[1]))
