from pwn import *
context.log_level = 'error'
p = remote('34.92.37.22','10001')
dic ={' ':'0001', '-':'00100100', ',':'0010001', '.':'00100101', ';':'001001111', 'I':'00101011', 'L':'00101100001', 'a':'0011', 'c':'010001', 'b':'010000', 'e':'0101', 'd':'01001', 'g':'01101', 'f':'01100', 'i':'1000', 'h':'0111', 'k':'1001001', 'm':'10011', 'l':'100101', 'o':'10110', 'n':'1010', 'q':'11000', 'p':'10111', 's':'1101', 'r':'11001', 'u':'111100', 't':'1110', 'w':'1111100', 'v':'111101', 'y':'1111110'}
plain = 'If you cannot read all your books...fondle them---peer into them, let them fall open where they will, read from the first sentence that arrests the eye, set them back on the shelves with your own hands, arrange them on your own plan so that you at least know where they are. Let them be your friends; let them, at any rate, be your acquaintances.'
cipher = ''
for i in range(len(plain)):
    cipher+=dic[plain[i]]
s = ''
cipher+='111111100010'
# print(cipher)

for i in range(0,len(cipher),8):
    temp = eval('0b'+cipher[i:i+8])
    if temp>=0x80:
        res = '000'+bin(temp)[2:]
        res = '110'+res[0:5]+'10'+res[5:]
        a = res[0:8]
        b = res[8:]
        s+=chr(eval('0b'+a))
        s+=chr(eval('0b'+b))
    else:
        s+=chr(temp)

# p = process('fanoGo')
p.recv()
p.recv()
p.send(s)
try:
    print(p.recv())
except EOFError:
    p.close()
        
