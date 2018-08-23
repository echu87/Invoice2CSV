from __future__ import print_function
from wand.image import Image
from Whitespace_Remover import remove_whitespace
import os
import boto3
import time


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
        s3.upload_file(png_path, bucket_name,  png_names[counter])
        time.sleep(2)
        counter+=1

#gets the list of file names in the unconverted pdf folder, and calls pdf_to_png for each item
def folder_to_png(folderpath):

    file_names = os.listdir(basepath+ '\PDFs')

    for x in  file_names:
        filePath = basepath + "\PDFs\\" + x
        saveName = x.split(".")[0]   +  ".png"
        pdf_to_png(filePath,saveName)


def folder_detect_text():
    png_names = os.listdir(basepath + '\convertedimages')
    for x in png_names:
        detect_text(x)



def detect_text(image_name):
    if __name__ == "__main__":

     photo= image_name

     client=boto3.client('rekognition')

     response=client.detect_text(Image={'S3Object':{'Bucket':bucket_name,'Name':photo}})

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

#taken from https://alexwlchan.net/2017/07/listing-s3-keys/
def delete_all_s3_keys(bucket):

    """Get a list of all keys in an S3 bucket."""
    keys = []

    kwargs = {'Bucket': bucket_name}
    while True:
        resp = s3.list_objects_v2(**kwargs)
        for obj in resp['Contents']:
            keys.append(obj['Key'])

        try:
            kwargs['ContinuationToken'] = resp['NextContinuationToken']
        except KeyError:
            break

    print(keys)
    for x in keys:
        s3.delete_object(Bucket=bucket_name, Key=x)


folder_to_png("E:\Documents\Git\PDF2EXCEL\PDFs")

#upload_pngs()
#delete_all_s3_keys(bucket_name)

#detect_text("Frontier-0.png")

#folder_detect_text()



