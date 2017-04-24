def cipher(s):
    if s.islower():
        return chr(219 - ord(s))
    else:
        return s

word = 'aBcDeFg'

enc = ''
for s in word:
    enc += cipher(s)

print('Encode: ' + enc)

dec = ''
for s in enc:
    dec += cipher(s)

print('Decode: ' + dec)
