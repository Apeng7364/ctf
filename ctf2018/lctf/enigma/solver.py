from pwn import *

plain='DQYHTONIJLYNDLA'
flag = ''
context.log_level = 'warn'
for i in range(15):
    for ch in 'QWERRTYUIOPASDFGHJKLZXCVBNM':
        p=process('./enigma')
        p.sendline(flag+ch)
        t=p.recvline(False)
        p.close()
        if t==plain[0:i+1]:
            flag+=ch
            break
    print(flag)