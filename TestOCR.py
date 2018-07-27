from __future__ import print_function
from wand.image import Image
from PyPDF2 import PdfFileReader
import os

basepath = os.path.dirname(os.path.abspath('TestOCR.py'))
def pdf_to_png(filepath, save_name):

    #saves an image as a png into the ConvertedImages folder
    fileSave = basepath+"\ConvertedImages"
    with Image(filename=filepath, resolution=200) as image:
        image.compression_quality = 99
        image.save(filename=fileSave + "\\" + save_name)

def folder_to_png(folderpath):
    #gets the list of file names in the unconverted pdf folder, and calls pdf_to_png for each item
    file_names = os.listdir(basepath+ '\PDFs')

    for x in  file_names:
        filePath = basepath + "\PDFs\\" + x
        saveName = x.split(".")[0] + ".png"
        pdf_to_png(filePath,saveName)

def get_num_pages(filepath):
    calc_page_sum = 0;
    calc_page_sum += PdfFileReader(filepath, 'rb').getNumPages()
    print(calc_page_sum)

folder_to_png("E:\Documents\Git\PDF2EXCEL\PDFs")

#get_num_pages("E:\Documents\Git\PDF2EXCEL\PDFs\CenturyLink.pdf")
#print(os.listdir('E:\Documents\Git\PDF2EXCEL\PDFs'))
