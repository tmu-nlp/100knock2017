from collections import defaultdict

frequency = defaultdict(int)
for line in open('./hightemp.txt'):
    frequency[line.strip().split()[0]] += 1

for word, freq in sorted(frequency.items(), key=lambda x:x[1], reverse=True):
    print(word, freq)