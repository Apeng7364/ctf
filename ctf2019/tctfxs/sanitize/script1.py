from __future__ import print_function
from pwn import *  
from time import *
context.log_level = 'error'

u=6
seed = int(time())
def rand():
    global seed
    seed = seed * 0x343FD + 0x269EC3
    return (seed >> 16) & 0x7FFF  
flag = 'flag{'
payload = ''
# for j in range(5):
#     payload += chr((rand()%(0x7f-0x20))+0x20)
payload = '9L<!}'
print(payload)

for i in range(0x20,0x7f):
    f = open('flag','w+')
    f.write(flag+chr(i)+'a'*20)  #the sixth
    f.close()

    payload += '\n'
    payload+=str(3)+'\n'+str(0)+'\n'+str(1)+'\n'+str(5)+'\n'
    p = process('./sanitize')
    p.send(payload)
    s = p.recv()
    p.close()
    t=[]
    tt = []
    for j in range(len(s)/8):
        t.append(s[j*8:j*8+8])
    # print(t)
    for j in range(len(t)):
        temp = 0
        for k in range(4):
            temp+=int(t[j][2*k:2*k+2],16)*(256**k)
        tt.append(temp)
    print('%4d'%tt[38],end = '')
    print('%4d'%tt[39],end = '')
    print('%4d'%tt[42],end = ' ')
    print(chr(i))