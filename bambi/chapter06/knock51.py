import re 
'''
空白を単語の区切りとみなし，50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
why need the 50 result huh!?
just break to word and add \n after "."(文の終端) sounds more sense.
anyway, just follow this damn construction
'''
with open('nlp.txt') as file:
    for line in file:
        data = re.sub(r"(\;|\!|\:|\.)(\s+)(?P<capital>[A-Z])", r"\1\2\n\3",line).split(" ")
        for x in data:
            x = x.replace("\n","") # remove it, to make "." be the last character
            if x.endswith('.'):
                x += "\n"
            print(x)
        
        
