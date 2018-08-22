from PIL import Image
import os
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))

im = Image.open(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png", 'r')
width, height = im.size
pixel_values = list(im.getdata())
pix = im.load()
count = 0
for x in range (width):
    for y in range(height):
        count +=1
        print(pix[x,y])
print (count)

