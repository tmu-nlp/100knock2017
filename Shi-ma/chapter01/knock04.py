txt = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = txt.replace(',', ' ').replace('.', ' ').split()
words_c = []
ans = {}

for num in range(len(words)):
    if num+1 in nums:
        words[num] = words[num][0]
    else:
        words[num] = words[num][:2]
    ans[num+1] = words[num]

print(ans)
