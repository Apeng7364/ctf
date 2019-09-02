from PIL import Image
img = Image.open("./1.bmp")
pix = img.load()
for x in range(540):
    t = 0
    for y in range(371):
        if pix[x,y] == (0,0,0):
            t+=1
    print(t)