import collections

with open('../data/hightemp.txt', 'r') as data:
    n_data_1 = collections.defaultdict(lambda: 0)
    for line in data:
        data_1 = line.strip().replace('\t', ' ').split()[0]
        n_data_1[data_1] += 1
data_sorted_1 = sorted(n_data_1.items(), key=lambda x: x[1], reverse = 1)
for line in data_sorted_1:
    print(' '.join(map(str, line)))

# cut -f 1 ../data/hightemp.txt | sort | uniq -c | sort -nr #
