st = 0x404000
key = map(ord,list("sycloversyclover"))
for i in range(512):
    tmp = ord(get_bytes(st,1))
    tmp^=key[i%16]
    tmp = ~tmp
    patch_bytes(st,chr(tmp))
    st+=1