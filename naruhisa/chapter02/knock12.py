text = open('hightemp.txt', 'r')
odd = open('col1.txt', 'w')
even = open('col2.txt', 'w')

for str in text:
    count = 0
    for i in range(len(str)):
        if(str[i] == ' ' or str[i] == '\t'):
            if(count == 0):
                odd.write(str[0:i] + '\n')
                count = 1
                start = i
                continue
            elif(count == 1):
                even.write(str[start+1:i] +  '\n')
                count = 2
                start = 0
text.close()
