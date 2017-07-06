import random

if __name__ == '__main__':
    with open('tokens_knock81.txt') as i_f, open('context_knock82.txt', 'w') as o_f:
        for line in i_f:
            words = line.split()
            s_length = len(words)
            for i in range(s_length):
                window_size = random.randint(1,5)
                for j in range(1,window_size+1):
                    #前側を記述
                    try:
                        o_f.write('{}\t{}\n'.format(words[i], words[i-j]))
                    except:
                        continue
                for j in range(1,window_size+1):    
                    #後ろ側を記述
                    try:
                        o_f.write('{}\t{}\n'.format(words[i], words[i+j]))
                    except:
                        continue
