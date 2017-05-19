from collections import defaultdict
import re
base_info = defaultdict(lambda:0)
switch = 0

with open('UKdata.txt', 'r') as input_data:
    for line in input_data:
        line = re.sub("[']", "", line)
        for i in range(len(line) - 3):
            if(line[i:i+4] == '基礎情報'):
                switch = 1
        if switch == 1:
            for j in range(len(line)):
                if(line[j] == '='):
                    base_info[line[1:j]] = line[j+2:]
                    break
                elif(line[j] == '*'):
                    break
                elif(line[j] == '}'):
                    switch = 0
    print(base_info)
