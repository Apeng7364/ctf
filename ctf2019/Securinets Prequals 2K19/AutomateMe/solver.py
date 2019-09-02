f = open('bin','rb')
f.read(0x74C)
g = open('flag.txt','ab')

with open('bin','rb') as f:
    f.read(0x74C)
    while(True):
        temp = f.read(1)
        if temp =='':
            break
        temp = ord(temp)
        if temp == 0x3C:
            t = f.read(1)
            k = f.read(1)
            if k=='\x74':
                g.write(t)
        elif temp ==0x80:
            if ord(f.read(1))==0x75:
                f.read(1)
                t = ord(f.read(1))
                f.read(1)
                f.read(1)
                f.read(1)
                k = ord(f.read(1))
                g.write(chr(k^t))