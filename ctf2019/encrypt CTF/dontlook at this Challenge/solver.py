cipher = "hbpkjdhMWT{qhyhz00u__1wg_zr_dsqbhh}"
key = "dontlook"
plain = ""
t = 0
for i in range(len(cipher)):
    if ord(cipher[i])>=97 and ord(cipher[i])<=ord('z'):
        plain+=chr(((ord(cipher[i]) - 97) - (ord(key[t%8]) - 97) + 26)%26 + 97)
    elif ord(cipher[i])>=65 and ord(cipher[i])<=ord('Z'):
        plain+=chr(((ord(cipher[i]) - 65) - (ord(key[t%8]) - 97) + 26)%26 + 65)
    else:
        plain += cipher[i]
        continue
    t+=1
print(plain)
#或者直接动调看到结果