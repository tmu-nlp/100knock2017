
# coding: utf-8

# In[1]:

#!/usr/bin/python

import sys,getopt


# In[2]:

def tail_n(f_name,n):
    result=[]
    with open(f_name,"r",encoding="UTF-8") as input_f:
        lines=input_f.read().splitlines()
    return lines[-n:]


# In[4]:

if __name__=="__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],"ht:")
    except getopt.GetoptError:
        opts=[("-h","")]
    
    for opt, value in opts:
        if opt == "-h":
            print("try use -t <line number> to show tail lines")
        elif opt == "-t" and value:
            if args:
                for file in args:
                    for i in tail_n(file,int(value)):
                        print(i)
                    print()
            else:
                print("please provide file name")
        else:
            print("enter -h for help")


# In[ ]:



