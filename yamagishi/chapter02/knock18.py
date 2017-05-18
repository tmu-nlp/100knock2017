text = open('./hightemp.txt').readlines()

for line in sorted(text, key=lambda x:float(x.split()[2])):
    print(line.strip())

# UNIX command: sort -k 3 -nr hightemp.txt 
