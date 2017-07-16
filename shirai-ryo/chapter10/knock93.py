with open("92_family85.txt") as text:
    total = 0
    sim = 0
    for line in text:
        if line.startswith(':'):
            pass
        else:
            words = line.split()
            # print(words)
            total += 1
            if words[3] == words[4]:
                sim += 1
    print("{} {}".format("85の方", sim/total))

with open("92_family") as text:
    total = 0
    sim = 0
    for line in text:
        if line.startswith(':'):
            pass
        else:
            words = line.split()
            total += 1
            if words[3] == words[4]:
                sim += 1
    print("{} {}".format("90の方", sim/total))
