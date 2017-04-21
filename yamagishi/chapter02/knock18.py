text = open('./hightemp.txt').readlines()

for line in sorted(text, key=lambda x:x.split()[2], reverse=True):
    print(line.strip())

# UNIX command: sort -k 3 -r hightemp.txt 
