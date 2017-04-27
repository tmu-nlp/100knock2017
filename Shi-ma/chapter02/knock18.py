import collections
with open('../data/hightemp.txt', 'r') as data:
    data_all_3 = collections.defaultdict(lambda: 0)
    for line in data:
        data_3 = float(line.strip().replace('\t', ' ').split()[2])
        data_all_3[line] = data_3
data_sorted_3 = sorted(data_all_3.items(), key=lambda x: x[1])
for line in data_sorted_3:
    print(line[0], end='')

# sort -k3 ../data/hightemp.txt #
