bg = 0x00000378
end = 0x00007058
addr = bg

def next_instr(addr):
    return addr+ItemSize(addr)
counter = 0
counter_c = 1

while(addr<end):
    counter = 0
    print "flag[0]",
    while(True):
        next = next_instr(addr)
        mnem = GetMnem(addr)
        
        if 'addiu' in mnem:
            counter+=1
        elif 'addu' in mnem:
            print "+ flag[%d]"%counter,
        elif "subu" in mnem:
            print "- flag[%d]"%counter,
        if "sw" in GetDisasm(addr):
            print("== cipher[%d]"%counter_c)
            addr = next
            addr = next_instr(addr)
            addr = next_instr(addr)
            break
        addr = next
    counter_c+=1