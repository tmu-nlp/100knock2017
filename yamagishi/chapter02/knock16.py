import sys

num = int(sys.argv[1])
file_num = 1
data = list()
for i, line in enumerate(open('./hightemp.txt')):
    data.append(line.strip())
    if (i + 1) % num == 0:
        with open('split{0:02d}.txt'.format(file_num), 'w') as f:
            f.write('\n'.join(data))
        data = list()
        file_num += 1

if len(data) > 0:
    with open('split{0:02d}.txt'.format(file_num), 'w') as f:
        f.write('\n'.join(data))

# UNIX command: split -l 10 hightemp.txt
