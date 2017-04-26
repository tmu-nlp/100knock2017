import re
from knock20 import getUKdata

re_file = re.compile('File:(?P<name_en>.+?)\||ファイル:(?P<name_ja>.+?)\|')
for line in getUKdata().split('\n'):
    result = re_file.search(line)
    if result:
        if result.group('name_en'):
            print(result.group('name_en'))
        elif result.group('name_ja'):
            print(result.group('name_ja'))
