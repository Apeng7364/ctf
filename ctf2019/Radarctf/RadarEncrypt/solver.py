a = [4,11,14,11,4,0,8,26,14,3,22,13,9,15,13,27,11,19,3,13,12,27,11,20,20,13,23,4,6,10,5,9,4,28]
table = '{qwertyuiopas_dfghjklzxcvbnm}'
s = ''
print(len(table))
for i in range(len(a)):
	s+=table[a[i]]
	print(s)
print(s)