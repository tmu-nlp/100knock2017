def cipher(s):
    pw = ""
    for i in range(len(s)):
#    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
#        if ord('a') <= ord(s[i]) <= ord('z'):
#           pw += chr(219 - i)
            pw += chr(219 - ord(s[i]))
        else:
            pw += s[i]
    return pw

str1 = input("message:")
print("暗号処理後:",cipher(str1))
print("復合処理後:",cipher(cipher(str1)))
