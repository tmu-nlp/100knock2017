import re
with open('nlp.txt') as file:
    for line in file:
        #(. or ; or : or ? or !)
        # replace (group1 group2 group3) by r"group1+group2+\n+group3"
        print(re.sub(r"(\;|\!|\:|\.)(\s+)(?P<capital>[A-Z])", r"\1\2\n\3",line))
