from pwn import *
from hashlib import md5

# context.log_level = 'debug'
p = remote('e552a168f687.gamectf.com', 9999)



subkey = []
sbox = [0x0B, 0x0C9, 0x0AC, 0x0A6, 0x63, 0x0F3, 0x0FE, 0x0A3, 0x0E0, 0x27, 0x22, 0x0CE, 0x0EE, 0x0, 0x0CA, 0x34, 0x15, 0x4A, 0x8A, 0x9A, 0x0A2, 0x36, 0x0ED, 0x5E, 0x0BA, 0x0D8, 0x0F9, 0x76, 0x65, 0x31, 0x55, 0x0C3, 0x0CC, 0x0C1, 0x0E, 0x1B, 0x0E4, 0x7A, 0x43, 0x54, 0x95, 0x6F, 0x0FA, 0x61, 0x0BE, 0x1E, 0x0E2, 0x46, 0x4D, 0x49, 0x0A7, 0x2B, 0x0D1, 0x0F, 0x2A, 0x58, 0x0C4, 0x0AD, 0x5, 0x42, 0x33, 0x78, 0x0EA, 0x72, 0x6E, 0x0AE, 0x0AB, 0x0E6, 0x0F2, 0x4, 0x96, 0x90, 0x66, 0x0A, 0x1, 0x40, 0x8D, 0x0AF, 0x23, 0x57, 0x0B2, 0x0C5, 0x41, 0x0AA, 0x0B3, 0x92, 0x70, 0x0DC, 0x2D, 0x0B8, 0x47, 0x94, 0x6D, 0x1C, 0x0EF, 0x12, 0x38, 0x0C7, 0x0B7, 0x18, 0x0BD, 0x87, 0x0B6, 0x91, 0x13, 0x50, 0x0F7, 0x4B, 0x67, 0x0D5, 0x64, 0x68, 0x4E, 0x75, 0x0A4, 0x7B, 0x0BB, 0x4F, 0x8E, 0x7C, 0x0F0, 0x5A, 0x74, 0x0D7, 0x35, 0x0D4, 0x7F, 0x0F4, 0x0CD, 0x83, 0x2C, 0x30, 0x0D6, 0x5F, 0x1A, 0x2E, 0x24, 0x0C6, 0x71, 0x56, 0x11, 0x0FF, 0x0C2, 0x0C, 0x93, 0x99, 0x0E1, 0x21, 0x77, 0x1F, 0x0E3, 0x0A0, 0x3D, 0x29, 0x5C, 0x0E9, 0x84, 0x9C, 0x8F, 0x10, 0x17, 0x0B1, 0x7E, 0x48, 0x0F6, 0x0B4, 0x0E5, 0x6B, 0x0DE, 0x0D0, 0x20, 0x86, 0x0CB, 0x0DA, 0x85, 0x14, 0x82, 0x16, 0x52, 0x5B, 0x0B5, 0x0BC, 0x44, 0x2, 0x7, 0x0DB, 0x0F5, 0x19, 0x7D, 0x0D2, 0x39, 0x9E, 0x3E, 0x32, 0x5D, 0x6, 0x0F8, 0x6C, 0x0EB, 0x6A, 0x8, 0x0DF, 0x2F, 0x79, 0x4C, 0x8B, 0x0CF, 0x81, 0x88, 0x0D9, 0x73, 0x0E8, 0x89, 0x0EC, 0x3A, 0x59, 0x25, 0x3F, 0x3C, 0x97, 0x0FB, 0x69, 0x53, 0x0D, 0x0FD, 0x0E7, 0x0C8, 0x60, 0x3B, 0x80, 0x51, 0x8C, 0x28, 0x3, 0x0F1, 0x0FC, 0x0BF, 0x45, 0x98, 0x0A5, 0x1D, 0x26, 0x0A8, 0x0C0, 0x9B, 0x0A9, 0x0B0, 0x0A1, 0x9F, 0x0DD, 0x9, 0x9D, 0x37, 0x0D3, 0x62, 0x0B9]

