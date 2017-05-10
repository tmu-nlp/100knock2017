import re

with open('../data/jawiki-country.txt', 'r') as data:
    pettern = re.compile(r'==+.+=+=')
    for line in data:
        if pettern.search(line):
            section = pettern.findall(line)
            print('Level: {0:.0f} '.format(section[0].count('=')/2 - 1), section[0])
