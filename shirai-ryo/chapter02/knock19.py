from collections import defaultdict
my_dict = defaultdict(int)

f = open('hightemp.txt', 'r')
for line in f:
    line = line.split()
    my_dict[line[0]] += 1

for k, v in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    print(k, v)

#reverse=Trueで降順ソートができる
#list = [1,5,2,3,6,7]があったとして
#sorted(list)すると
#[1,2,3,5,6,7]
#sorted(list, reverse=True)すると
#[7,6,5,3,2,1]
