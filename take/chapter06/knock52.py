'''
usage
$ python knock50.py| python knock51.py | python knock52.py
'''
from nltk import stem
import sys

lines_list = sys.stdin.readlines()

for line in lines_list:
    l = line.strip('\n')
    porter_stm = stem.PorterStemmer()
    lancas_stm = stem.LancasterStemmer()
    p_gokan = porter_stm.stem(l.replace('\n','').lower())
    l_gokan = lancas_stm.stem(l.replace('\n','').lower())
    print("{0}\t{1}\t{2}".format(l, p_gokan, l_gokan))
