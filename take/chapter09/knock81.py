'''
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．

Thanks,
https://gist.github.com/keeguon/2310008
'''

import json
from knock80 import purged_file

with open('countries.json') as f:
    countries_dict = json.load(f)

country_inc_space_list = list()
for country in countries_dict:
    #country listからスペース含まないやつは削除する
    if ' ' in country['name']:
        country_inc_space_list.append(country['name'])
    else:
        pass

under_scored_file = 'undersore.txt'

with open(purged_file) as f, open(under_scored_file, 'w') as out_f:
    for line in f:
        num_of_replacement = 0
        new_line = line
        for _country in country_inc_space_list: #対象国名List内の国名を全部まわして見つけたらreplace
            if _country in line:
                split_country =  '_'.join(_country.split(' '))
                new_line = new_line.replace(_country, split_country)
                num_of_replacement += 1
        print(new_line, end='', file=out_f)