import random

if __name__ == '__main__':
    with open('data/answer81.txt') as i_f, open('data/answer82.txt', 'w') as o_f:
        for line in i_f:
            words = line.split()
            for i in range(len(words)):
                width = random.randint(1,5)
                for j in range(1,width + 1):
                    try:
                        o_f.write('{}\t{}\n'.format(words[i],words[i-j]))
                        # 該当の単語　該当する単語のj個前の単語
                    except:
                        continue
                for j in range(1,width + 1):
                    try:
                        o_f.write('{}\t{}\n'.format(words[i],words[i+j]))
                        # 該当の単語　該当する単語のj個後の単語
                    except:
                        continue
