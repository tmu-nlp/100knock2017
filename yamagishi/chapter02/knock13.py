with open('./merge.txt', 'w') as f:
    for col1, col2 in zip(open('./col1.txt'), open('./col2.txt')):
        f.write(col1.strip() + '\t' + col2)

# UNIX command: paste -d '\t' col1.txt col2.txt > merge.txt
