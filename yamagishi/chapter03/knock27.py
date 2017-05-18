import re
from knock20 import getUKdata


def cleaning(value):
    value = re.sub("'''''|'''", "", value)
    match = re.match('.*\[\[.+\|(?P<string>.+?)\]\]|.*\[\[(?P<article>.+?)\]\]', value)
    if match:
        value = match.group('article') if match.group('string') is None else match.group('string')
    return value

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
            base[content.group('key')] = cleaning(content.group('value'))

for key, value in base.items():
    print('{}\t{}'.format(key, value))
