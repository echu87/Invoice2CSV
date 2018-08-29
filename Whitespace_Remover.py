from PIL import Image
import os
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))

def find_rows_with_color(pixels, width, height, colour):
    rows_found=[]
    verify_rows = []
    #go through the entire picture row by row, if the row only has white pixels, append the row to rows_found array, then return the rows.

    count = 0
    for y in range(height):
        for x in range(width):
            if pixels[x, y] != colour:
                count=0
                verify_rows.clear()
                break
        else:
            if(count>=100):
                for i in verify_rows:
                    rows_found.append(i)
                verify_rows.clear()
                count = 0
            else:
                verify_rows.append(y)
                count+=1

    return rows_found

#goes through the entire convertedimages folder, and doubles the size of each image
def resize_image():
    png_names = os.listdir(basepath + '\convertedimages')
    # go through each file in the converted images path, and create a image object for each.
    for x in png_names:
        png_path = basepath + "\convertedimages" + "\\" + x

        old_im = Image.open(png_path)
        if old_im.mode != 'RGB':
            old_im = old_im.convert('RGB')
        width, height = old_im.size[0], old_im.size[1]

        old_im = old_im.resize([width*2, height*2])
        old_im.save(png_path)



def remove_whitespace():

    png_names = os.listdir(basepath + '\convertedimages')
    #go through each file in the converted images path, and create a image object for each.
    for x in png_names:
        png_path = basepath + "\convertedimages" + "\\" + x

        old_im = Image.open(png_path)
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

        new_im.save(png_path)
    resize_image()




# if __name__ == '__main__':
#     png_path = basepath + "\convertedimages" + "\\" + "Frontier-0.png"
#     old_im = Image.open(png_path)
#     pixels = old_im.load()


remove_whitespace()
