if __name__ == '__main__':
    with open('result/knock80_result.txt', 'r') as data_in, open('../data/countries.txt', 'r') as data_countries:
        data_in_str = data_in.read()
        for country in data_countries:
            data_in_str = data_in_str.replace(country.strip(), country.strip().replace(' ', '_'))
    with open('result/knock81_result.txt', 'w') as data_out:
        print(data_in_str, file=data_out)
