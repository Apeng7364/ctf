from pwn import *
p = remote('39.106.224.151','10001')
print(p.recv())
p.sendline('badrer12')
print(p.recv())
p.send('xyz{|}')
print(p.recv())