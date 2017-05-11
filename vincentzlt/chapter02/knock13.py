
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: <encoding name> -*- 
import sys


# In[14]:

def save_column(str_list1, str_list2):
    zipped=list(map(list,zip(str_list1,str_list2)))
    lines=[]
    for w in zipped:
        #words=[_[:-1] for _ in i]
        lines.append(w[1]+"\t"+w[0]+"\n")
    with open("combine.txt","w") as output_f:
        output_f.writelines(lines)


# In[15]:

if __name__=="__main__":
    input_str1="""高知県
埼玉県
岐阜県
山形県
山梨県
和歌山県
静岡県
山梨県
埼玉県
群馬県
群馬県
愛知県
千葉県
静岡県
愛媛県
山形県
岐阜県
群馬県
千葉県
埼玉県
大阪府
山梨県
山形県
愛知県
"""
    input_str2="""江川崎
熊谷
多治見
山形
甲府
かつらぎ
天竜
勝沼
越谷
館林
上里見
愛西
牛久
佐久間
宇和島
酒田
美濃
前橋
茂原
鳩山
豊中
大月
鶴岡
名古屋
"""
 
    try:
        with open(sys.argv[1],"r") as input_f1:
            with open(sys.argv[2],"r") as input_f2:
                save_column(input_f1.readlines(),input_f2.readlines())
    except :
        save_column(input_str1.splitlines(),input_str2.splitlines())


# In[ ]:



