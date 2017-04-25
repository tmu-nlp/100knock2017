with open('../data/hightemp.txt', 'r') as data:
    num_line = sum(1 for line in data)
    print(num_line)

# wc -l ../data/hightemp.txt #
