import json
import gzip
def jsonget():
    with gzip.open('jawiki-country.json.gz','r') as f:
        for line in f:
            wiki = json.loads(line.decode('utf-8'))
            if wiki['title'] == 'イギリス':
                return wiki['text']

if __name__ == '__main__':
    print(jsonget())
