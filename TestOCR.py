from __future__ import print_function
from wand.image import Image
from PyPDF2 import PdfFileReader
import os
import boto3

s3 = boto3.client('s3')
basepath = os.path.dirname(os.path.abspath('TestOCR.py'))
bucket_name = 'zayyer'


# saves an image as a png into the ConvertedImages folder
def pdf_to_png(filepath, save_name):

    file_save = basepath+"\ConvertedImages"

    with Image(filename=filepath, resolution=200) as image:
        image.compression_quality = 99
        image.save(filename=file_save + "\\" + save_name)



#goes through all of the png's in the convertedimages folder, and uploads the file to the s3 bucket
def upload_pngs():

    png_names = os.listdir(basepath + '\convertedimages')
    counter = 0

    for x in png_names:
        png_path = basepath +  "\convertedimages" + "\\" + x
        s3.upload_file(png_path, bucket_name, "pictures//" + png_names[counter])
        #detect_text(png_names[counter])
        counter+=1

#gets the list of file names in the unconverted pdf folder, and calls pdf_to_png for each item
def folder_to_png(folderpath):

    file_names = os.listdir(basepath+ '\PDFs')

    for x in  file_names:
        filePath = basepath + "\PDFs\\" + x
        saveName = x.split(".")[0]   +  ".png"
        pdf_to_png(filePath,saveName)


def get_num_pages(filepath):
    calc_page_sum = 0;
    calc_page_sum += PdfFileReader(filepath, 'rb').getNumPages()
    print(calc_page_sum)


def detect_text(image_name):
    if __name__ == "__main__":
     bucket='zayyer'
     photo= image_name
     client=boto3.client('rekognition')

     response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

     textDetections=response['TextDetections']
     print(response)
     print('Matching faces')

     for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
     if 'ParentId' in text:
        print ('Parent Id: {}'.format(text['ParentId']))
        print ('Type:' + text['Type'])



folder_to_png("E:\Documents\Git\PDF2EXCEL\PDFs")
upload_pngs()
detect_text("3.PNG")


#get_num_pages("E:\Documents\Git\PDF2EXCEL\PDFs\CenturyLink.pdf")
#print(os.listdir('E:\Documents\Git\PDF2EXCEL\PDFs'))

