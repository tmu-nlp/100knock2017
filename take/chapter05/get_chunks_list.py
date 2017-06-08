import sys
import pickle
from xml.etree.ElementTree import *
from collections import defaultdict
from morph import Morph
from chunk import Chunk


# morphs = []
sents_list = [] #chunkのリスト。1文は複数のchunkをもつ。chunksリスト
def dump(node):
    debugcnt = 0
    sentence_id = -1
    for c in node:
        if c.tag == "sentence":
            sentence = []
            sentence_id += 1
            chunk_dict = {} # chunkは1sentenceに複数
            token_dict = {} #tokenは1chunkに複数
            chunk_iter = c.getiterator('chunk')
            for chunk in chunk_iter:
                morphs = []
                tok_iter = chunk.getiterator('tok')
                chunk_dict['id'] = chunk.get("id")
                chunk_dict['link'] = chunk.get("link")
                chunk_dict['rel'] = chunk.get("rel")
                chunk_dict['score'] = chunk.get("score")
                chunk_dict['head'] = chunk.get("head")
                chunk_dict['func'] = chunk.get("func")
                for tok in tok_iter:
                    tok_id = tok.get('id')
                    tok_feature = tok.get('feature')
                    morph = Morph(sentence_id, chunk_dict['id'], tok_id, tok_feature, tok.text)
                    morphs.append(morph)
                    tok_content = tok.text
                a_chunk = Chunk(sentence_id,chunk_dict['id'], chunk_dict['link'], chunk_dict['rel'], \
                chunk_dict['score'], chunk_dict['head'], chunk_dict['func'], morphs)
                # chuncks.append(a_chunk)
                sentence.append(a_chunk)
            sents_list.append(sentence)
        dump(c)

def get_chunks_list():
    tree = parse("neko.txt.xml")
    root = tree.getroot()
    dump(root)
    return sents_list
    # return chuncks

# print("\n---knock40---")
# for c in chuncks:
#     if c.sentence_id == 8:
#         for m in c.morphs:
#             print(m.feature)
