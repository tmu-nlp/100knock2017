with open('../data/hightemp.txt', 'r') as data_in:
    with open('../data/col1.txt', 'w') as data_out1:
        with open('../data/col2.txt', 'w') as data_out2:
            for line in data_in:
                line = line.strip().replace('\t', ' ')
                data_out1.write(line.split()[0] + '\n')
                data_out2.write(line.split()[1] + '\n')
print('exit')

# cat ../data/hightemp.txt | cut -f1 # # col1.txt #
# cat ../data/hightemp.txt | cut -f2 # # col2.txt #
