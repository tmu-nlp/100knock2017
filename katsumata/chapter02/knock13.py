with open('col1.txt', 'r') as r_col1:
    with open('col2.txt', 'r') as r_col2:
        list_line = []
        for (row1, row2) in zip(r_col1, r_col2):
            temp_row = ''
            temp_row += (row1.strip() + '\t' + row2.strip())
            """
            a+で追加する方法
            with open('merge_col.txt', 'a+') as m_col:
                m_col.writelines(temp_row+'\n')
            """
            list_line.append(temp_row)
        with open('merge_col.txt', 'w') as m_col:
            for w_row in list_line:
                m_col.writelines(w_row+'\n')
#paste col1.txt col2.txt
