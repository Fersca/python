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
        return raw_text

    else:
        print(f'Transcription job {job_name} has not completed yet')
        return ""

def create_comprehend_client():
    comprehend = boto3.client(
        'comprehend',
        region_name=aws['region_name'],
        aws_access_key_id=aws['aws_access_key_id'],
        aws_secret_access_key=aws['aws_secret_access_key']
    )
    return comprehend


def sentiment_analysis(comprehend, text_to_analyse):

    if text_to_analyse == "":
        return

    # Call the Sentiment API to analyze the text
    response = comprehend.detect_sentiment(Text=text_to_analyse, LanguageCode='es')

    # Extract the sentiment score and label from the response
    sentiment_score = response['SentimentScore']
    sentiment_label = response['Sentiment']

    # Print the results
    print("")
    print("Sentiment score: {}".format(sentiment_score))
    print("Sentiment label: {}".format(sentiment_label))

def detect_entities(comprehend, text_to_analyse):
    # Call the DetectEntities API
    response = comprehend.detect_entities(
        Text=text_to_analyse,
        LanguageCode='es'
    )

    print()
    # Print the identified entities
    sorted_response = sorted(response['Entities'], key=lambda x: x['Score'], reverse=True)
    for entity in sorted_response:
        print('Score:', int(round(entity['Score'], 2)*100),'%','Entity:', entity['Text'])



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
    text_to_analyse = process_job()

    print("")
    user_input = input("Perform Sentimental Analysis? (y/n): ")
    if user_input== "y":
        # Initialize Amazon Comprehend client
        comprehend = create_comprehend_client()
        sentiment_analysis(comprehend, text_to_analyse)
        detect_entities(comprehend, text_to_analyse)




