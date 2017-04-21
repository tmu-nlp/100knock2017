import random
str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

str2 = str1.split()
count = 0
new_str = ''
for words in str2:
    length = len(words)
    if length > 4:
        temp = ''
        temp += words[0]
        list_rand = random.sample(range(1,length-1),length-2)
        for i in range(length - 2):   #ランダムで並び替え
            temp += words[list_rand[i]]
        temp += words[-1]
    else:
        temp = ''
        temp += words
    new_str += temp
    new_str += ' '
    count += 1

print (new_str)
