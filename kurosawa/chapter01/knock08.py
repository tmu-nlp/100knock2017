def cipher(str):
    strnew = ""
    l = len(str)
    for i in range(l):
        if 'a' <= str[i] <= 'z':
            strnew += chr(219 - ord(str[i]))
        else:
            strnew += str[i]
    return strnew

strin = input('> ')
print(cipher(strin))
