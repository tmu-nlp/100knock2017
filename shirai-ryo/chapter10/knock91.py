with open("questions-words.txt") as data, open("91_family.txt", "w") as family:
    for line in data:
        words = line.split()
        # flag = 0 ここに置いてはいけない（戒め）
        if words[0] == ":":
            if words[1] == "family":
                flag = 1
            else:
                flag = 0
        if flag == 1:
            family.write(line)
