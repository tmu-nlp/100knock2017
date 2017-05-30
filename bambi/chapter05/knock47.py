from knock41 import Cabocha
'''
動詞のヲ格にサ変接続名詞
返事をする      と に は        及ばんさと 手紙に 主人は
「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．
'''
if __name__ == "__main__":
    for chunks in Cabocha().get_sentence():
        for chunk in chunks:
            verb = ""
            final_verb = ""
            for m in chunk.morphs:
                if m.pos == "動詞":
                    verb = m.base
            if verb == "":
                continue
                
            particles = {}
            sahen = [] #複数あるだっけ？
            for src in chunk.srcs:
                clean_morphs = [c for c in chunks[src].morphs if c.pos != "記号"]
                if len(clean_morphs) == 0:
                    break
                    
                morph = clean_morphs[-1] # want only element to check
                if morph.surface == "を":
                    if len(clean_morphs) >= 2 and chunks[src].morphs[-2].pos1 == "サ変接続":
                        final_verb = chunks[src].morphs[-2].surface + "を" + verb
                elif morph.pos == "助詞":
                    particles[morph.base] = chunks[src].print_morphs(do_remove_punc=True)
            
            if len(final_verb) > 0 and len(particles) > 0:
                print(final_verb," ".join(particles.keys())," ".join(particles.values()))
