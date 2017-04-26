def cipher(s):
    s = list(s)
    for i in range(len(s)):
        if(s[i] <= 'z' and s[i] >= 'a'):
                tmp = 219 - ord(s[i])
                s[i] = chr(tmp)

    s = ''.join(s)
    return s

str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(cipher(str1))
