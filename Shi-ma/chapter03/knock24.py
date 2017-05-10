import re
n = 0
with open('../data/jawiki-country.txt', 'r') as data:
    for line in data:
        if re.search(r'(File:|ファイル:)', line):
            section = re.search(r'(?<=File:|ファイル:).+\.[a-zA-Z]+(?=\|)', line)
            print(section.group())
