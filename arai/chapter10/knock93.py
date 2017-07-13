data = open('knock92.txt').readlines()


total_count = 0
match_count_90 = 0
match_count_85 = 0
for line in data:
  words = line.strip().split()
  total_count += 1
  if words[0] == words[1]:
    match_count_90 += 1
  if words[3] == words[4]:
    match_count_85 += 1


print('90:{}\t85:{}'.format((match_count_90 / total_count), (match_count_85 / total_count)))

