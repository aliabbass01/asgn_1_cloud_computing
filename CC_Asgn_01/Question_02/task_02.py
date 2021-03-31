# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 15:24:33 2021

@author: ALI
"""

import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'bucketali'

data = open('img104.jpg', 'rb')

s2 = boto3.resources(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=aws_secret_access_key,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(key='img104.jpg', Body=data, ContentType='image/jpg')

print("Done")