with open('../data/hightemp.txt', 'r') as data:
    for line in data:
        line = line.strip().replace('\t', ' ')
        print(line)

# cat ../data/hightemp.txt | tr '\t' ' ' #
