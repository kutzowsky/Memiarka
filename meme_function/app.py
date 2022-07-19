import os
import json
import uuid

import boto3

from PinguMeme import PinguMeme


INPUT_BUCKET = os.environ['INPUT_BUCKET']
OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

PINGU_TEMPLATE = 'angry_pingu.png'
FONT = 'impact.ttf'

s3 = boto3.client('s3')
template_path = f'/tmp/{PINGU_TEMPLATE}'
font_path = f'/tmp/{FONT}'

s3.download_file(INPUT_BUCKET, PINGU_TEMPLATE, template_path)
s3.download_file(INPUT_BUCKET, FONT, font_path)

pingu_meme = PinguMeme('/tmp/')

def lambda_handler(event, context):
    first_line = event['queryStringParameters']['firstLine']
    second_line = event['queryStringParameters']['secondLine']

    print('First line: ', first_line)
    print('Second line: ', second_line)

    output_file_name = f'{uuid.uuid4()}.png'
    output_file_path = f'/tmp/{output_file_name}'
    s3_file_name = f'https://{OUTPUT_BUCKET}.s3.amazonaws.com/{output_file_name}'

    pingu_meme.set_text(first_line, second_line)

    pingu_meme.save(output_file_path)

    print('Meme file created')

    s3.upload_file(output_file_path, OUTPUT_BUCKET, output_file_name)

    print('Uploaded to S3', s3_file_name)

    os.remove(output_file_path)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        'body': json.dumps({
            'memeUrl': s3_file_name,
        }),
    }
