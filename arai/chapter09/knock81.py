
country_list =  open ('country.txt').readlines()
text = open('knock80.txt').read()

for line in country_list:
    line = line.strip()
    text = text.replace(line, line.replace(' ', '_'))
print(text)

    
