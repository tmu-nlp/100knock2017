def nekoneko():
    with open("neko.txt.mecab", "r") as text:
        n_list = []
        k_list = []
        for line in text:
            words = line.strip("\n").replace("\t", ",").split(",")
            if len(words) == 1:
                k_list.append(n_list)
                n_list = []
            else:
                n_list.append({"surface" : words[0], "pos" : words[1], "pos1" : words[2], "base" : words[7]})
    return k_list


if __name__ == "__main__":
    print(nekoneko())
