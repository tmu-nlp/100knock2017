from knock41 import Cabocha
'''
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
        body
Xは | Yという -> ものを | 見た
Xは | Yを | 見た

inside body
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
'''

def add_unique(container, item):
    if item not in container:
        container.append(item)
bags = []
for s in Cabocha().get_sentence():
    items = []
    for i, c in enumerate(s):
        chunk = s[i]
        np = []
        if chunk.morphs[0].pos != "名詞":
            continue
        dst = chunk.dst
        body = s[i+1:dst]
        inside_body = s[i+1:dst]
        got_y = False
        x = chunk.print_morphs(do_remove_punc=True).replace(chunk.morphs[0].surface,"X")
        x += "|"
        np.append(x)
        # whole pic
        while len(body) > 0:
            for j in body:
                content = j.print_morphs(do_remove_punc=True)
                if j.morphs[0].pos == "名詞":
                    if got_y == False:
                        content = j.print_morphs(do_remove_punc=True).replace(j.morphs[0].surface,"Y")
                        got_y = True
                # add rest of content after y appear
                if got_y == True:
                    np.append(content)

            np.append("|{}".format(s[-1].print_morphs(do_remove_punc=True)))
            if np not in bags:
                bags.append(np)
            del body[0]
            got_y = False
            np = []
            np.append(x)
        np = []
        while len(inside_body) > 0:
            for b in inside_body:
                if b.morphs[0].pos != "名詞":
                    del inside_body[0]
                    break
                new_body = inside_body[1:]
                for i,n in enumerate(new_body):
                    if len(np) == 0:
                        np.append(b.print_morphs(do_remove_punc=True).replace(b.morphs[0].surface,"X"))
                    if n.morphs[0].pos == "名詞":
                        if "Y" not in np:
                            np.append("Y")
                        add_unique(bags,np)
                        if i == len(new_body) - 1:
                            break
                        # reset after add y
                        np = []
                        np.append(b.print_morphs(do_remove_punc=True).replace(b.morphs[0].surface,"X"))
                        for w in new_body[:i]:
                            np.append(w.print_morphs(do_remove_punc=True))

                    np.append(n.print_morphs(do_remove_punc=True))

                add_unique(bags,np)
            if len(inside_body) > 0:
                del inside_body[0]
            np = []

for b in bags:
    print("{}".format(" ->".join(b)))
