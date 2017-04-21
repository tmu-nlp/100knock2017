for line in open('./hightemp.txt'):
    print(line.strip().replace('\t', ' '))

# UNIX command:
## cat hightemp.txt | sed -e 's/ /\ /g'
## cat hightemp.txt | tr '\t' ' '
## cat hightemp.txt | expand -t 1

