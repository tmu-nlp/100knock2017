# import numpy
from scipy.stats import spearmanr

with open('94_combined.txt') as text_1:
    human_sim = []
    no_human_sim = []
    for line in text_1:
        words = line.strip().split()
        if words[0] == "Word":
            pass
        else:
            human_sim.append(words[2])
            no_human_sim.append(words[3])
    print(spearmanr(human_sim, no_human_sim))

with open('94_combined85.txt') as text_2:
    human_sim = []
    no_human_sim = []
    for line in text_2:
        words = line.strip().split()
        if words[0] == "Word":
            pass
        else:
            human_sim.append(words[2])
            no_human_sim.append(words[3])
    print(spearmanr(human_sim, no_human_sim))
