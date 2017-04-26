def cipher(txt):
    txt_cip = ''
    for char in txt:
        if char.isalpha() and char.islower():
            txt_cip += chr(219 - ord(char))
        else:
            txt_cip += char
    return txt_cip

def decipher(txt_cip):
    txt_dec = ''
    for char in txt_cip:
        if char.isalpha() and char.islower():
            txt_dec += chr(219 - ord(char))
        else:
            txt_dec += char
    return txt_dec
# main #
txt = 'Hello World!! ハローワールド！！'
print(cipher(txt))
print(decipher(cipher(txt)))
