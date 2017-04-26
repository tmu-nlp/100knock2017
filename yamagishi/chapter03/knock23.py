import re
from knock20 import getUKdata

re_level = re.compile(r'==.+==')
for line in getUKdata().split('\n'):
    result = re_level.search(line)
    if result:
        level = (line.count('=') / 2) - 1
        word = line.replace('=', '')
        print('{0}: level{1}'.format(word, int(level)))
