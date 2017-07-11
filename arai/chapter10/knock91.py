data = open('questions-words.txt').readlines()
w_data = open('family.txt', 'w')

flag = False
for line in data:
  line = line.strip().split()
#if ':' in data:
  #print(line) 
  if line[0] == ':' and line[1] == 'family':
    #print(line)
    flag = True
  
  elif flag == True and line[0] == ':':
    flag = False
  
  elif flag == True:
    w_data.write('{}\n'.format(' '.join(line)))
      
 
  

