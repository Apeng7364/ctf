st = 0x403DE3
end = 0x00000000004E83B6
addr = st

def next_instr(addr):
    return addr+ItemSize(addr)

def patch_puts(addr):
    PatchByte(addr,0xE8)
    addr+=1
    opv = 0x400470 - (addr + 4)
    opv&=0xffffffff
    PatchDword(addr,opv)
    #print(hex(opv)[2:-1])
def patch_jmp(addr, dest):
    PatchByte(addr, 0xE9)
    offset = dest - (addr + 5)
    #print(hex(offset))
    PatchDword(addr+1, offset)
i = 0
while addr<end:
    next = next_instr(addr)
    dis = GetDisasm(addr)
    if dis == "mov     [rbp+var_14], ecx" and "jmp" in GetDisasm(next):
        i+=1
        print(hex(addr)[2:-1])
        addr = next
        dest = GetOperandValue(addr, 0)
        #print(hex(dest)[2:-1])
        PatchByte(addr, 0x85)
        PatchByte(addr+1, 0xC9)
        PatchByte(addr+2, 0x75)
        PatchByte(addr+3, 0x0c)
        PatchByte(addr+4, 0x48)
        PatchByte(addr+5, 0xc7)
        PatchByte(addr+6, 0xc7)
        PatchByte(addr+7, 0x50)
        PatchByte(addr+8, 0x84)
        PatchByte(addr+9, 0x4e)
        PatchByte(addr+10, 0x00)
        addr += 11
        patch_puts(addr)
        addr += 5
        patch_jmp(addr, dest)
        #break
        continue
    addr = next
print(i)