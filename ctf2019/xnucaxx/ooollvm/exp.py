from pwn import *
context.log_level = "error"
res = "flag{this_is_a_naive_but_hard_obfuscated_program_compiled_by_llvm_pass}"
lenth = len(res)
print(lenth)
p = process("./ooollvm")
for i in range(lenth,70):
    for j in range(0x20,0x7f):
        print chr(j),
        p.close()
        p = process("./ooollvm")
        p.sendline(res + chr(j))
        for k in range(lenth-2):
            p.recvline()
        t = p.recvline().strip()
        if t == "N":
            print("")
            print(res+chr(j))
            if chr(j) == res[-2] or chr(j) == res[-1]:
                continue
            res+=chr(j)
            lenth = len(res)
            print(res)
    