def rol(a,n):
    return ((a<<n)|(a>>(32-n)))&0xffffffff
def ror(a,n):
    return ((a>>n)|(a<<(32-n)))&0xffffffff
const = [0x6291BDA5, 0x0D40CBBBB, 0x0CDB9F3E5, 0x0EDBD5140, 0x2A716584, 0x42A476DE, 0x79C7CEA9, 0x48852B0E, 0x2A53B9C8, 0x2984790B, 0x0DAAED337, 0x245815E, 0x14020AE, 0x3A84AAA9, 0x84B1FD24, 0x2766105F, 0x1B765E10, 0x0B691ADC9, 0x0EB50C850, 0x264C358B, 0x32213A84, 0x387A7378, 0x1D7A8A61, 0x883DE7F1,0x2C3BAE3B,0x6DE14BA2]
'''
# encode
flag = 'testingf'
fl1 = []
fl2 = []
f1 = 0
f2 = 0
for i in range(4):
    fl1.append(ord(flag[i]))
    fl2.append(ord(flag[i+4]))
for i in range(4):
    f1<<=8
    f2<<=8
    f1+=fl1[3-i]
    f2+=fl2[3-i]

f1+=const[0]
f2+=const[1]
print(hex(f1),hex(f2))
for i in range(1,13):
    f1 = (rol(f1^f2,f2&0x1f)+const[2*i])&0xffffffff
    f2 = (rol(f1^f2,f1&0x1f)+const[2*i+1])&0xffffffff
    # print(hex(f1),hex(f2))
    # exit()
print('')
print(hex(f1),hex(f2))'''

f = open('data.jac2','rb')
flag = ''
for j in range(6):
    en1 = f.read(4)
    en2 = f.read(4)
    e1 = 0
    e2 = 0
    for i in range(4):
        e1<<=8
        e2<<=8
        e1+=ord(en1[3-i])
        e2+=ord(en2[3-i])

    for i in range(1,13)[::-1]:
        e2 = ror((e2 - const[2*i+1])&0xffffffff,e1&0x1f)^e1
        e1 = ror((e1 - const[2*i])&0xffffffff,e2&0x1f)^e2
    e2-=const[1]
    e2&=0xffffffff
    e1-=const[0]
    e1&=0xffffffff
    for i in range(4):
        flag =flag + chr(e1&0xff)
        e1>>=8
    for j in range(4):
        flag += chr(e2&0xff)
        e2>>=8
print(flag)