from hashlib import *
s='aaaaaa'
for a in 'opqrstuvwxyz':
    for b in 'abcdefghijklmnopqrstuvwxyz':
        for c in 'abcdefghijklmnopqrstuvwxyz':
            for d in 'abcdefghijklmnopqrstuvwxyz':
                for e in 'abcdefghijklmnopqrstuvwxyz':
                    for f in 'abcdefghijklmnopqrstuvwxyz':
                        s=a+b+c+d+e+f
                        smd5=md5(s.encode('ascii')).hexdigest()
                        count=0
                        for i in range(32):
                            if(smd5[i]=='0'):
                                count+=10
                                count+=i
                        if count==403:
                            print(s)
                            exit(0)
        print(s)
s='ozulmt'
print('flag{a197b847-7092-53a4-7c41-bc7d6d52e69d}')
# ozulmt
# flag{________-____-____-____-____________}
# flag{abcdefgh-ijkl-mnop-qrst-uvwxyzabcdef}
# flag{a197b847-7092-53a4-7c41-bc7d6d52e69d}
