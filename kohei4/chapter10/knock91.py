"""
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，
"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""

input_file = 'questions-words.txt'
output_file = '91_output.txt'

ff = open(output_file,'w')
ff.close()

with open(input_file, 'rt') as ff:
    fami_content = ''
    flag = 0
    for line in ff:
        if  line.strip() == ': family':
            flag = 1
            continue

        if line.strip()[0] == ':' and flag == 1:
            flag = 0
            continue

        if flag == 1:
            with open(output_file, 'a') as hh:
                print(line.strip(), file = hh)
