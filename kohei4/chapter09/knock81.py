"""
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が
曖昧である．
そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，
複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．

http://www.listofcountriesoftheworld.com/ を元に、（）付で、２つの呼び方を
書いてあるのは、展開した。
また、China, Korea関連等、色んな呼び方を知っているものは、追加。
その上で、' '(空白)を含む国名に限定。
長い名前を最初にチェック(United States of America と、United States, Peoples's
Republic of China と　Republic of China)為に、リストにして、長いものは、
最初にいれた。


"""

import bz2
import re

def getcountry(file_name):
    with open(file_name,'r') as ff:
        country_l = []
        for ii, line in enumerate(ff):
            if (ii % 2) == 1:
                if ' ' in line.strip():
                    country_l.append(line.strip())
    return country_l
    #print(country)

if __name__ == "__main__":

    input_file = '80corpus.txt'
    #input_file = 'corpus80.txt'
    country_l = getcountry('countries2.tsv')
    #print(country_l)
    country_s = set(country_l)
    #print(country_s)

    with open(input_file,'r') as ff,\
    open('80corpus_edit.txt','w') as gg:
        for ii, line in enumerate(ff):
            for country in country_l:
                if country in line:
                    #print(line)
                    country_new = country.replace(' ', '_',100)
                    #print(country, country_new)
                    line = line.replace(country,country_new, 100)
                    #print(line)
                    while True:
                        for country in country_l:
                            if country in line:
                                country_new = country.replace(' ', '_',100)
                                #print(country, country_new)
                                line = line.replace(country,country_new, 100)
                                #print('more than 2 countries\n',line)
                                continue
                        break
                    #print('last replaced line\n',line)

            print(line,end='',file = gg)
