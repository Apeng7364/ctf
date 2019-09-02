# Reverse

## 8V

V8的汇编代码。

简单的异或加密，每次异或密钥的值都会改变

```python
res = "\xd2\"\xf1\x8d\xb7\xe0\xd0MF\x87T?\x1fI\x1c\xe7\xcb\x07\xc3\x95z\xb3z\x0b\xbb\xdb\xa1I\xc5;"
res = map(ord,list(res))
a3 = 88
for i in range(30):
    res[i] ^= a3
    a3 *= 65
    a3 += 66
    a3 %=256
for i in range(30)[::-1]:
    res[i]^=a3
    a3 *=35
    a3 -=16
    a3 %=256
print("".join(map(chr,res)))
```

## babyre

lz77压缩算法，写出解压算法

```python
f = open("output.file","rb")
g = open("input.file","wb")
bits = ""
i = 0
tmp = f.read(1)
tmpbuf = [0]*0x11
buf = [0]*0x1000
s = ""
k = 1
count = 1
debug = 0
while(True):
    
    bit = ord(tmp)
    if bit & 1<<(7-i):
        tmp1 = f.read(1)
        bit1 = ord(tmp1)

        bit<<=(i+1)
        bit &= 0xff
        bit |= (bit1>>(7-i))
        #print(hex(bit),i,hex(ord(tmp)),hex(ord(tmp1)))
        g.write(chr(bit))
        buf[count] = bit
        count+=1
        count %= 0x1000
        k+=1
        k%=0x1000
        s+=chr(bit)
        i = (i+1)%8
        if i == 0:
            tmp = f.read(1)
        else:
            tmp = tmp1
    else:
        tmp1 = f.read(1)
        tmp2 = f.read(1)
        bit1 = ord(tmp1)
        bit2 = ord(tmp2)
        m = (bit&((1<<(7-i))-1))<<(5+i)
        m&=0xFFF
        if i <=3:
            m |= (bit1 >>(3-i))
        else:
            m |= (bit1 << (i-3))
            m |= bit2 >> (8-(i-3))
        if i<=3:
            l = bit1 & ((1<<(3-i))-1)
            l <<= (1+i)
            l |= (bit2 >> (8-(1+i)))
        else:
            l = bit2 >> ((8-(i-3))-4)
        l &= 0b1111
        i = (i+1)%8
        if i == 0:
            tmp = f.read(1)
        else:
            tmp = tmp2
#         if debug<10:
#             print(l,m,hex(bit),i)
#             if debug == 6:
#                 print(buf)
#             debug+=1
#         else:
#             break
        l+=2
        for j in range(l):
            buf[(count+j)%0x1000] = buf[(m+j)%0x1000]
            #print(buf[(m+j)%0x1000])
            g.write(chr(buf[(m+j)%0x1000]))
        count+=l
        count%=0x1000
        k = 1

```

解压后打开bmp得到flag

## King of KOF

一个KOF的安装包。一开始不知道安装包是nisi，硬调的。

注意到`40B5A8`和`40BDA8`是用来存放临时字符串的。

`sub_401434`是nisi的解释器。

安装后需要输入注册码。查找字符串查不到提示语。

用CE查找UTF16字符串，很快能找到提示语。在附近观察字符串，注意到一些比较有用的信息：`这是注册码`，注册码校验失败后的提示信息，`fnCheck`，`fnKoF97`，`Base64Encode`，一些提示输入flag的提示语，还有一串base64字符串：

```
cYZ1KIjhiR7Ol4RN9c0Xh7XryYfUD7A0m96h0/MQMI45mVhgTAnAtENpnzVKhfDZpVzfuiCBx5+BctkWo0GfU5qIYQV1bnFbNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1zYqDbEN0VbXNioNsQ3RVtc2Kg2xDdFW1w=
```

b64decode再hexencoe得到：

```
7186752888e1891ece97844df5cd1787b5ebc987d40fb0349bdea1d3f310308e399958604c09c0b443699f354a85f0d9a55cdfba2081c79f8172d916a3419f539a886105756e715b36c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5cd8a836c437455b5c
```

可以看到，后面有一长串8个字符重复，估计都是同样的字符加密，padding长度是8，估计都是由'\x00'*8加密得到的密文。分组长度为8的加密一开始想到的就是des，但是没有密钥。

