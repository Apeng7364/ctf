f = open("trace3data.txt")
g = open("1.txt",'w')
for line in f:
    if line[24:26]=='89':
        g.write(line)