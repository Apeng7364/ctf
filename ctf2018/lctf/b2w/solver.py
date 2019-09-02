from struct import unpack
f = open("./out.wav", "rb")
header = f.read(0xC)
fmt = f.read(0x18)
data = f.read(0x8)
buf = f.read()
f.close()

chennel=2
rate = 48000
lenth = 90000

key = bytearray("LCTF{LcTF_1s_S0Oo0Oo_c0o1_6uT_tH1S_iS_n0t_fL4g}")
ln =len(key)
temp=bytearray(buf)

n=0
for i in range(lenth*chennel):
    m=key[n%ln]
    temp[2*i]^=m
    temp[2*i+1]^=m
    n+=m

buf = str(temp)
f = open("./dec.wav", "wb")
f.write(header + fmt + data + buf)
f.close()