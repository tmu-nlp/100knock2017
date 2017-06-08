from stemming.porter2 import stem
import re
with open('nlp.txt') as file:
    for line in file:
        data = re.sub(r"(\;|\!|\:|\.)(\s+)(?P<capital>[A-Z])", r"\1\2\n\3",line).split(" ")
        for x in data:
            x = x.replace("\n","") # remove it, to make "." be the last character
            if x.endswith('.'):
                x += "\n"
            print("{} -> {}".format(x,stem(x)))
