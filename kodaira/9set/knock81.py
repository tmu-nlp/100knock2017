#!usr/bin/python
## wget http://www.benricho.org/translate/countrycode.html
## grep "<td>" countrycode.html | grep " [A-Z]" | cut -d ">" -f2 | cut -d "<" -f1 > country.txt

import bz2


fin = "./data/enwiki_knock80.txt.bz2"
fout = "./data/enwiki_knock81.txt.bz2"

country_data = [tuple((count.strip(), count.strip().replace(' ', '_') ) ) \
  for count in open('./data/country.txt').readlines()]

corpus = bz2.decompress(open(fin, 'rb').read() ).decode()
corpus = corpus.replace('\n', ' ')

for before, after in country_data:
  corpus = corpus.replace(before, after)
open(fout, 'wb').write(bz2.compress(corpus.encode(), 9) )
