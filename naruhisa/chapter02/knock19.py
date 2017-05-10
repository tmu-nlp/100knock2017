from collections import defaultdict

counts = defaultdict(lambda : 0)

with open('hightemp.txt', 'r') as text:
    for line in text:
        line = line.split()
        line1 = line[0]
        counts[line1] += 1

    for k, v in sorted(counts.items(), key = lambda x:x[1], reverse = True):
        print('{}:{}' .format(k, v))
