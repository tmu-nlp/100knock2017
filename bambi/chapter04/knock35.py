from knock30 import getMecab
longest_len = 0
container = []

answer = ""
for x in getMecab():
    if x["pos"] == "名詞":
        container.append(x["surface"])
    else:
        current_len = len(container)
        if current_len > longest_len:
            longest_len = current_len
            answer = "".join(container)
        del container[:]
print(answer)
