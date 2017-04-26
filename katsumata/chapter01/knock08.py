def cipher(str1):
    str_new = ''
    for c in str1:
        if ord(c) >= 97 and ord(c) <= 123:
            str_new +=  chr(219 - ord(c))
        else:
            str_new += c
    return str_new

str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str2 = cipher(str1)
print ('encode')
print (str2)
print ('decode')
print (cipher(str2))
