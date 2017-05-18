import re
from knock20 import getUKdata

re_category = re.compile(r'Category:(?P<category>.+?)\|*\**\]\]')
for line in getUKdata().split('\n'):
    result = re_category.search(line) 
    if result is not None:
        print(result.group('category'))
