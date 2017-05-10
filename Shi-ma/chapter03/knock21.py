import re

with open('../data/jawiki-country.txt', 'r') as data:
    pettern = re.compile(r'Category:')
    for line in data:
        if pettern.search(line):
            print(line.strip())
