# from knock40 import Morph
from knock41 import Chunk, cabocha_data

for line in cabocha_data():
    for chunk in line:
        if chunk.get_dst() != -1: #係り先がないと-1なので
            origin = chunk.get_word_only()
            destination = line[chunk.get_dst()].get_word_only()
            if len(str(origin)) > 0 and len(str(destination)) > 0:
                print(str(origin) + "\t" + str(destination))


# 9行目で　TypeError: object of type 'method' has no len() のエラーが出たので
# originとdestinationにstr()をつけたらエラー出なくなったが理由がよくわからない
