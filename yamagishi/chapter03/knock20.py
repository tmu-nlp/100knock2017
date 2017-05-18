import json
import gzip

def getUKdata():
    with gzip.open('./jawiki-country.json.gz', 'r') as f:
        for line in f:
            text = json.loads(line.decode('utf-8'))
            if text['title'] == 'イギリス':
                return text['text']


if __name__ == '__main__':
    print(getUKdata())
