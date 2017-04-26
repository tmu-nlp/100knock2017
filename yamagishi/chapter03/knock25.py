import re
from knock20 import getUKdata

base = dict()

flag = False 
re_base = re.compile('基礎情報')
re_content = re.compile('\|(?P<key>.+?) = (?P<value>.+)')
for line in getUKdata().split('\n'):
    if re_base.search(line):
        flag = True
    elif flag is True and line.startswith('}}'):
        flag = False
        break
    elif flag is True:
        content = re_content.search(line)
        if content:
            base[content.group('key')] = content.group('value')

for key, value in base.items():
    print('{}\t{}'.format(key, value))
