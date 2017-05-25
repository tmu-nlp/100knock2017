import re
def getMecab():
    morph_list = []
    with open("neko.txt.mecab", "r") as f:
        for line in f.readlines():
            # guess that EOS wont be used ??
            if "EOS" not in line:
                w = re.split(r',|\t', line.strip()) #strip to remove ¥n at the end, just in case
                dic = {"surface":w[0], "base":w[7],"pos":w[1], "pos1":w[2]}
                morph_list.append(dic)
    return morph_list
if __name__ == "__main__":
    print(getMecab())
