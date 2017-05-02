import re
from knock20 import getUKdata

def cleaning(value):
    value = re.sub("'''''|'''", "", value)
    match_inlink = re.match('.*\[\[.+\|(?P<string>.+?)\]\]|.*\[\[(?P<article>.+?)\]\]', value)
    if match_inlink:
        value = match_inlink.group('article') if match_inlink.group('string') is None else match_inlink.group('string')
    value = re.sub('<.*>', '', value)
    match_anchor = re.match('{{.+\|.+\|(?P<anchor>.+?)}}', value)
    if match_anchor:
        value = match_anchor.group('anchor')
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
            feature = cleaning(content.group('value'))
            if feature != '':
                base[content.group('key')] = feature

for key, value in base.items():
    print('{}\t{}'.format(key, value))
