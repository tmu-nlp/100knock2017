with open('../data/hightemp.txt', 'r') as data:
    for line in data:
        line = line.replace('\t', ' ')
        print(line, end='')

# cat ../data/hightemp.txt | tr '\t' ' ' #
