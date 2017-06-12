import re

def deliSplit(article):
#    ans1 = []
#    sentence = []
    for line in article:
        frag = 0
#        fr = 0
#        ser = re.search('.|;|:|?|!',line)
#        print(ser.group(0))
        sline = line.split()
        ans1 = []
#        ans2 = ''
        for phrase in sline:
#            ans1.append(phrase)
#            if phrase[-1] == '.'or
            if phrase[-1] in '.:;?!':
                ans1.append(phrase)
#                ans2 = ' '.join(ans1)
                frag = 1
            elif frag == 1 and re.match(r'[A-Z]',phrase[0]):
                ans2 = ' '.join(ans1)
#                sentence.append(ans2)
                yield(ans2)
                frag = 0
                ans1 = []
                ans1.append(phrase)
#                print('\n---period---\n')
#            elif frag == 1:
#                ans2 = ' '.join(ans1)
#                yield(ans2)
#                frag = 0
#                ans1 = []
            else:
                ans1.append(phrase)
        yield ' '.join(ans1)
#                continue
#            ans1.append(phrase)

if __name__ == '__main__':
    with open('../data/nlp.txt','r') as i_f,open('answer50.txt','w') as a_f:
#        print('\n')
        for line in deliSplit(i_f):
            if len(line) != 0:
#            for sentence in deliSplit(i_f):
                print(line)
                a_f.write(line + '\n')
#            else:
#                print('\n\n')
#                a_f.write('\n\n')
