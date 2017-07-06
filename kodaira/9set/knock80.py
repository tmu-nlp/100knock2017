#!usr/bin/python

import bz2
import re

fin = "./data/enwiki-20150112-400-r100-10576.txt.bz2"
fout = "./data/enwiki_knock80.txt.bz2"

text = bz2.decompress(open(fin, 'rb').read()).decode() 
r_sym = r'([!?,.;:\'\"\{\}\[\]\(\)]* [!?,.;:\'\"\{\}\[\]\(\)]*)+|([!?,.;:\'\"\{\}\[\]\(\)]+\n)'

open(fout, 'wb').write(\
  bz2.compress( \
    re.sub(r_sym, lambda m: ' ' if not m.group(2) else ' \n', text).encode(), 9 \
  )
)

