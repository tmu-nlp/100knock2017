import random

if __name__ == '__main__':
    with open('result/knock81_result.txt', 'r') as data_in, open('result/knosk82_result.txt', 'w') as data_out:
        for line in data_in:
            tokens = line.strip().split()
            for t, token in enumerate(tokens):
                d = random.randint(1, 5)
                if t - d < 0:
                    strat_c = 0
                else:
                    strat_c = t - d
                if t + d + 1 > len(tokens):
                    end_c = len(tokens)
                else:
                    end_c = t + d + 1
                if t + 1 > len(tokens) - 1:
                    cs = tokens[strat_c:t]
                else:
                    cs = tokens[strat_c:t] + tokens[t+1:end_c]
                for c in cs:
                    print(token + '\t' + c, file=data_out)
