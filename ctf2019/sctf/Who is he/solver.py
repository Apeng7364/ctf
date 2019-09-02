import base64
from binascii import unhexlify
from Crypto.Cipher import DES
key = b"t\x00e\x00s\x00t\x00"
# print(a)
# print(key)
des = DES.new(key, mode = DES.MODE_CBC, iv = key)
a = b"xZWDZaKEhWNMCbiGYPBIlY3+arozO9zonwrYLiVL4njSez2RYM2WwsGnsnjCDnHs7N43aFvNE54noSadP9F8eEpvTs5QPG+KL0TDE/40nbU="
a = base64.b64decode(a)
res = des.decrypt(a)[0:-6].decode("utf-16")
print(res)