# -*- coding: utf-8 -*-

s1 = 'パトカー'
s2 = 'タクシー'

ans = ''
for l1, l2 in zip(s1, s2):
    ans += l1 + l2

print(ans)
