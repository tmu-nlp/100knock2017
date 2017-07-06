
if __name__ == '__main__':
    c_list = list()
    with open('country_list.txt') as country_f:
        for line in country_f:
            c_list.append(line.strip())
    with open('enwiki_tokens.txt') as i_f, open('tokens_knock81.txt', 'w') as o_f:
        for line in i_f:
            tokens = line.split(' ')
            for country in c_list:
                c_name = country.split(' ')
                line = line.replace(country, '_'.join(c_name))
            o_f.write(line) 
