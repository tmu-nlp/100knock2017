answer = set()

for line in open('./hightemp.txt'):
    answer.add(line.strip().split()[0])

print(answer)

# UNIX command: cut -f 1 hightemp.txt | sort | uniq 
