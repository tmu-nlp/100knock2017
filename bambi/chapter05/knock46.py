from knock41 import Cabocha
'''
始める  で      ここで
見る    は を   吾輩は ものを
'''
if __name__ == "__main__":
    for chunks in Cabocha().get_sentence():
        for chunk in chunks:
            verb = ""
            for m in chunk.morphs:
                if m.pos == "動詞":
                    verb = m.base
            if verb == "":
                continue
                
            particles = {}
            for src in chunk.srcs:
                morph = chunks[src].morphs[-1] # want only last element to check
                if morph.pos == "助詞": # if last element == "助詞" then
                    particles[morph.base] = chunks[src].print_morphs()
                
            if len(verb) > 0 and len(particles) > 0:
                print(verb," ".join(particles.keys())," ".join(particles.values()))
