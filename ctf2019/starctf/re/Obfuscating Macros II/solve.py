#encrypt
def rol(a,b):
    tmp1 = (a&0x8000000000000000)//0x8000000000000000
    tmp2 = (b&0x8000000000000000)//0x8000000000000000
    a = a << 1
    b = b << 1
    a |= tmp2
    b |= tmp1
    a&=0xffffffffffffffff
    b&=0xffffffffffffffff
    return a,b

a = 0x6161616161616161
b = 0x3030303030303030
for i in range(0x400):
    if b&1:
        a^=b
    else:
        a^=(~b)
    b = ~b
    a &= 0xffffffffffffffff
    b &= 0xffffffffffffffff
    a,b = rol(a,b)
    tmp = a
    a = a+b
    b = tmp
    a,b = rol(a,b)
print(hex(a))
print(hex(b))
print('')

#decrypt
def ror(a,b):
    tmp1 = (a&1)*0x8000000000000000
    tmp2 = (b&1)*0x8000000000000000
    a = a >> 1
    b = b >> 1
    a |= tmp2
    b |= tmp1
    a&=0xffffffffffffffff
    b&=0xffffffffffffffff
    return a,b

a = 0x50A2DCC51ED6C4A2
b = 0xA1E8895EB916B732
for i in range(0x400):
    a, b = ror(a, b)
    tmp = b
    b = (a - b) & 0xffffffffffffffff
    a = tmp
    a, b = ror(a, b)
    if b&1:
        a^=b
    else:
        a^=(~b)
    b = ~b
    a&=0xffffffffffffffff
    b&=0xffffffffffffffff
flag = ''
for i in range(8):
    tmp = b&0xff
    b>>=8
    flag+=chr(tmp)
for i in range(8):
    tmp = a&0xff
    a>>=8
    flag+=chr(tmp)    
print(flag)
