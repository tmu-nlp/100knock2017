import sys

N = int(sys.argv[1])
n = 1
with open('../data/hightemp.txt', 'r') as data:
    n_line = sum(1 for line in data)
with open('../data/hightemp.txt', 'r') as data:
    for line in data:
        if (n_line - N) < n & n <= n_line:
            print(line, end='')
        n += 1

# tail -n6 ../data/hightemp.txt #
