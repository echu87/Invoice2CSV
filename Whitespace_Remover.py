from PIL import Image, ImageOps
import os
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))



def find_rows_with_color(pixels, width, height, white):
    rows_found=[]
    for y in range(height):
        for x in range(width):
            if pixels[x, y] != white:
                break
        else:
            rows_found.append(y)

    return rows_found

old_im = Image.open(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png")
if old_im.mode != 'RGB':
    old_im = old_im.convert('RGB')

pixels = old_im.load()
width, height = old_im.size[0], old_im.size[1]
rows_to_remove = find_rows_with_color(pixels, width, height, (255, 255, 255))
new_im = Image.new('RGB', (width, height - len(rows_to_remove)))
pixels_new = new_im.load()
rows_removed = 0

for y in range(old_im.size[1]):
    if y not in rows_to_remove:
        for x in range(new_im.size[0]):
            pixels_new[x, y - rows_removed] = pixels[x, y]
    else:
        rows_removed += 1
new_im.save(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png")


# OLD STUFF
# im = Image.open(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png", 'r')
# width, height = im.size
# pixel_values = list(im.getdata())
# pix = im.load()
#
# white_row = 0
# white_pixel = 0
# count = 0
#
# old_im = Image.open(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png")
# if old_im.mode != 'RGB':
#     old_im = old_im.convert('RGB')
#
# rows_to_remove = []
#
# #iterate over all the pixels in the picture, if the white count of a row is greater or equal to the width (the entire row is white), add the y value (row), to the rows_to_be_removed list.
# for y in range (height):
#     if count>=100:
#         print(count)
#         pixels = old_im.load()
#         new_im = Image.new('RGB', (width, height - 100))
#         pixels_new = new_im.load()
#
#         pixels_new[x, y - 100] = pixels[x, y]
#         #transformed = im.transform(im.size, Image.EXTENT,(0,0, width, y-100))
#         #transformed.save('Frontier-0-cropped.png')
#         count = 0
#
#     for x in range(width):
#         if white_pixel >=width:
#             white_pixel = 0
#             count+=1
#             rows_to_remove.append(y)
#
#         elif pix[x,y] == 0:
#             white_pixel +=1
#         else:
#             count = 0



# how to crop an image
# image = Image.open('unsplash_01.jpg')
# box = (150, 200, 600, 600)
# cropped_image = image.crop(box)
# cropped_image.save('cropped_image.jpg')
#
# if white_pixel exceeds width, increase white row. If white row exceeds 100, delete the 100 rows.