import boto3

if __name__ == "main":

    bucket='zayyer'
    photo='3.PNG'

    client=boto3.client('rekognition')


    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})


    textDetections=response['TextDetections']
    print (response)
    print ('Matching faces')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print()