跟踪调试几步后，发现在`40B5A8`和`40BDA8`对比了输入和常量，常量是用UTF-16存储的，之前的字符串`这是注册码`就是注册码

之后校验flag的部分比较复杂，观察这两个地方的数据，注意到在`user\AppData\Local\Temp\nsiF181.tmp`目录创建了一些临时dll。同时从0-255遍历每个字符，可能是获取字符的ascii的utf-16值？遍历完所有后跟踪不久可以发现多了一个奇怪的KOF91.dll

复制出来ida打开，发现加了壳，不过是比较简单的壳。

重新开始调试，这次在输入flag之后，x86dbg选项中打开加载dll后中断，可以看到KOF97.dll被加载了，入口点在8000，81C4壳的代码执行完成。这时候就可以用插件把dlldump下来了。

dump后发现fnCheck与fnKoF97两个函数。这两个就是校验与加密函数，加密算法是TEA，密钥在算法内。用它来解密之前的密文，得到

```
dj_eyucjamkc]rm]rfc]emmb+mjb+b_wq{
```

发现前四个字符和flag字符偏移固定为2，是个凯撒密码，加密可能在之前的nisi里面。修正一下得到flag

```C
#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"

void decrypt (uint32_t v[2], uint32_t k[4]) {
    uint32_t v0=v[0], v1=v[1], sum=0xC6EF3720, i;  /* set up; sum is 32*delta */
    uint32_t delta=0x9E3779B9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i<32; i++) {                         /* basic cycle start */
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

int main()
{
    uint32_t key[4] = {0x20776F77,0x20756F79,0x646E6966,0x21656D20};
    uint8_t cipher[] = {113, 134, 117, 40, 136, 225, 137, 30, 206, 151, 132, 77, 245, 205, 23, 135, 181, 235, 201, 135, 212, 15, 176, 52, 155, 222, 161, 211, 243, 16, 48, 142, 57, 153, 88, 96, 76, 9, 192, 180, 67, 105, 159, 53, 74, 133, 240, 217, 165, 92, 223, 186, 32, 129, 199, 159, 129, 114, 217, 22, 163, 65, 159, 83, 154, 136, 97, 5, 117, 110, 113, 91, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168, 54, 196, 55, 69, 91, 92, 216, 168,0};
    int i;
    uint32_t *p = (uint32_t*)cipher;
    for(i = 0;i<30;i++)
    {
        decrypt(p,key);
        p+=2;
    }
    for(i = 0;i<240;i++)
    {
        if(cipher[i]!=0)
            printf("%c",cipher[i]+2);
    }
    printf("\n");
}
```

# Mobile

## mblockchain

jadx打开后看java代码。

需要输入key和flag。key算一次md5后，取其中的三个字符再md5，md5值作为aes的key加密flag，之后重复md5之前的哈希作为key继续加密9次，一共十次。爆破这三个字符即可。

```python
from Crypto.Cipher import AES
from hashlib import md5
foundpad = "\x10"*16

cipher = "74f0b165db8a628716b53a9d4f6405980db2f833afa1ed5eeb4304c5220bdc0b541f857a7348074b2a7775d691e71b490402621e8a53bad4cf7ad4fcc15f20a8066e087fc1b2ffb21c27463b5737e34738a6244e1630d8fa1bf4f38b7e71d707425c8225f240f4bd2b03d6c2471e900b75154eb6f9dfbdf5a4eca9de5163f9b3ee82959f166924e8ad5f1d744c51416a1db89638bb4d1411aa1b1307d88c1fb5".decode("hex")
"""
cipherpad = cipher[-16:]
for i in range(240,256):
    print(i)
    for j in range(256):
        for k in range(256):
            key = chr(i) + chr(j) + chr(k)
            ck = key
            for _ in range(10):
                ck = md5(ck).digest()
            aes = AES.new(ck,mode = AES.MODE_ECB)
            cp = aes.decrypt(cipherpad)
            if cp == foundpad:
                print(cp.encode("hex"))
                print(ck.encode("hex"))
                print(i,j,k)
                exit()
"""
key = chr(241) + chr(183) + chr(36)
subkey = []
ck = key
for i  in range(10):
    subkey.append(md5(ck).digest())
    ck = md5(ck).digest()
for i in range(10):
    ck = subkey[9-i]
    aes = AES.new(ck)
    cipher = aes.decrypt(cipher)
print(cipher)
```



