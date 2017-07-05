import random

if __name__ == '__main__':
    file_name = 'corpus_81.txt'
    ans_name = 't_c_list.txt'
    with open(file_name) as f, open(ans_name,'w') as ans:
        for line_num, line in enumerate(f):
            line = line.split()
            l = len(line)
            for i in range(l):
                num = random.randint(1,5)
                w = line[i]
                c = []
                if i-num < 0:
                    begin = 0
                else:
                    begin = i-num
                if i+num >= l:
                    end = l
                else:
                    end = i + num + 1
                for j in range(begin, end):
                    if j != i:
                        ans.write('{}\t{}\n'.format(w,line[j]))
#                print(c)
            if line_num%10000 == 0:
                print(line_num)
#            if line_num == 10:
#                break
