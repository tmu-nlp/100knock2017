import json
import gzip

def getUK():
    with gzip.open('jawiki-country.json.gz') as f:
        for line in f:
            data = json.loads(line.decode("utf-8"))
            if data['title']=='イギリス': 
                return data['text'].split('\n')
              


if __name__ == '__main__':
    for line in getUK():
        print(line)
