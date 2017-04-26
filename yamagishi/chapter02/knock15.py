import sys

answer = [''] * int(sys.argv[1])
for line in open('./hightemp.txt'):
    answer.pop(0)
    answer.append(line.strip())

for line in answer:
    print(line)

# UNIX command: tail -n 10 hightemp.txt
