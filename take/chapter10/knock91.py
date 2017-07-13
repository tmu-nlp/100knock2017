'''
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．このデータ中で": "で始まる行はセクション名を表す．例えば，": capital-common-countries"という行は，"capital-common-countries"というセクションの開始を表している．ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
'''

with open('questions-words.txt') as f:
    for line in f:
        if line.startswith(':') and 'family' in line:
            print_flag = True
            continue
        elif line.startswith(':') and 'family' not in line:
            print_flag = False
        else:
            pass

        if print_flag:
            print(line, end='')
