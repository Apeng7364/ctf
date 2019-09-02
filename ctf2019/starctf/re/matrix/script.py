bg = 0x000027A0
end = 0x00010B80
main_return = 0x00005C10
addr = bg
print('start at %08x'%addr)
def patch_nop(begin,end):
    while(end>begin):
        PatchByte(begin,0x90)
        begin=begin+1
def next_instr(addr):
    return addr+ItemSize(addr)
while(addr<end):
    next_addr =next_instr(addr)
    MakeCode(next_addr)
    addr = next_instr(addr)
    MakeCode(addr)
    if 'jmp     $+5' in GetDisasm(addr):
        print('ret :%08x'%addr)
        patch_nop(addr,addr+5)
        PatchByte(addr + 6,0xC3)
        patch_nop(addr + 7, addr + 9)
        addr = addr + 9
    if 'xor' in GetDisasm(addr) and GetOpnd(addr,0) == GetOpnd(addr,1) and 'jnz' in GetDisasm(addr + 2):
        patch_nop(addr, addr + 4)
        print('xor jmp: %08x'%addr)
        patch_nop(addr, addr + 4)
        addr = addr + 4
    
    if 'call    $+5' in GetDisasm(addr):
        print('nop: %08x'%addr)
        patch_nop(addr,addr+0xB)
        PatchByte(addr + 0xA, 0xE8)
        addr = addr + 0xF
print('end')