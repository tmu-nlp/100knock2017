origin_input = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

targetStr = origin_input.replace(',', '').replace('.', '')
#print(targetStr)

target_list = targetStr.split()
#print(target_list)

ichimoji_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# result = ''
resultdict = {}
for w in target_list:
    index = target_list.index(w) + 1
    if index in ichimoji_index:
        # result += w[:1] # 一文字切り取り
        resultdict[w[:1]] = index
    else:
        # result += w[:2]
        resultdict[w[:2]] = index

print(resultdict)