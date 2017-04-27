with open('../data/hightemp.txt', 'r') as data:
    data_1 = []
    n_sort = 0
    for line in data:
        line = line.strip().replace('\t', ' ')
        if not line.split()[0] in data_1:
            data_1.append(line.split()[0])
            n_sort += 1
    print(data_1, '{0}種類'.format(n_sort))

# cat ../data/col1.txt | sort | uniq; sort ../data/col1.txt | uniq | wc -l
 #
