op=[0xA3,0xF9,0x77,0xA6,0xC1,0xC7,0x4E,0xD1,0x51,0xFF,0x93,0xC8,0x45,0x95,0xF5,0xF2,0x78,0xE6,0x69,0xC6,0x90,0xCD,0x40,0x96,0xF0,0xFE,0x78,0xE3,0x64,0xC7]
O=[[0x30133403,0x3401CC01,0x36327A09,0x3300CC00,0x3015CC04,0x35289D07,0x3027CC06,0x3412CC03,0x3026CD06,0x34081F01,0x3311C302,0x3625CC05,0x3930CC07,0x37249405,0x34027200,0x39236B04,0x34317308,0x3704CC02],
[0x38531F11,0x3435CC09,0x3842CC0A,0x3538CB0B,0x3750CC0D,0x3641710D,0x3855CC0F,0x3757CC10,0x3740000C,0x3147010F,0x3146CC0B,0x3743020E,0x36360F0A,0x3152CC0E,0x34549C12,0x34511110,0x3448CC0C,0x3633CC08],
[0x3080CC17,0x37742C16,0x3271CC14,0x3983CC19,0x3482BB17,0x3567BC15,0x3188041A,0x3965CC12,0x32869C19,0x3785CC1A,0x3281CC18,0x3262DC14,0x3573CC15,0x37566613,0x3161CC11,0x3266CC13,0x39844818,0x3777CC16]]

# cpuid(0xDEADBEEF)
for i in range(10):
    op[i]^=op[i+20]
	
# invd(0x4437)
v3 = op[7]
for k in range(3):
	op[k + 7] = op[6 - k]
	if ( k == 2 ):
		op[6 - k] = op[3]
	else:
		op[6 - k] = op[k + 8]
op[3] = op[1]
op[1] = op[2]
op[1] = v3

# invd(0x4433)
for i in range(5):
    v0 = op[2 * i]
    op[2 * i] = op[2 * i + 1]
    op[2 * i + 1] = v0
op0=op[0:10]

# invd(0x4434)
v5 = op[0]
for j in range(9):
	op[j] = op[j + 1]
op[9] = v5
op1=op[0:10]

# invd(4437)
v3 = op[7]
for k in range(3):
	op[k + 7] = op[6 - k]
	if ( k == 2 ):
		op[6 - k] = op[3]
	else:
		op[6 - k] = op[k + 8]
op[3] = op[1]
op[1] = op[2]
op[1] = v3
op2=op[0:10]
opa=[op0,op1,op2]

# get the operation
for i in range(3):    
    op=opa[i]
    for opcode in O[i]:
        v1 = opcode >> 24
        v2 = ((opcode>>16) & 0xF) + 9 * ((opcode>>20)&0xF)
		v3 = (opcode&0xff)
        if ( ((opcode>>8)&0xff) == 0xCC ):
            t=opcode&0xff
            t1=v3-1
            t2=v3+1
            t3=v3-2
            t4=v3+2
        else:
            t=26-v3
            t1=26-(v3-1)
            t2=26-(v3+1)
            t3=26-(v3-2)
            t4=26-(v3+2)

        if ( v1 == op[0] ):
            print("A[%d]=x[%d]"%(v2,t))
        elif ( v1 == op[1] ):
            print("A[%d]=(A[%d]+x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[2] ):
            print("A[%d]=(A[%d]-x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[3] ):
            print("A[%d]=(A[%d]/x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[4] ):
            print("A[%d]=(A[%d]*x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[5] ):
            print("A[%d]=(A[%d]^x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[6] ):
            print("A[%d]=(A[%d]^(x[%d]+x[%d]-x[%d]))&0xFF"%(v2,v2,t1,t,t2))
        elif ( v1 == op[7] ):
            print("A[%d]=(A[%d]^(x[%d]<<4))&0xFF"%(v2,v2,t))
        elif ( v1 == op[8] ):
            print("A[%d]=(A[%d]|x[%d])&0xFF"%(v2,v2,t))
        elif ( v1 == op[9] ):
            print("A[%d]=(A[%d]^(x[%d]^x[%d]^x[%d]+x[%d]-x[%d]))&0xFF"%(v2,v2,t2,t1,t3,t,t4))
    print()




