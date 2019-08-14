import csv
import boto3


with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]


photo = 'report1.jpg'

client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name="ap-south-1")


response = client.detect_text(
    Image={
        'S3Object': {
            'Bucket': 'lalith-babu',
            'Name': 'report1.jpg'
        }
    }
)
textDetections = response['TextDetections']
print('Detected text')
for text in textDetections:
    print(text['DetectedText'])
   # print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
   # print('Id: {}'.format(text['Id']))
   # if 'ParentId' in text:
   #     print('Parent Id: {}'.format(text['ParentId']))
   # print('Type:' + text['Type'])

