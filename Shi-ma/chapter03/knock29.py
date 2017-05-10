import re
import collections
import urllib.request
import json

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
    line_27 = ''
    flag = 0
    line = re.sub(r'^\||\'{2,5}', r'', line)
    line = re.sub(r'(\[\[(?!.+\[\[.+).+\|)|(\[\[(?!.+\[\[.+).+#.+\|)', r'', line)
    line = re.sub(r'(\[\[)|(\]\])', r'', line)
    line = re.sub(r'(<ref>.+</ref>)|(<ref name=.+/>)|((<ref name=.+</ref>))', r'', line, flags=re.DOTALL)
    info_dict[re.match(r'.+(?= = )', line).group()] = re.search(r'(?<= = ).+(?=\n\Z)', line, flags=re.DOTALL).group()
info_sorted = sorted(info_dict.items(), key=lambda x: x[0])

common_api = 'https://commons.wikimedia.org/w/api.php?'
format_api = 'format=xml'
action_api = 'action=query'
titles_api = 'titles=File:' + re.sub(r' ', r'%20', info_dict['国旗画像'])
prop_api = 'prop=imageinfo&iiprop=url'
flag_api = common_api + '&'.join([format_api, action_api, titles_api, prop_api])
with urllib.request.urlopen(flag_api) as response:
    print(re.search(r'(?<=ii url=").+\.[a-zA-Z]+(?=" descriptionurl=)', response.read().decode('utf-8')).group())
