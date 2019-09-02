from base64 import b64decode
from Crypto.Cipher import AES
key = b"sycloversyclover"
iv = b"sctfsctfsctfsctf"
aes = AES.new(key, mode = AES.MODE_CBC, iv = iv)
res = b"nKnbHsgqD3aNEB91jB3gEzAr+IklQwT1bSs3+bXpeuo="
cipher = b64decode(res)
tmp = aes.decrypt(cipher)
print(tmp)