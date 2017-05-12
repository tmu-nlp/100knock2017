from collections import defaultdict
prefe_count = defaultdict(lambda: 0)
with open('hightemp.txt', 'r') as f:
    for row in f:
        words = row.split()
        prefe_count[words[0]] += 1
    for prefe,count in sorted(prefe_count.items(),reverse=True, key=lambda x:x[1]):
            print('%d %s' %(count, prefe))
#cut -f 1 hightemp.txt | sort | uniq -c | sort -nr
