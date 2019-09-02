import base64
import string
from pysm4 import *
a = "IJLMNOPKABDEFGHCQRTUVWXSYZbcdefa45789+/6ghjklmnioprstuvqwxz0123y"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base_fix = "RVYtG85NQ9OPHU4uQ8AuFM+MHVVrFMJMR8FuF8WJQ8Y="
key = int('DA98F1DA312AB753A5703A0BFD290DD6',16)
table = string.maketrans(a, b)
cipher = int(base64.b64decode(base_fix.translate(table)),16)
plain = decrypt(cipher,key)
username = hex(plain)[2:-1].decode('hex').decode('hex')
password = "xyz{|}"
print(username)
print(password)