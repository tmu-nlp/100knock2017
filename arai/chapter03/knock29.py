import re
import requests
import json


def get_response(name):
    end_point = 'https://en.wikipedia.org/w/api.php'
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get(end_point, params)
    return response.json()
                    

if __name__ == '__main__':
    result = get_response('Flag of the United Kingdom.svg')
    print(result['query']['pages']['23473560']['imageinfo'][0]['url'])

