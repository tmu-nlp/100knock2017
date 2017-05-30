from knock41 import Cabocha
if __name__ == "__main__":
    for chunks in Cabocha().get_sentence():
        for chunk in chunks:
            verb = ""
            for m in chunk.morphs:
                if m.pos == "動詞":
                    verb = m.base
            # get 格助詞 from src
            for src in chunk.srcs:
                p = [x.base for x in chunks[src].morphs if x.pos1 == "格助詞"]
            if len(verb) > 0 and len(p) > 0:
                print(verb," ".join(p))
