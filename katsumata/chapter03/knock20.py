import json
import gzip
with gzip.open('jawiki-country.json.gz', 'r') as f:

    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj.get('title') == 'イギリス':
            for key, value in obj.items():
                print('{}'.format(value))
