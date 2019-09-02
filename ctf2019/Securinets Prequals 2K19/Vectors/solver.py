from pwn import *
from itertools import *
context.log_level = 'error'
a = [0xad,0xef,0xbe,0xde,0xc,0xed,0xd]
b = permutations(a,7)
for i in b:
    p = process('./bin')
    payload = ''
    for j in range(7):
        k = hex(i[j])[2:]
        if(len(k)==1):
            k = '0'+k
        payload+=k
    p.recv()
    p.sendline(payload)
    p.recvuntil('FLAG:')
    a = p.recv()
    if a.startswith('securinets'):
        print(a)
        exit()
    p.close()
