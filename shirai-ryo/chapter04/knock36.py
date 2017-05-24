from knock30 import nekoneko
from collections import defaultdict
my_dict = defaultdict(int)

for line in nekoneko():
    for i in line:
        my_dict[i['base']] += 1

for k, v in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
