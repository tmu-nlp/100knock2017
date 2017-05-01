
# coding: utf-8

# In[1]:

#!/usr/bin/python

import sys,getopt


# In[2]:

def sort_n(f_name,n,descending=False):
    with open(f_name,"r",encoding="UTF-8") as input_f:
        lines=input_f.readlines()
    return sorted(lines,key=lambda x: x.split()[2], reverse=not descending)


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
                    for _ in sort_n(i,int(value)-1):
                        print(_)
            else:
                print("please enter file name")
        else:
            print("enter -h for help")

