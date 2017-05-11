import re

with open('../data/jawiki-country.txt', 'r') as data:
    for line in data:
        pettern = re.compile(r'(?<=\[\[Category:).+(?=\]\])')
        if pettern.search(line):
            print(pettern.search(line).group())
