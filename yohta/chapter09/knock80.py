import re

# pattern = r'\'|\.|\!|\?|\;|\:|\(|\)|\[|\]|\'|\"'
if __name__ == '__main__':
    with open('data/enwiki-20150112-400-r100-10576.txt','r') as i_f,open('data/answer80.txt','w') as o_f:
        for line in i_f:
            tokens = line.strip().split()
            token_b = []
            for token in tokens:
                token_a = token.strip("'.,!?;:()[]'\"")
#            print(token_a)
                token_b.append(token_a)
#            print(' '.join(token_b))
            ans = ' '.join(token_b)
            if len(ans) > 0:
                o_f.write(ans + '\n')
