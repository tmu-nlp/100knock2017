f = open('col_merge.txt', 'w')
f_1 = open('col1.txt')
f_2 = open('col2.txt')

for line_1, line_2  in zip(f_1, f_2):
    f.write(line_1.replace('\n', '') + '\t' + line_2)
    #1つめの改行は置き換えて、2つめはどうせ改行するのでそのまま

f.close()
f_1.close()
f_2.close()
