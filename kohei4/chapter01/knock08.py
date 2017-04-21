original = "I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus)."

def cipher(text):
  ans = ''
  for i in range(len(text)):
    t = ord(text[i])
    if (t >= 97) and (t<= 122):
      r = chr(219 - t)
    else:
      r = text[i]
    ans = ans + r
  return ans

print("Original :", original)
encr = cipher(original)
print("Encrypted:",encr)
print("Recovered:",cipher(encr))
