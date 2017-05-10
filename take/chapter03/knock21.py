import re
from knock20 import gen_uk_info

ukinfo = gen_uk_info()
print(ukinfo)
lineOfCatList = re.findall(r'\[\[Category:.*\]\]', ukinfo)
print("result.")
print(lineOfCatList)
