from collections import defaultdict

with open('hightemp.txt', 'r') as f:
    freq = defaultdict(int)
    for list in f:
        list = list.split()
        freq[list[0]] += 1
for i, j in sorted(freq.items(),key=lambda x: x[1],reverse=True):
    print(i, j)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -nr
