def cipher(word):
    characters = []
    characters[:0] = word
    result = ""
    for char in characters:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result
print(cipher("aA18*@#"))
