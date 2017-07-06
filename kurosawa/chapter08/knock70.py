import random

def concatenate(pos_file,neg_file,con_file):
    with open(pos_file) as pos, open(neg_file) as neg, open(con_file,'w') as con:
        concate = []
        pos_num = 0
        neg_num = 0
        for line in pos:
            concate.append('1\t{}'.format(line))
        for line in neg:
            concate.append('-1\t{}'.format(line))
        random.shuffle(concate)
        for line in concate:
            con.write(line)
            ann = line.split()[0]
            if ann == '1':
                pos_num += 1
            elif ann == '-1':
                neg_num += 1
    return pos_num,neg_num

if __name__ == '__main__':
    pos_file = 'rt-polaritydata/rt-polarity.pos'
    neg_file = 'rt-polaritydata/rt-polarity.neg'
    con_file = 'sentiment.txt'
    pos_num,neg_num = concatenate(pos_file,neg_file,con_file)
    print('positive:{}\nnegative:{}'.format(pos_num,neg_num))
