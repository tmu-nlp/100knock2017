import sys
import time

limit = int(sys.argv[1])
for i, line in enumerate(open('./hightemp.txt')):
    if i == limit:
        break
    else:
        print(line.strip())

# UNIX command: head -n 10 hightemp.txt
