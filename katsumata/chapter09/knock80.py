
def getTokens(f_name):
    with open(f_name) as i_f:
        for line in i_f:
            token_l = line.strip().split() 
            token_l = [x.strip('.,!?;\':"()[]') for x in token_l]
            token_l = filter(lambda s : s != '', token_l)
            yield token_l 
            
if __name__ == '__main__':
    file_name = 'enwiki-20150112-400-r100-10576.txt'
    with open('enwiki_tokens.txt', 'w') as o_f:
        for token_l in getTokens(file_name):
            #print (' '.join(token_l), end='')
            o_f.write(' '.join(token_l) + '\n')
