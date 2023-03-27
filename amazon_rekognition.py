import boto3
import platform
import requests
import json
from io import BytesIO
from PIL import Image
from aws_keys import aws

#test the platform import
print(platform.system())
print(platform.release())
print(platform.version())
print()

# create a session with the specified credentials
session = boto3.Session(
    aws_access_key_id=aws['aws_access_key_id'],
    aws_secret_access_key=aws['aws_secret_access_key']
)

# create a Rekognition client with the specified region and credentials
client = boto3.client(
    'rekognition',
    region_name=aws['region_name'],
    aws_access_key_id=aws['aws_access_key_id'],
    aws_secret_access_key=aws['aws_secret_access_key']
)

# specify image to analyze from URL
image_url = 'https://daily.jstor.org/wp-content/uploads/2022/12/public_pawlicy_dog_breeding_from_pedigree_to_bans_1050x700.jpg'

# Download the image using the requests library
response = requests.get(image_url)

# Get the image content in bytes format
image_bytes = response.content

# Call the detect_labels API to detect labels in the image
response = client.detect_labels(
    Image={
        'Bytes': image_bytes
    },
    MaxLabels=10,
    MinConfidence=70
)

#print the json response
# Use json.dumps() to pretty print the JSON object
pretty_json = json.dumps(response, indent=4)
# Print the pretty-printed JSON object
print(pretty_json)
print("------------------")

# print detected labels
print('Detected labels:')
for label in response['Labels']:
    print(label['Name'], label['Confidence'])

# Show the image on the screen
image = Image.open(BytesIO(image_bytes))
image.show()