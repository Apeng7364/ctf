from Crypto.Util.number import inverse
p = 282164587459512124844245113950593348271
q = 366669102002966856876605669837014229419
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = inverse(e,phi)
c = 0xad939ff59f6e70bcbfad406f2494993757eee98b91bc244184a377520d06fc35
m = pow(c,d,n)
print(hex(m)[2:-1].decode("hex"))