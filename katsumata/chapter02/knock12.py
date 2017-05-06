with open('hightemp.txt', 'r') as f:
    
    """
    a+で追加していく方法
    for row in f:
        row = row.split()
        with open('col1.txt', 'a+') as col1:
            col1.writelines(row[0]+'\n')
        with open('col2.txt', 'a+') as col2:
            col2.writelines(row[1]+'\n')
    """
    col1 = []
    col2 = []
    for row in f:
        row = row.split()
        col1.append(row[0])
        col2.append(row[1])
    with open('col1.txt', 'w') as f_col1:
        for word1 in col1:
            f_col1.writelines(word1+'\n')
    with open('col2.txt', 'w') as f_col2:
        for word2 in col2:
            f_col2.writelines(word2+'\n')
"""
cut -f 1 hightemp.txt
cut -f 2 hightemp.txt
"""
