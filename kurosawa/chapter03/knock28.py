from knock27 import ltemp
import re

def mtemp():
    dic = ltemp()
    for key in dic:
        dic[key] = re.sub(r'<\w*\s*/?>','',dic[key]) #タグ完全形
        dic[key] = re.sub(r'\(&\w*;\)','',dic[key]) #タグ()形
        dic[key] = re.sub(r'<\w*\s*\w*','',dic[key]) #タグ不完全開始形
        dic[key] = re.sub(r'/\w*>','',dic[key]) #タグ不完全終了形
        dic[key] = re.sub(r'\{\{lang\|\w*\|','',dic[key]) #lang表記処理
        dic[key] = re.sub(r'\}\}','',dic[key]) #lang表記終端
    return dic

if __name__ == '__main__':
    for key, data in sorted(mtemp().items()):
        print('{} : {}'.format(key,data))
