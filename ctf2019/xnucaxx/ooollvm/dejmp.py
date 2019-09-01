st = 0x4005C0
end = 0x4E837D
addr = st

def next_instr(addr):
    return addr+ItemSize(addr)
    
def patch_nop(begin,end):
    while(end>begin):
        PatchByte(begin,0x90)
        begin=begin+1

while(addr<end):
    next = next_instr(addr)
    if "jmp     $+5" == GetDisasm(addr):
        patch_nop(addr,addr+5)
        print("jmp $+5", hex(addr))
        addr+=5
        continue
    addr = next