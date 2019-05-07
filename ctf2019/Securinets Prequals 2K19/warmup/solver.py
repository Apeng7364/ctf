table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
k = [0 for i in range(36)]
k[0] = table[28]
k[1] = table[54]
k[2] = k[10] = table[((28+54)>>2) + 1]
k[3] = 'j'
k[4] = chr(ord(k[0])+1)
k[12] = k[22] = k[24] = chr(ord(k[4])-1)
k[23] = k[11] = chr(48)
k[35] = chr(ord(k[11])+9)
k[6] = chr(ord(k[3]) - 32)
k[8] = chr(ord(k[0]) - 1)
k[27] = k[31] = chr(ord(k[4]) + 2)
k[25] = k[9] = chr(ord(k[27]) + 7)
k[13] = k[17] = k[21] = chr(ord(k[1]) + 1)
k[7] = 'p'
k[15] = chr(ord(k[7]) + 3)
k[14] = chr(ord(k[15]) + 1)
k[19] = 'z'
k[34] = chr(ord(k[0]) - 33)
k[5] = k[20] = k[29] = k[33] = 'X'
k[26] = chr(49)
k[16] = k[28] = chr(ord(k[9]) - 32)
k[1] = chr(50)
k[18] = k[30] = chr(ord(k[7]) - 30)
k[32] = k[4]
t = ''
for i in range(36):
    t+=k[i]

print(t.decode('base64'))


