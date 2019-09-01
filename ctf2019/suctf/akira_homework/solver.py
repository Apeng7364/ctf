from Crypto.Cipher import AES
aes = AES.new("Ak1i3aS3cre7K3y\x00")
cipher = "flag{Ak1rAWin!}\x00"
plain = aes.encrypt(cipher)
print(plain.encode("hex"))