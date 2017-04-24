with open('./col1.txt', 'w') as f, open('./col2.txt', 'w') as g:
    for line in open('./hightemp.txt'):
        element = line.strip().split()
        f.write(element[0] + '\n')
        g.write(element[1] + '\n')

# UNIX command:
## cat hightemp.txt | cut -f 1 > col1.txt
## cat hightemp.txt | cut -f 2 > col2.txt

