import boto3
s3 = boto3.resource('s3')
source= { 'Bucket' : 'zayyer', 'pictures': 'Bucket'}
dest = s3.Bucket('zayyer-pictures')
dest.copy(source, 'backupfile')