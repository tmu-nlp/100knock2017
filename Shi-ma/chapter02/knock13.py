with open('../data/col1.txt', 'r') as data_col1:
    with open('../data/col2.txt', 'r') as data_col2:
        with open('../data/col3.txt', 'w') as data_out:
            for (line_col1, line_col2) in zip(data_col1, data_col2):
                data_out.write(line_col1.strip() + '\t' + line_col2)
print('和歌山県' + '\t' + 'かつらぎ')
print('exit')

# paste ../data/col1.txt ../data/col2.txt #
