

from ida_bytes import get_bytes, patch_bytes, get_dword
from struct import pack, unpack
addr = 0x4005C0
buf = get_bytes(addr, 0x4E837D - addr)
def patch_at(p, ln):
    global buf
    buf = buf[:p] + "\x90" * ln + buf[p+ln:]
    
pattern = 'B00184C00F85'.decode('hex')
p = buf.find(pattern)
while p != -1:
    if buf[p + 6 + 4:p + 6 + 4 + 5] == '\xE9\x00\x00\x00\x00':
        dst = p + 6 + 4 + get_dword(addr + p + 6)
        off = dst - p - 5
        t = '\xE9' + pack('<I', off)
        t = t.ljust(6 + 4 + 5, '\x90')
        patch_bytes(addr + p, t)
        print(hex(addr + p), hex(addr + dst))
    else:
        pass
    p = buf.find(pattern, p+1)
    
pattern = '31C088C184C90F85'.decode('hex')
p = buf.find(pattern)
while p != -1:
    if buf[p + 8 + 4:p + 8 + 4 + 5] == '\xE9\x00\x00\x00\x00':
        patch_bytes(addr + p, '\x90' * (8+4+5))
        print(hex(addr + p), hex(addr + dst))
    else:
        pass
    p = buf.find(pattern, p+1)