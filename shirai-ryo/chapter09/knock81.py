import re

with open('country.txt') as c_text:
    country = []
    for line in c_text:
        line = line.strip('\n')
        country.append(line)
    #print(country)
with open('corpus80.txt') as in_text, open('corpus81.txt', 'w') as out_text:
    new_line = []
    for line in in_text:
        for i in country:
            if i in line:
                result = re.sub(i, i.replace(' ', '_'), line)
                #print(result)
                line = result
        new_line.append(line)
    out_text.write(" ".join(new_line) + '\n')


"""
countryの中にある国を探して、
見つけたら間のスペースをアンダーバーにしたい
"""
