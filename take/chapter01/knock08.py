s = 'HelloNLP.'
print('Original:', s)

def cipher(str=s):
    return ''.join([chr(219 - ord(w)) if w.islower() else w for w in list(str)])

print('Encrypted:', cipher())
print('Decrypted:', cipher(cipher()))
