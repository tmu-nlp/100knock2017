fifteen = open("fifteen_answer.txt")

with open("fifteen_one_answer.txt", "w") as text:
    for line in fifteen:
        words = line.split()
        text.write("\n".join(words))
        # くっつける
        text.write("\n")
        # print()みたいな空行の出力は.writeだとできないので

fifteen.close
