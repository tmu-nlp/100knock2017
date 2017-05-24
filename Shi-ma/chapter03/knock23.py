import re

with open('../data/jawiki-country.txt', 'r') as data:
    pettern = re.compile(r'==+.+=+=')
    for line in data:
        if pettern.search(line):
            section = pettern.search(line).group()
            print('Level: {0:.0f} '.format(section.count('=')/2 - 1), section)
