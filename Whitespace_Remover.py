from PIL import Image
import os
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))

im = Image.open(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png", 'r')
width, height = im.size
pixel_values = list(im.getdata())
pix = im.load()

white_row = 0
white_pixel = 0
rows_to_be_removed = []

#iterate over all the pixels in the picture, if the white count of a row is greater or equal to the width (the entire row is white), add the y value (row), to the rows_to_be_removed list.
for y in range (height):
    for x in range(width):
        if white_pixel >=width:
            rows_to_be_removed.append(y)
            white_pixel = 0
        elif pix[x,y] == 0:
            white_pixel +=1

print (rows_to_be_removed)




#if white_pixel exceeds width, increase white row. If white row exceeds 100, delete the 100 rows.