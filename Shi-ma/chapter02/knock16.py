import sys

N = int(sys.argv[1])
with open('../data/hightemp.txt', 'r') as data_in:
    data_in = list(data_in)
n_line = len(data_in)
n_pop = 0
n_out = 1
end_flag = 0
for n in range(n_line):
    with open('../data/split_{0}.txt'.format(n_out), 'w') as data_out:
        for i in range(N):
            if n_pop >= n_line:
                end_flag = 1
                break
            data_out.write(data_in.pop(0))
            n_pop += 1
        if end_flag == 1:
            break
    n_out += 1

# split -l 7 ../data/hightemp.txt split_unix_ #
