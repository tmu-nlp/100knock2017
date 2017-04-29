
# coding: utf-8

# In[4]:

#!/usr/bin/python

import sys,getopt


# In[5]:

def head_n(f_name,n):
    result=[]
    with open(f_name,"r",encoding="UTF-8") as input_f:
        for i in range(n):
            result.append(input_f.readline())
    return result


# In[6]:

if __name__=="__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hl:")
    except getopt.GetoptError:
        opts=[("-h","")]
    
    for opt, value in opts:
        if opt == "-h":
            print("try use -l <line number> to show head lines")
        elif opt == "-l" and value:
            if args:
                for file in args:
                    for i in head_n(file,int(value)):
                        print(i,end="")
                    print()
            else:
                print("please provide file name")
        else:
            print("enter -h for help")


# In[ ]:



