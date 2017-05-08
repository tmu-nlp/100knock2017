import sys

N = int(sys.argv[1])
n = 1
with open('../data/hightemp.txt', 'r') as data:
    for line in data:
        if n <= N:
            print(line, end='')
        n += 1

# head -n6 ../data/hightemp.txt # # N = 6のとき #
