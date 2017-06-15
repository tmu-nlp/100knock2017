from xml.etree.ElementTree import *
OPEN_BRACKETS = ('(', '[', '{')
CLOSE_BRACKETS = (')', ']', '}')

def checkio(expr):
    #arg:string
    np_count = 0    #入れ子判定
    floar = 0
    flag_inner = False
    temp_word = ''
    np_word = list()
    temp_list = list()
    for i, ch in enumerate(expr):
        if expr[i:i+3] != '(NP' and floar == 0:
            continue 
        elif expr[i:i+3] == '(NP':
            np_count += 1
        #以下は(NPが開いている時のみ実行    
        if ch in OPEN_BRACKETS:
            flag_inner = True
            floar += 1
        elif ch in CLOSE_BRACKETS:
            flag_inner = False
            temp_word += ')'
            temp_list.append(temp_word)
            np_word.append(temp_word.strip(')').split(' ')[-1])
            temp_word = ''
            floar -= 1
        if flag_inner:
            temp_word += ch     #temp_wには(NP (..(NP (..)))みたいに入ってる
        if floar == 0:
            if np_count < 2:    #npが入れ子になってなかったらok
                np_count = 0
                print (' '.join(np_word))
            else:
                #print (' '.join(temp_list)[:-1].lstrip('(NP'))
                np_word = filter(lambda s:s != '', np_word)
                print (' '.join(np_word))
                checkio(' '.join(temp_list)[:-1].lstrip('(NP'))
                #print (' '.join(temp_list))
            np_word = list()
            temp_list = list()
            
            
tree = parse('nlp2.txt.xml')
elem = tree.getroot()
doc = elem.find('document')
sentences = doc.find('sentences')

for child_sentence in sentences.findall('sentence'):
    id_num = int(child_sentence.get('id'))
    print (id_num)

    parse = child_sentence.find('parse')
    checkio(parse.text)
