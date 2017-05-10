import re
from knock20 import gen_uk_info

allLevel = re.findall(r'(={2,4})([^=].*[^=])={2,4}\n', gen_uk_info())
print([ (x[1],len(x[0])) for x in allLevel])
