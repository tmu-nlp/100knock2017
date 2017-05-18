import re
import requests
import gzip
import json

def get_flag_name():
    '''
    get_responseの動作確認のため、イギリス以外の国旗も取得
    (本当はイギリス国旗だけ持って来ればいい)
    '''

    re_flag = re.compile('.*国旗画像.*=.*(?P<flag>Flag.+\.svg)')
    name_dict = dict()
    with gzip.open('./jawiki-country.json.gz', 'r') as f:
        for line in f:
            text = json.loads(line.decode('utf-8'))
            for sentence in text['text'].split('\n'):
                content = re_flag.search(sentence)
                if content:
                    name_dict[text['title']] = content.group('flag')
    return name_dict
    

def get_response(name):
    end_point = 'https://en.wikipedia.org/w/api.php'
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get(end_point, params)
    return response.json()
    

def get_url(element):
    # 辞書かどうかを見る
    if isinstance(element, dict):
        if 'url' in element:
            return element['url']
        else:
            # 一つ下の階層に潜る(最終層のvalueはこれ以下が回らない)
            for value in element.values():
                cand = get_url(value)
                # 最後までurlが出ない辞書に潜ったら、最後にNoneが返る
                # urlが出る階層に潜ったら、順にcandidateがもどってくる
                if cand is not None:
                    return cand
    elif isinstance(element, list):
        for value in element:
            cand = get_url(value)
            if cand is not None:
                return cand


if __name__ == '__main__':
    site_index = dict()
    for name, file_name in sorted(get_flag_name().items()):
        response = get_response(file_name)
        site_index[name] = get_url(response)
        print(name, site_index[name])
