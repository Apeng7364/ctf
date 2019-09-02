for i in range(1048576):
    a = "{0:020b}".format(i)
    v9 = 0.0
    v10 = 0.0
    v11 = -180.0
    v12 = 180.0
    # v11 = -90.0
    # v12 = 90.0
    for i in range(20):
        if a[i]=='0':
            v12 = v10
            v10 = (v11 + v10)/2.0
        else:
            v11 = v10
            v10 = (v10 + v12) / 2.0
    if (v10-175)>=-0.0001 and (v10-175)<=0.0001:
        print(a)
        break
for i in range(1048576):
    b = "{0:020b}".format(i)
    v9 = 0.0
    v10 = 0.0
    v11 = -90.0
    v12 = 90.0
    for i in range(20):
        if a[i]=='0':
            v12 = v10
            v10 = (v11 + v10)/2.0
        else:
            v11 = v10
            v10 = (v10 + v12) / 2.0
    if (v10-25)>=-0.0001 and (v10-25)<=0.0001:
        print(b)
        break
a = '11111100011100011100'
b = '10100011100011100011'
s = ''
for i in range(len(a)):
    s += a[i]
    s += b[i]
print(s)
flag = ''
table =  '0123456789bcdefghjkmnpqrstuvwxyz'
for i in range(0,len(s),5):
    flag += table[eval('0b' + s[i:i+5])]
flag = 'flag{' + flag + '}'
print(flag)