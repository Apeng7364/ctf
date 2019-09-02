from math import *

def bin1(a):
    s = bin(a)
    s = s[2:]
    num = 0
    for i in s:
        if i == '1':
            num+=1
    return num%2

def get_result(a):
    mi = a*a
    ma = (a+1)*(a+1)
    for i in range(mi,ma):
        if(bin1(i)):
            return i

def is_prime(a):
    if a == 0:
        return 0
    if a == 1:
        return 0
    if a == 2:
        return 1
    for i in range(2,(a/2)+1):
        if a%i == 0:
            return 0
    return 1
res = [963,4396,6666,1999,3141]
flag = ""
for i in res:
    flag+=str(get_result(i))
    flag+='-'
s = 0
for i in range(1,10001):
    if is_prime(i):
        s+=1
flag+=str(s)
print(flag)