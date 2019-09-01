from pysm4 import decrypt
key = [13, 204, 99, 177, 254, 41, 198, 163, 201, 226, 56, 214, 192, 194, 98, 104]
c = [46, 48, 220, 156, 184, 218, 57, 13, 246, 91, 1, 63, 60, 67, 105, 64, 149, 240, 217, 77, 107, 49, 222, 61, 155, 225, 231, 196, 167, 121, 9, 16, 60, 182, 65, 101, 39, 253, 250, 224, 9, 204, 154, 122, 206, 43, 97, 59]
key = "".join(map(chr,key))
c = "".join(map(chr,c))
plain = ""
for i in range(3):
    t = c[i*16:i*16+16].encode("hex")
    cipher_num = eval("0x"+t)
    mk = 0x0dcc63b1fe29c6a3c9e238d6c0c26268
    m = decrypt(cipher_num,mk)
    plain+=hex(m)[2:-1].decode("hex")
print(plain)