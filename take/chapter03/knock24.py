import re
from knock20 import gen_uk_info

filetag = re.findall(r'(file|ファイル):(.+?)\|', gen_uk_info(), flags=re.IGNORECASE)
print([i[1] for i in filetag])
