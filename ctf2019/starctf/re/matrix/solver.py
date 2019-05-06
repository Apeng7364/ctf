from itertools import *
a = [i for i in range(54)]
mat = [0x0FDFE0BA1, 0x9A915052, 0x0C96F3527, 0x0F5201FCD, 0x0FE32ED8F, 0x0DB8E3EF9, 0x51EF954, 0x0FE217F1C, 0x7B33A8BB, 0x9CF903A1, 0x0C381E2CD, 0x22B35BE4, 0x4550E6AE, 0x0DC9E8F3C, 0x0A9B44EAF, 0x3372486A, 0x51329F58, 0x5F2F456E, 0x9B555A08, 0x0EB1A8529, 0x9B009084, 0x9B0B7B06, 0x9967F311, 0x91FB13AB, 0x18952236, 0x6F7B9915, 0x0EDD9D6D1, 0x0FB67FE21, 0x259911B0, 0x3DC4EE74, 0x98936FF0, 0x0DF7502CE, 0x0C3DF1016, 0x0BC1220F9, 0x0F54C810C, 0x715A634C, 0x3E1637A6, 0x80F07B8D, 0x0FB9CA491, 0x0AD254C2E, 0x0FB5A012F, 0x1AEF5581, 0x0B9CC1351, 0x9A3B536D, 0x0BD7FAF0F, 0x0F49AD883, 0x2C55324, 0x83BC3205, 0x43846281, 0x19382448, 0x0FADB2B18, 0x9335D185, 0x94C6BF5A, 0x591685AE]
m = combinations(a,5)

a= [[[0xfdfe0ba1, 0x7b33a8bb, 0x3dc4ee74, 0x3e1637a6],[0x51329f58, 0x6f7b9915, 0x2c55324, 0x43846281],0xdf7502ce],[[0xc96f3527, 0x51ef954, 0x715a634c, 0x9335d185], [0xf5201fcd, 0xdb8e3ef9, 0xeb1a8529, 0x9a3b536d],0x9967f311],[[0x9b009084, 0x18952236, 0xbd7faf0f, 0x83bc3205], [0xc381e2cd, 0x98936ff0, 0xc3df1016, 0x94c6bf5a], 0xdc9e8f3c],[[0x22b35be4, 0x3372486a, 0xedd9d6d1, 0xfb9ca491], [0x91fb13ab, 0x80f07b8d, 0xad254c2e, 0x1aef5581], 0xfe32ed8f],[[0x9cf903a1, 0x9b555a08, 0xb9cc1351, 0x591685ae], [0xfe217f1c, 0xa9b44eaf, 0x259911b0, 0xf54c810c], 0x19382448],[[0x5f2f456e, 0xfb67fe21, 0xbc1220f9, 0xf49ad883], [0x9a915052, 0x4550e6ae, 0x9b0b7b06, 0xfadb2b18], 0xfb5a012f]]
constmat = [0x0B849CD19, 0x55E00017, 0x844966B, 0x80C181EC, 0x686C0B3C, 0x55400592, 0x0CD42168A, 0x4039E81, 0x0D9DE549F, 0x2034677D, 0x144ABD, 0x49100D00, 0x0E003A0E0, 0x80F0006D, 0x8307ADD6, 0x4CF60781, 0x0A0352643, 0x0C580C3DE, 0x0EA8C4E24, 0x68603008, 0x687FBFFF, 0x19DE4BF9, 0x271A1179, 0x99791C4D, 0x29CBFFC, 0x2B82801E, 0x3C0307FB, 0x0DAE61CD6, 0x8F7B1BF0, 0x0C56CEF1D, 0x0D6493A96, 0x1808018, 0x0F48001B9, 0x3712519, 0x9294F318, 0x6DE20384, 0x0F3750B04, 0x256A122A, 0x257290B, 0x0C4582056, 0x204E8BC0, 0x79C7ADE7, 0x0C4C20203, 0x5B961570, 0x66034856, 0x78329E3A, 0x1D07C00, 0x4AC240E6, 0x854CFBBE, 0x0ABFEC404, 0x5BD80037, 0x0E94CBCD8, 0x1, 0x0C4CA280D]
'''
# get part of result
for i in m:
    summ = 0
    for j in i:
        summ+=mat[j]
    summ&=0xffffffff
    for k in range(len(res)):
        if summ == res[k][0]:
            print(k,0)
            for j in i:
                print(hex(mat[j]))
            print('')
        
        if summ == res[k][1]:
            print(k,1)
            for j in i:
                print(hex(mat[j]))
            print('')
# then combine these output in Notepad++, get the res
exit()
'''
res = [[0x0D481DD44, 0x0E66CF0E0], [0x6C86565D, 0x0EF6C2A6D], [0x0D170230A, 0x9159B169], [0x3DCF0D3F, 0x0D9331E76], [0x64691AF0, 0x0DBF384CF], [0x69E3E3A, 0x7122DE4D]]
m = permutations([0,1,2,3],4)
n = []
for i in m:
    n.append(i)
cont = 0


for i in range(0,6):
    print('')
    print('#########part %d#########'%i)
    for p in n:
        for q in n:
            cont+=1
            ress = ''
            resr = []
            resr.append(a[i][0][p[0]])
            resr.append(a[i][1][q[0]])
            resr.append(a[i][0][p[1]])
            resr.append(a[i][1][q[1]])
            resr.append(a[i][2])
            resr.append(a[i][1][q[2]])
            resr.append(a[i][0][p[2]])
            resr.append(a[i][1][q[3]])
            resr.append(a[i][0][p[3]])
            sumr = 0
            check0 = resr[0]+resr[2]+resr[4]+resr[6]+resr[8]
            check0&=0xffffffff
            check1 = resr[1]+resr[3]+resr[4]+resr[5]+resr[7]
            check1&=0xffffffff
            if  check0 != res[i][0]:
                print(i)
                for k in resr:
                    print(hex(k))
                print('')
                print(hex(check0))
                print(hex(res[i][0]))
                print(p)
                print(q)
                exit()
            assert check0 == res[i][0]
            assert check1 == res[i][1]
            for k in range(len(resr)):
                sumr+=resr[k]*constmat[i*9+k]
                sumr&=0xFFFFFFFF
            ff = 0
            for _ in range(4):
                temp = sumr&0xFF
                if temp < 0x20 or temp >= 0x7f:
                    ff = 1
                    break
                ress+=chr(temp)
                sumr>>=8
            if ff == 1:
                continue
            print(ress)