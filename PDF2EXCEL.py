from __future__ import print_function
from wand.image import Image
#from Whitespace_Remover import remove_whitespace
import os
import boto3
import time


s3 = boto3.client('s3')
basepath = os.path.dirname(os.path.abspath('PDF2EXCEL.py'))
bucket_name = 'zayyer'


# saves an image as a png into the ConvertedImages folder
def pdf_to_png(filepath, save_name):

    file_save = basepath+"\ConvertedImages"
    #make a new individual folder for each pdf
    if not os.path.exists(file_save +"\\"+ filepath):
        indi_folder = file_save +"\\"+ save_name.split(".")[0]
        os.makedirs(indi_folder)

    with Image(filename=filepath, resolution=200) as image:
        image.compression_quality = 99
        image.save(filename=indi_folder + "\\" + save_name)


#gets the list of file names in the unconverted pdf folder, and calls pdf_to_png for each item
def folder_to_png():

    file_names = os.listdir(basepath+ '\PDFs')

    for x in  file_names:
        filePath = basepath + "\PDFs\\" + x
        saveName = x.split(".")[0]   +  ".png"
        pdf_to_png(filePath,saveName)

#goes through all of the png's in the convertedimages folder, and uploads the file to the s3 bucket
def upload_pngs():

    png_names = os.listdir(basepath + '\convertedimages')
    counter = 0

    for x in png_names:
        png_path = basepath +  "\convertedimages" + "\\" + x
        s3.upload_file(png_path, bucket_name,  png_names[counter])
        time.sleep(2)
        counter+=1


def folder_detect_text():
    png_names = os.listdir(basepath + '\convertedimages')
    for x in png_names:
        detect_text(x)


#takes a png from s3 bucket, and detects text using amazon rekognition, then it writes the json response to a text file with the name of the png.
def detect_text(image_name):
    if __name__ == "__main__":

     client=boto3.client('rekognition')
     file = open(basepath + "\convertedimages\\" + image_name.split("/")[0]+ ".txt", "w")

     response=client.detect_text(Image={'S3Object':{'Bucket':bucket_name,'Name':image_name}})

     textDetections=response['TextDetections']
     file.write(str(response))
     file.write('Matching faces')

     for text in textDetections:
        file.write('Detected text:' + text['DetectedText'])
        file.write('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        file.write('Id: {}'.format(text['Id']))
     if 'ParentId' in text:
        file.write ('Parent Id: {}'.format(text['ParentId']))
        file.write('Type:' + text['Type'])

     file.close()
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

#pdf_to_png("ds.pdf",'ds.png')
#folder_to_png()
#remove_whitespace()
upload_pngs()
#delete_all_s3_keys(bucket_name)
#detect_text("ds-0.png")
#folder_detect_text()



