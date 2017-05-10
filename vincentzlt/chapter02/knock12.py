
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: <encoding name> -*- 
import sys


# In[25]:

def save_column(str_list, col_num):
    zipped=list(map(list,zip(*str_list)))
    f_name="col"+str(col_num)+".txt"
    with open(f_name,"w") as output_f:
        for i in zipped[col_num-1]:
            output_f.write(i+"\n")


# In[28]:

if __name__=="__main__":
    input_str="""高知県	江川崎	41	2013-08-12
    埼玉県	熊谷	40.9	2007-08-16
    岐阜県	多治見	40.9	2007-08-16
    山形県	山形	40.8	1933-07-25
    山梨県	甲府	40.7	2013-08-10
    和歌山県	かつらぎ	40.6	1994-08-08
    静岡県	天竜	40.6	1994-08-04
    山梨県	勝沼	40.5	2013-08-10
    埼玉県	越谷	40.4	2007-08-16
    群馬県	館林	40.3	2007-08-16
    群馬県	上里見	40.3	1998-07-04
    愛知県	愛西	40.3	1994-08-05
    千葉県	牛久	40.2	2004-07-20
    静岡県	佐久間	40.2	2001-07-24
    愛媛県	宇和島	40.2	1927-07-22
    山形県	酒田	40.1	1978-08-03
    岐阜県	美濃	40	2007-08-16
    群馬県	前橋	40	2001-07-24
    千葉県	茂原	39.9	2013-08-11
    埼玉県	鳩山	39.9	1997-07-05
    大阪府	豊中	39.9	1994-08-08
    山梨県	大月	39.9	1990-07-19
    山形県	鶴岡	39.9	1978-08-03
    愛知県	名古屋	39.9	1942-08-02"""
    try:
        with open(sys.argv[1],"r") as input_f:
            str_list=[_.split() for _ in input_f.readlines()]
    except FileNotFoundError:
        str_list=[_.split() for _ in input_str.splitlines()]
#    print(str_list)
    save_column(str_list,1)
    save_column(str_list,2)


# In[ ]:



