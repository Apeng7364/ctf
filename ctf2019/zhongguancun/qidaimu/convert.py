from PIL import Image
import os
gifFileName = 'qidaimu.gif'
im = Image.open(gifFileName)
pngDir = gifFileName[:-4]
os.mkdir(pngDir)
try:
    while True:
        current = im.tell()
        im.save(pngDir+'\\'+str(current)+'.png')
        im.seek(current+1)
except EOFError:
    pass