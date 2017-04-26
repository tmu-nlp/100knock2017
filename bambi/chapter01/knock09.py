import random
content = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = content.split(" ")
result_list = []
for word in words:
    if len(word) >= 4:
        first_letter = word[0]
        last_letter = word[-1]
        middle_part = word[1:-1]
        new_middle_part = ''.join(random.sample(middle_part,len(middle_part)))
        result_list.append("{}{}{}".format(first_letter,new_middle_part,last_letter))
    else:
        result_list.append(word)
print(result_list)
