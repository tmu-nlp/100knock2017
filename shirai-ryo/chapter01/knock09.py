import random

exam = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
exam_word = exam.split()

result = []

for word in exam_word:
	if len(word) > 4:
		first = word[0]
		last = word[-1] 
		middle = word[1:-1]
		new_middle = random.shuffle(list(middle))
			#ランダムシャッフルはlistにしないと使えないっぽい
		result.append(first + "".join(middle) + last)
	else:
		result.append(word)

result = " ".join(result)
print(result)
