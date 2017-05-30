from knock41 import Cabocha
def pair_chunk(chunks):
    result = []
    for chunk in chunks:
        dst = chunk.dst
        if dst == -1:# skip
            continue
        base_morph = "".join([m.surface for m in chunk.morphs if m.pos != "記号"])
        # base_morph = merge all chunk without space, but there are cases that space stand alone so, need to check
        if len(base_morph) == 0:
            continue
        dst_morph = "".join([m.surface for m in chunks[dst].morphs if m.pos != "記号"])
        result.append((base_morph, dst_morph))
    return result
if __name__ == "__main__":
    for s in Cabocha().get_sentence():
        pair = pair_chunk(s)
        for p in pair:
            print(p[0] + "\t" + p[1])