desbox = [13, 74, 183, 233, 69, 58, 195, 184, 200, 250, 73, 0, 143, 223, 34, 53, 159, 140, 95, 104, 175, 16, 177, 160, 99, 187, 134, 35, 93, 240, 45, 149, 170, 147, 10, 78, 136, 216, 241, 9, 232, 153, 54, 51, 130, 88, 135, 202, 131, 29, 193, 60, 15, 124, 21, 252, 96, 190, 214, 228, 218, 152, 192, 217, 75, 82, 59, 38, 182, 237, 47, 90, 163, 49, 17, 107, 204, 48, 112, 117, 105, 230, 178, 222, 39, 30, 139, 79, 55, 215, 121, 179, 154, 194, 23, 133, 227, 43, 254, 4, 110, 28, 72, 108, 111, 221, 199, 167, 197, 92, 64, 41, 86, 138, 63, 210, 122, 113, 27, 148, 61, 203, 37, 115, 119, 188, 162, 126, 229, 207, 176, 129, 156, 174, 171, 101, 208, 212, 18, 205, 231, 76, 118, 158, 71, 103, 85, 144, 91, 40, 70, 219, 238, 145, 19, 244, 157, 251, 191, 248, 151, 247, 20, 7, 114, 239, 3, 50, 242, 245, 83, 66, 2, 57, 65, 77, 246, 161, 80, 84, 165, 180, 102, 98, 89, 255, 24, 116, 181, 100, 44, 236, 243, 33, 142, 31, 56, 81, 137, 97, 226, 1, 14, 172, 32, 128, 11, 206, 169, 52, 189, 253, 125, 109, 132, 123, 25, 209, 173, 185, 87, 249, 168, 201, 8, 146, 46, 150, 36, 166, 67, 225, 211, 155, 62, 198, 213, 22, 12, 94, 120, 234, 68, 5, 127, 186, 164, 106, 196, 26, 42, 220, 235, 224, 6, 141]

mixs = [0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27, 35, 43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7, 15, 23, 31, 39, 47, 55, 63]

def long2bit(a):
    res = []
    for i in range(64):
        res.append(a&0x1)
        a>>=1
    return res

def bit2long(a):
    res = 0
    for i in range(63,-1,-1):
        res<<=1
        res+=a[i]
    return res
        
def long2byte(a):
    res = []
    for i in range(8):
        res.append(a&0xff)
        a>>=8
    return res

def byte2long(a):
    res = 0
    for i in range(7,-1,-1):
        res<<=8
        res+=a[i]
        
    return res
def subbytes(a):
    b = long2byte(a)
    for i in range(8):
        b[i] = desbox[b[i]]
    res = byte2long(b)
    return res
    
def mix(a):
    bits = long2bit(a)
    res_bit = [0] * 64
    for i in range(64):
        res_bit[mixs[i]] = bits[i]
    res = bit2long(res_bit)
    return res

def decrypt(key, cipher):
    # key = "31323334353637386162636465666768"
    # cipher = 8815030963248612207

    k = key
    ka = k[0:8]
    ka = ka[::-1].encode("hex")
    kb = k[8:16]
    kb = kb[::-1].encode("hex")
    a = int(ka,16)
    b = int(kb,16)

    for i in range(64,-1,-4):
        tmp = a>>i | b <<(64 - i)
        tmp &= 0xffffffffffffffff
        if i == 64 or i == 0:
            tmp = a|b
        subkey.append(tmp)

    cipher ^= subkey[16]
    cipher = subbytes(cipher)
    cipher ^= subkey[15]
    for i in range(15):
        cipher = mix(cipher)
        cipher = subbytes(cipher)
        cipher ^= subkey[14-i]
    # print(cipher, hex(cipher), hex(cipher)[2:-1], hex(cipher)[2:].rstrip('L'))
    cipher = hex(cipher)[2:].rstrip('L').decode("hex")
    cipher = cipher[::-1]
    # print(cipher)
    return cipher

def cmd(c):
    p.sendlineafter('_>', c)

def radar():
    cmd('radr')
    mp = []
    for i in xrange(4):
        lvl = []
        for j in xrange(5):
            t = p.recvline(False)
            lvl.append(t)
        t = p.recvline(False)
        assert t == '--------', t
        mp.append(lvl[:])
    return mp

def radr():
    r = radar()
    s = ''
    for lvl in reversed(r):
        for row in lvl:
            s += row + '\n'
        s += '--------\n'
    print(s)
    # return s

