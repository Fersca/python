import boto3
import requests
import json
import urllib.request
import os
from aws_keys import aws

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Call the start_transcription_job API to transcribe the audio
def transcribe_audio():
    print("Sending transcription job")
    job_uri = f's3://{bucket_name}/{file_name}'
    response = transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='mp3',
        LanguageCode='es-ES'
    )
    print("Job sent")

#detete the transcription job
def delete_transcription_job():
    print("deleting previous job")
    response = transcribe.delete_transcription_job(TranscriptionJobName=job_name)

# Initialize the Transcribe client
def create_transcribe_client():
    transcribe = boto3.client(
        'transcribe',
        region_name=aws['region_name'],
        aws_access_key_id=aws['aws_access_key_id'],
        aws_secret_access_key=aws['aws_secret_access_key']
    )
    return transcribe

def uploadFile():

    # Ask for input
    audio_url = input("Enter the audio URL: ")
    if audio_url == "":
        # Define the audio URL
        audio_url = 'https://audio-lingua.ac-versailles.fr/IMG/mp3/el_asado_argentino.mp3'
        print("Using default URL: ", audio_url)

    # Download the audio file using the requests library
    print("Downloading Audio...")
    response = requests.get(audio_url)
    print("Audio Downloaded, updating S3")

    # Upload the audio file to S3
    # Initialize the Transcribe client
    s3 = boto3.resource('s3',
        region_name=aws['region_name'],
        aws_access_key_id=aws['aws_access_key_id'],
        aws_secret_access_key=aws['aws_secret_access_key']
        )

    s3.Bucket(bucket_name).put_object(Key=file_name, Body=response.content)
    print("S3 updated")

def process_job():
    response = transcribe.list_transcription_jobs()
    jobs = response['TranscriptionJobSummaries']

    for job in jobs:
        print("Getting job: ", job['TranscriptionJobName'])

    response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    job_status = response['TranscriptionJob']['TranscriptionJobStatus']

    if job_status == 'COMPLETED':
        transcript_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        transcript_file = urllib.request.urlopen(transcript_uri)
        transcript_text = transcript_file.read().decode('utf-8')

        with open('output.txt', 'w') as file:
            file.write(transcript_text)
        print("Text save to file: ", 'output.txt')

        json_data = json.loads(transcript_text)
        raw_text = json_data['results']['transcripts'][0]['transcript']
        print("------------------------------")
        print(raw_text)

    else:
        print(f'Transcription job {job_name} has not completed yet')

# Define the S3 bucket and key names
bucket_name = 'my-transcribe-bucket2'
file_name = 'my-audio.mp3'
job_name = 'MyTranscriptionJob'

transcribe = create_transcribe_client()

user_input = input("Upload a new audio file? (y/n): ")

if user_input== "y":
    uploadFile()
    delete_transcription_job()
    transcribe_audio()
else: 
    process_job()




