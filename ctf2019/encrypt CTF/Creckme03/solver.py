from pwn import *
context.log_level = 'error'
payload = ["CRACKME02","\xef\xbe\xad\xde","ZXytUb9fl78evgJy3KJN","1","\x75\x7e\x77\x79\x69\x50\x70\x50\x60"]
p = process('./crackme03')
p = remote("104.154.106.182","7777")
for i in range(5):
    print(p.recv())
    p.sendline(payload[i])
print(p.recvall())
