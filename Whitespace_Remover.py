from PIL import Image, ImageOps
import os
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))



def find_rows_with_color(pixels, width, height, white):
    rows_found=[]
    #go through the entire picture row by row, if the row only has white pixels, append the row to rows_found array, then return the rows.
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

#create a new blank image with the height - the amount of rows that have to be removed
pixels = old_im.load()
width, height = old_im.size[0], old_im.size[1]
rows_to_remove = find_rows_with_color(pixels, width, height, (255, 255, 255))
new_im = Image.new('RGB', (width, height - len(rows_to_remove)))
pixels_new = new_im.load()
rows_removed = 0

#go through the new blank image, and add the rows that are not only white (if y not in rows_to_remove)
for y in range(old_im.size[1]):
    if y not in rows_to_remove:
        for x in range(new_im.size[0]):
            pixels_new[x, y - rows_removed] = pixels[x, y]
    else:
        rows_removed += 1

new_im.save(basepath + "\\" + "ConvertedImages\\" + "Frontier-0.png")

