bg = 0x000000CC
end = 0x0000706C

addr = bg

def next_instr(addr):
	return addr + ItemSize(addr)

f = open("data.txt",'w')

print >> f,'[[1,',
index = 0
while addr < end:
	next = next_instr(addr)
	if 'addiu' == GetMnem(addr) :
		i = str(GetOperandValue(addr, 1))
		dest = next_instr(next)
		if 'addu' == GetMnem(dest):
			print >> f,"1",
		elif 'subu' == GetMnem(dest):
			print >> f,"-1",
		if i == '41':
			print >> f,"],",
			print >> f,"[1",
		else:
			print >> f,',',
	addr = next_instr(addr)
f.close()