s = 'D9cS9N9iHjMLTdA8YSMRMp'
t = []
table = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
for i in range(len(s)):
    t.append(table.index(s[i]))
res = 0
for i in range(22):
    res+=t[i]*(58**(21-i))
t = hex(res)[2:-1]
print(t.decode('hex'))