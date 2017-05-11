from collections import defaultdict

word_counts = defaultdict(lambda: 0)
for line in open('hightemp.txt'):
    line2 = line.split()
    word_counts[line2[0]] += 1

for y,w in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(y,w)

