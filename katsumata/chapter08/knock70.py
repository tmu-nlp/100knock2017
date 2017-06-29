import tarfile
import io
import random
file_nega = 'rt-polaritydata/rt-polaritydata/rt-polarity.neg'
file_posi = 'rt-polaritydata/rt-polaritydata/rt-polarity.pos'
"""
with tarfile.open(file_name, 'r:gz') as file_p:
    a, b, c = file_p.getmembers()
"""
def make_list(file_name):
    seq_list = list()
    with io.open(file_name, encoding='latin-1') as f_p:
        for line in f_p:
            if file_name==file_posi:
                seq_list.append('+1 {}'.format(line))
            else:
                seq_list.append('-1 {}'.format(line))
    return seq_list

if __name__ == '__main__':
    hyper_list = make_list(file_posi) + make_list(file_nega)
    random.shuffle(hyper_list)    
    with open('sentiment.txt', 'w') as o_f:
        o_f.write(''.join(hyper_list))
    count_pos = 0
    count_neg = 0
    with open('sentiment.txt') as i_f:
        for line in i_f:
            if line[0:2] == '+1':
                count_pos +=1
            else:
                count_neg +=1
    print ('+1 {}'.format(count_pos))
    print ('-1 {}'.format(count_neg))
