if __name__ == '__main__':
    country = []
    with open('data/country_list.txt') as c_f,open('data/answer80.txt') as i_f,open('data/answer81.txt','w') as o_f:
        for line in c_f:
            line = line.strip()
            country.append(line)
        for line in i_f:
            for words in country:
                word = words.split(' ')
                line = line.replace(words,'_'.join(word))
            o_f.write(line)
