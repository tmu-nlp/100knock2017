import json
import gzip

def wiki_UK():
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f:
            obj = json.loads(line.decode('utf-8'))
            #loads関数：文字列からPythonオブジェクトに変換する
            #load関数：ファイルオブジェクトからPythonオブジェクトに変換する
            if obj["title"] == "イギリス":
                return obj["text"]

if __name__ == "__main__":
    print(wiki_UK())
    #このモジュールで定義した関数を他のプログラムでも使うことができるようにする
