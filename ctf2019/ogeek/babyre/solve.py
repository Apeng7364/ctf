f = open("output.file","rb")
g = open("input.file","wb")
bits = ""
i = 0
tmp = f.read(1)
tmpbuf = [0]*0x11
buf = [0]*0x1000
s = ""
k = 1
count = 1
debug = 0
while(True):
    
    bit = ord(tmp)
    if bit & 1<<(7-i):
        tmp1 = f.read(1)
        bit1 = ord(tmp1)

        bit<<=(i+1)
        bit &= 0xff
        bit |= (bit1>>(7-i))
        #print(hex(bit),i,hex(ord(tmp)),hex(ord(tmp1)))
        g.write(chr(bit))
        buf[count] = bit
        count+=1
        count %= 0x1000
        k+=1
        k%=0x1000
        s+=chr(bit)
        i = (i+1)%8
        if i == 0:
            tmp = f.read(1)
        else:
            tmp = tmp1
    else:
        tmp1 = f.read(1)
        tmp2 = f.read(1)
        bit1 = ord(tmp1)
        bit2 = ord(tmp2)
        m = (bit&((1<<(7-i))-1))<<(5+i)
        m&=0xFFF
        if i <=3:
            m |= (bit1 >>(3-i))
        else:
            m |= (bit1 << (i-3))
            m |= bit2 >> (8-(i-3))
        if i<=3:
            l = bit1 & ((1<<(3-i))-1)
            l <<= (1+i)
            l |= (bit2 >> (8-(1+i)))
        else:
            l = bit2 >> ((8-(i-3))-4)
        l &= 0b1111
        i = (i+1)%8
        if i == 0:
            tmp = f.read(1)
        else:
            tmp = tmp2
#         if debug<10:
#             print(l,m,hex(bit),i)
#             if debug == 6:
#                 print(buf)
#             debug+=1
#         else:
#             break
        l+=2
        for j in range(l):
            buf[(count+j)%0x1000] = buf[(m+j)%0x1000]
            #print(buf[(m+j)%0x1000])
            g.write(chr(buf[(m+j)%0x1000]))
        count+=l
        count%=0x1000
        k = 1
