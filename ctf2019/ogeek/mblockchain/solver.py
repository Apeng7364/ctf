from Crypto.Cipher import AES
from hashlib import md5
foundpad = "\x10"*16


cipher = "74f0b165db8a628716b53a9d4f6405980db2f833afa1ed5eeb4304c5220bdc0b541f857a7348074b2a7775d691e71b490402621e8a53bad4cf7ad4fcc15f20a8066e087fc1b2ffb21c27463b5737e34738a6244e1630d8fa1bf4f38b7e71d707425c8225f240f4bd2b03d6c2471e900b75154eb6f9dfbdf5a4eca9de5163f9b3ee82959f166924e8ad5f1d744c51416a1db89638bb4d1411aa1b1307d88c1fb5".decode("hex")
"""
cipherpad = cipher[-16:]
for i in range(240,256):
    print(i)
    for j in range(256):
        for k in range(256):
            key = chr(i) + chr(j) + chr(k)
            ck = key
            for _ in range(10):
                ck = md5(ck).digest()
            aes = AES.new(ck,mode = AES.MODE_ECB)
            cp = aes.decrypt(cipherpad)
            if cp == foundpad:
                print(cp.encode("hex"))
                print(ck.encode("hex"))
                print(i,j,k)
                exit()

"""
key = chr(241) + chr(183) + chr(36)
subkey = []
ck = key
for i  in range(10):
    subkey.append(md5(ck).digest())
    ck = md5(ck).digest()
for i in range(10):
    ck = subkey[9-i]
    aes = AES.new(ck)
    cipher = aes.decrypt(cipher)
print(cipher)