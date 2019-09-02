res = "J2261C63-3I2I-EGE4-IBCC-IE41A5I5F4HB"
t = map(ord,res)
print(t)
s = []
for i in t:
    if (i>=(ord('a')-0x30)) and (i<=(ord('z')-0x30)):
        i+=0x30
    elif (i>=(ord('0')+0x11) )and (i<= (ord('9') +0x11)):
        i-=0x11
    

    s.append(i)
s = "".join(map(chr,s))
print(s)