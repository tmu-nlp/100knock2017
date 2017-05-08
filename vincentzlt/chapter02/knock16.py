
# coding: utf-8

# In[5]:

#!/usr/bin/python

import sys,getopt


# In[6]:

def split_n(f_name,n):
    with open(f_name,"r",encoding="UTF-8") as input_f:
        lines=input_f.readlines()
    digits=len(str(len(lines)))
    
    for i in range(0,len(lines),n):
        output_f_name=f_name+"."+'{num:0>{digits}}'.format(num=int(i/n),digits=digits)
        with open(output_f_name,"w",encoding="UTF-8") as f:
            f.writelines(lines[i:i+n])
    return


# In[7]:

if __name__=="__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hn:")
    except getopt.GetoptError:
        opts=[("-h","")]
    
    for opt, value in opts:
        if opt == "-h":
            print("try use -n <line number> to input lines")
        elif opt == "-n" and value:
            if args:
                for file in args:
                    split_n(file, int(value))
            else:
                print("please provide file name")
        else:
            print("enter -h for help")



