from pwn import *
context.log_level = "error"
f = open("op.txt","w")
p = process("./fly")
for i in range(0x20,0x7f):
    print i,
    for j in range(0x20,0x7f):
        
        for k in range(0x20,0x7f):
            print k,
            for l in range(0x20,0x7f):
                s = chr(i)+chr(j)+chr(k)+chr(l)
                p.close()
                p = process("./fly")
                p.recvuntil("_>")
                p.sendline(s)
                res = p.recvline().strip()
                if(res!="wrong"):
                    print(s)
                    f.wirte(s + "\n")