import re

country_names = list()
with open('countries.txt', 'r') as f_c, open('tokens.txt', 'r') as f_i, open('tokens81.txt', 'w') as f_o:
    for line in f_c:
        country_names.append(line.strip())
    for line in f_i:
        for country_name in country_names:
            line = line.replace(country_name, '_'.join(country_name.split()))
        f_o.write(line)
