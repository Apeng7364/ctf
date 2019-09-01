## Prime

题目给出4个N，不知道是咋生成的

瞎试，发现n0 n1不互质，后来发现任意两个都不互质，然后就能求出每个n的四个因子。

```python
from pwn import *
from hashlib import md5
import decimal
import gmpy2
def gcd(a, b):
   if a < b:
     a, b = b, a
   while b != 0:
     temp = a % b
     a = b
     b = temp
   return a

a = 0
def oracle(num):
    p.recvuntil("Please input your option:")
    p.sendline("D")
    p.recvuntil("Your encrypted message:")
    p.sendline(str(num))
    p.recvuntil("The plain of your decrypted message is ")
    lsb = p.recv(3)
    return lsb == 'odd'

def partial(c,e,n):
    k = n.bit_length()
    decimal.getcontext().prec = k  # for 'precise enough' floats
    lo = decimal.Decimal(0)
    hi = decimal.Decimal(n)
    for i in range(k):
        if not oracle(c):
            hi = (lo + hi) / 2
        else:
            lo = (lo + hi) / 2
        c = (c * pow(2, e, n)) % n
        print i, int(hi - lo)
    return int(hi)

s = "0123456789abcdefABCDEF"
p = remote("47.111.59.243","8003")
p.recvuntil("[*] Please find a string that md5(str + ")
salt = p.recv(4)
p.recvuntil("[0:5] == ")
part_hash = p.recv(5)
found = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for m in s:
                    ss = i+j+k+l+m
                    if md5(ss+salt).hexdigest()[:5] == part_hash:
                        found = 1
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

p.recvuntil("> ")
p.sendline(ss)

p.recvuntil("cs[0] = ")
c1 = eval(p.recvline())
p.recvuntil("ns[0] = ")
n1 = eval(p.recvline())
p.recvuntil("cs[1] = ")
c2 = eval(p.recvline())
p.recvuntil("ns[1] = ")
n2 = eval(p.recvline())
p.recvuntil("cs[2] = ")
c3 = eval(p.recvline())
p.recvuntil("ns[2] = ")
n3 = eval(p.recvline())
p.recvuntil("cs[3] = ")
c4 = eval(p.recvline())
p.recvuntil("ns[3] = ")
n4 = eval(p.recvline())


n1p1 = gcd(n1,n2)
n1p2 = gcd(n1,n3)
n1p3 = gcd(n1,n4)
n1p4 = n1/(n1p1*n1p2*n1p3)
d1=int(gmpy2.invert(n1,(n1p1-1)*(n1p2-1)*(n1p3-1)*(n1p4-1)))
m1 = pow(c1,d1,n1)

n2p1 = gcd(n2,n1)
n2p2 = gcd(n2,n3)
n2p3 = gcd(n2,n4)
n2p4 = n2/(n2p1*n2p2*n2p3)
d2=int(gmpy2.invert(n2,(n2p1-1)*(n2p2-1)*(n2p3-1)*(n2p4-1)))
m2 = pow(c2,d2,n2)

n3p1 = gcd(n3,n1)
n3p2 = gcd(n3,n2)
n3p3 = gcd(n3,n4)
n3p4 = n3/(n3p1*n3p2*n3p3)
d3=int(gmpy2.invert(n3,(n3p1-1)*(n3p2-1)*(n3p3-1)*(n3p4-1)))
m3 = pow(c3,d3,n3)

n4p1 = gcd(n4,n2)
n4p2 = gcd(n4,n3)
n4p3 = gcd(n4,n1)
n4p4 = n4/(n4p1*n4p2*n4p3)
d4=int(gmpy2.invert(n4,(n4p1-1)*(n4p2-1)*(n4p3-1)*(n4p4-1)))
m4 = pow(c4,d4,n4)

p.recvuntil("ms[0] = ")
p.sendline(hex(m1))

p.recvuntil("ms[1] = ")
p.sendline(hex(m2))

p.recvuntil("ms[2] = ")
p.sendline(hex(m3))

p.recvuntil("ms[3] = ")
p.sendline(hex(m4))

print(p.recvline().strip())
```

