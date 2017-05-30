from knock41 import Cabocha
'''
文中のすべての名詞を含む文節
各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''
def make_tree(chunks):
    result = []
    for chunk in chunks:
        noun = ""
        nodes = []
        for m in chunk.morphs:
            if m.pos == "記号":
                continue
            
            
            if m.pos == "名詞" and chunk.dst != -1:
                noun = chunk.print_morphs(do_remove_punc=True)
                
            if noun == "":
                continue
            current_word_dst = chunk.dst
            while current_word_dst != -1: # not end or terminal
                nodes.append(chunks[current_word_dst].print_morphs(do_remove_punc=True))
                current_word_dst = chunks[current_word_dst].dst
            break #if not break, it will repeat to last morphs...?? since we already loop all nodes, not get it now
        result.append((noun,nodes))     
    return result
    
if __name__ == "__main__":  
    for s in Cabocha().get_sentence():
        for x in make_tree(s):
            if len(x[1]) > 0:# mean has next node
                print(x[0] + "->" + "->".join(x[1]))
