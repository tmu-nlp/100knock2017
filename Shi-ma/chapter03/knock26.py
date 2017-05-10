import re
import collections

flag = 0
info = []
with open('../data/jawiki-country.txt', 'r') as data:
    for line in data:
        if re.match(r'\{\{基礎情報', line):
            flag = 1
            continue
        elif re.match(r'\}\}', line):
            break
        if flag == 1:
            if re.search(r'\|.+ = .+', line):
                info.append(re.search(r'\|.+ = .+\n', line).group())
            else:
                info[-1] += line

info_dict = collections.defaultdict(lambda: 0)
for line in info:
    line = re.sub(r'^\||\'{2,5}', r'', line)
    
    info_dict[re.match(r'.+(?= = )', line).group()] = re.search(r'(?<= = ).+(?=\n\Z)', line, re.DOTALL).group()
info_sorted = sorted(info_dict.items(), key=lambda x: x[0])
for item in info_sorted:
    print(item)
