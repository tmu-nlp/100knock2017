from collections import defaultdict

if __name__ == '__main__':
    for file_name in ['combined_94_85.txt','combined_94.txt']:
        print(file_name)
        with open(file_name) as data:
            all_list = defaultdict(tuple)
            for line in data:
                lines_s = line.split()
                all_list[lines_s[0]+'|||'+lines_s[1]] = (lines_s[2],lines_s[3])
            human_list = defaultdict()
            i = 0
            for key,value in sorted(all_list.items(),key=lambda x:x[1][0],reverse=True):
#                print(value)
                human_list[key] = i
                i += 1
            j = 0
            sum_ = 0
            for key,value in sorted(all_list.items(),key=lambda x:x[1][1],reverse=True):
#                print(value)
                sum_ += abs(j-human_list[key]) ** 2
                j += 1
            N = len(human_list)
            print(1-(6*sum_/(N**3-N)))
