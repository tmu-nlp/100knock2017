from knock41 import Cabocha
def get_content_start_with_type(t, morphs):
    result = ""
    start = False
    for m in morphs:
        if m.pos == "記号":
            continue
        if m.pos == t:
            start = True
        if start:
            result += m.surface
    return result
def pair_chunk(chunks):
    result = []
    for chunk in chunks:
        dst = chunk.dst
        if dst == -1:# skip
            continue
        base_morph = get_content_start_with_type("名詞",chunk.morphs)
        dst_morph = get_content_start_with_type("動詞",chunks[dst].morphs)
        if len(base_morph) > 0 and len(dst_morph) > 0:# only both of them exist, record
            result.append((base_morph, dst_morph))
    return result
if __name__ == "__main__":
    for s in Cabocha().get_sentence():
        pair = pair_chunk(s)
        for p in pair:
            print(p[0] + "\t" + p[1])
