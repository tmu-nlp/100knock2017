from scipy.stats import spearmanr
if __name__ == '__main__':
        with open('sim_cos90.txt', 'r') as i_f90, open('sim_cos85.txt', 'r') as i_f85:
            list_90 = list()
            list_85 = list()
            sim_90 = list()
            sim_85 = list()
            for line in i_f90:
                words = line.strip().split()
                list_90.append(words[2])
                sim_90.append(words[3])
            for line in i_f85:
                words = line.strip().split()
                list_85.append(words[2])
                sim_85.append(words[3])

        print('model85:', spearmanr(sim_85, list_85)[0])
        print('model90:', spearmanr(sim_90, list_90)[0])
