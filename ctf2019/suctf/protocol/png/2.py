f = open("1.txt")
g = open("2.txt","w")
for line in f:
    g.write(line[0:7]+"\n")