from pwn import *
context.log_level = 'debug'
p = process('./crackme01')
p.sendline('1D\x01A  !!e\x19\t')
print(p.recv())