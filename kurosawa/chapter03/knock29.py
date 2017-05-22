import re
import requests
import json
from knock28 import mtemp

def get_response(name):
    end_point = 'https://en.wikipedia.org/w/api.php'
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get(end_point, params)
    return response.json()
    

if __name__ == '__main__':
    data = get_response(mtemp()["国旗画像"])
    data = data['query']['pages']['23473560']['imageinfo'][0]['url']
    print(data)
