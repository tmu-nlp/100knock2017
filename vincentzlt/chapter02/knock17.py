
# coding: utf-8

# In[1]:

#!/usr/bin/python

import sys,getopt


# In[2]:

def uniq_n(f_name,n):
    with open(f_name,"r",encoding="UTF-8") as input_f:
        lines=[_.split() for _ in input_f.readlines()]
    output_line=set(list(map(list,zip(*lines)))[0])
    for i in output_line:
        print(i)
    return


# In[3]:

if __name__=="__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hn:")
    except getopt.GetoptError:
        opts=[("-h","")]
    
    if args:
        for file in args:
            uniq_n(file, 1)
    else:
        print("please provide file name")


