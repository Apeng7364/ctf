res = "\xd2\"\xf1\x8d\xb7\xe0\xd0MF\x87T?\x1fI\x1c\xe7\xcb\x07\xc3\x95z\xb3z\x0b\xbb\xdb\xa1I\xc5;"
res = map(ord,list(res))
a3 = 88
for i in range(30):
    res[i] ^= a3
    a3 *= 65
    a3 += 66
    a3 %=256
for i in range(30)[::-1]:
    res[i]^=a3
    a3 *=35
    a3 -=16
    a3 %=256
print("".join(map(chr,res)))