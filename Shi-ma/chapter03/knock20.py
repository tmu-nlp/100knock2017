import json
import gzip

with gzip.open('../data/jawiki-country.json.gz', 'r') as data_js:
    with open('../data/jawiki-country.txt', 'w') as data_out:
        for line in data_js:
            data_dict = json.loads(line.decode('utf-8'))
            if data_dict['title'] == 'イギリス':
                data_out.write(data_dict['text'])
