from Crypto.Cipher import AES

def strxor(s1,s2):
    s = ''
    for i in range(len(s1)):
        s+=chr(ord(s1[i])^ord(s2[i]))
    return s

key = '2B7E151628AED2A6ABF7158809CF4F3C'.decode('hex')
aes = AES.new(key)
cipher = ['AE4614F82A40CF5031D3FE048C061212'.decode('hex'),
'23FAC726E861D9C3A93C45701AC7F03D'.decode('hex'),
'DFBEBC16AB6E37AC148B9C94F75D6278'.decode('hex'),
'FC16981DB231D35ADC3A60869ACA7BA3'.decode('hex'),
'B5D5F1B2D9FFD209D477D73DC0561902'.decode('hex'),
'B69B426CE8A277E399AC324091A92A86'.decode('hex'),
'F3FA473CC35C419BE80507D0D4305A9E'.decode('hex'),
'8D529BA3FBADB6443F72839C2277FE48'.decode('hex'),
'FE868412004EEDFFAC441923841F12CA'.decode('hex')]
dic = {'\x82':'a', '\x05':'b', '\x86':'c', '\x8A':'d', '\x0B':'e', '\x11':'f', '\x96':'g', '\x1D':'h', '\x27':'i', '\xA9':'j', '\x2B':'k', '\xB1':'l', '\xF3':'m', '\x5E':'n', '\x37':'o', '\x38':'p', '\xC2':'q', '\x47':'r', '\x4E':'s', '\x4F':'t', '\xD6':'u', '\x58':'v', '\xDE':'w', '\xE2':'x', '\xE5':'y', '\xE6':'z', '\x67':'0', '\x6B':'1', '\xEC':'2', '\xED':'3', '\x6F':'4', '\xF2':'5', '\x73':'6', '\xF5':'7', '\x77':'8', '\x7F': '9'}
flag = ''
xor = '00'*16
xor = xor.decode('hex')
for i in range(len(cipher)):
    temp = cipher[i]
    plain = aes.decrypt(temp)
    plainp = strxor(plain,xor)
    xor = cipher[i]
    for j in plainp:
        try:
            flag+=dic[j]
        except KeyError:
            flag+='_'
            break
flag = '*CTF{'+flag[:-1]+'}'
print(flag)