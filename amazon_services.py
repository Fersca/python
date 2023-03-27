import boto3
from aws_keys import aws

session = boto3.Session(
        region_name=aws['region_name'],
        aws_access_key_id=aws['aws_access_key_id'],
        aws_secret_access_key=aws['aws_secret_access_key']
    )

services = session.get_available_services()

print(services)