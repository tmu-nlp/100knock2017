import MeCab

inputFile = './neko.txt'
outputFile = './neko.txt.mecab2'

mecab = MeCab.Tagger(r'-F surface:%m,base:%f[6],pos:%f[0],pos1:%f[1]\n -U surface:%m,base:%f[6],pos:%f[0],pos1:%f[1]\n')

with open(outputFile, 'w') as outfile, open(inputFile) as f:
    for line in f:
        print(line, end='')
        parsedStr = mecab.parse(line)
        print(parsedStr, end='')
        outfile.write(parsedStr)

# for i in s_list:
#     if i['pos'] == '動詞':
#         print(i['surface']) # 31. 動詞の表層形をすべて抽出せよ．
#         print(i['base'])    # 32. 動詞の原形をすべて抽出せよ