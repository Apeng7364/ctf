a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
b = [0 for i in range(16)]
for i in range(16):
    b[i] = a[15-i]
c = [0 for i in range(16)]
c[0] = b[0]
for i in range(1,16):
    c[i] = b[i] - b[0]
print(c)