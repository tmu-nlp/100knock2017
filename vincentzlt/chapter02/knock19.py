
# coding: utf-8

# In[1]:

#!/usr/bin/python

import sys,getopt
from collections import defaultdict


# In[2]:

def freq_n(f_name,n):
    with open(f_name,"r",encoding="UTF-8") as input_f:
        lines=input_f.readlines()
    _lines=[i.split() for i in lines]
    output=defaultdict(int)
    for i in list(map(list,zip(*_lines)))[n]:
        output[i]+=1
    return output


# In[3]:

if __name__=="__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hn:")
    except getopt.GetoptError:
        opts=[("-h","")]
    
    for opt, value in opts:
        if opt == "-h":
            print("provide file name to sort")
        elif opt == "-n" and value:
            if args:
                for i in args:
                    dd=freq_n(i,int(value)-1)
                    for item in dd.items():
                        print(item[0]+"\t"+str(item[1]))
            else:
                print("please enter file name")
        else:
            print("enter -h for help")