def mov(dr, times = 1, show = True):
    drs = {
        'nxt': '3355',
        'n': '5555',
        's': '3333',
        'w': '3535',
        'e': '5353',
        'nw': '4545',
        'sw': '3434',
        'ne': '5454',
        'se': '4343',
    }
    for i in xrange(4):
        cmd('set r%d %s' % (i + 1, drs[dr][i]))
    cmd('run %d' % (times))
    if show:
        radr()

def nxt(times = 1, show = True):
    mov('nxt', times, show)
def n(times = 1, show = True):
    mov('n', times, show)
def s(times = 1, show = True):
    mov('s', times, show)
def w(times = 1, show = True):
    mov('w', times, show)
def e(times = 1, show = True):
    mov('e', times, show)
def nw(times = 1, show = True):
    mov('nw', times, show)
def sw(times = 1, show = True):
    mov('sw', times, show)
def ne(times = 1, show = True):
    mov('ne', times, show)
def se(times = 1, show = True):
    mov('se', times, show)

def land():
    cmd('land')
    t = p.recvline(False)
    assert len(t) == 32, t
    key1 = unhex(t)
    t = p.recvline(False)
    key3 = int(t)
    ans = decrypt(key1, key3)
    p.sendline(ans)

def fire():
    cmd('fire')
    t = p.recvline(False)
    assert len(t) == 32, t
    t = unhex(t)
    ans = None
    for i in xrange(1 << 31):
        if md5(p32(i)).digest() == t:
            ans = i
    assert ans != None, ans
    p.sendline(str(ans))

def find_item(mp, item):
    dstx, dsty = None, None
    for x in xrange(8):
        for y in xrange(5):
            if mp[4 - y][x] == item:
                dstx, dsty = x, y
        if dstx != None and dsty != None:
            break
    assert dstx != None and dsty != None, mp
    return dstx, dsty

dest = None
mp = None
paths = None

def up():
    maps = radar()
    assert ''.join(maps[1]).count(' ') == 1, maps[1]
    assert ''.join(maps[0]).count('U') == 1, maps[0]
    dst = find_item(maps[1], ' ')
    auto(dst)
    nxt(show=False)
    nxt(show=False)

def auto(dst):
    global dest, mp, paths
    dest = dst
    usr = find_item(maps[0], 'U')
    mp = map(list, maps[0])
    mp[4 - usr[1]][usr[0]] = 'U'
    paths = []
    recrusion(usr, [])
    best = sorted(paths, key = lambda x:len(x))[0]
    for step in best:
        mov(step, show = False)
    
def recrusion(cur, path):
    global dest, mp, paths
    curx, cury = cur
    if cur == dest:
        paths.append(path[:])
        return
    if mp[4 - cury][curx] in ['#', 'X']:
        return
    mp[4 - cury][curx] = 'X'
    
    if curx < 7:
        recrusion((curx + 1, cury), path + ['e'])
    if curx > 0:
        recrusion((curx - 1, cury), path + ['w'])
    if cury < 4:
        recrusion((curx, cury + 1), path + ['n'])
    if cury > 0:
        recrusion((curx, cury - 1), path + ['s'])
    if curx > 0 and cury > 0:
        recrusion((curx - 1, cury - 1), path + ['sw'])
    if curx < 7 and cury > 0:
        recrusion((curx + 1, cury - 1), path + ['se'])
    if curx > 0 and cury < 4:
        recrusion((curx - 1, cury + 1), path + ['nw'])
    if curx < 7 and cury < 4:
        recrusion((curx + 1, cury + 1), path + ['ne'])
    mp[4 - cury][curx] = ' '


maps = radar()
t = ''.join(maps[0])
while t.count('E') != 1 and t.count('B') != 1:
    up()
    # radr()
    maps = radar()
    t = ''.join(maps[0])

assert not (t.count('E') == 1 and t.count('B') == 1), maps[0]
item = 'E' if t.count('E') == 1 else 'B'        
dst = find_item(maps[0], item)
dst = dst[0], 1
auto(dst)
radr()
# land()
    
# maps = radar()
# t = ''.join(maps[1])

# if t.count('D') == 1:

#     dst = find_item(maps[1], 'D')
#     auto(dst)
#     # radr()
#     fire()
#     maps = radar()
#     t = ''.join(maps[0])

