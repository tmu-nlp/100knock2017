import re
import requests
import json


def get_response(name):
    end_point = 'https://en.wikipedia.org/w/api.php'
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get(end_point, params)
    # get メソッドは、第 1 引数に取得したいアイテムのキーを、
    # 第 2 引数にそのアイテムが見つからなかった場合のデフォルト値を受け取ります。
    # params=付与するパラメーターの hash
    return response.json()


if __name__ == '__main__':
    result = get_response('Flag of the United Kingdom.svg')
    print(result['query']['pages']['23473560']['imageinfo'][0]['url'])
