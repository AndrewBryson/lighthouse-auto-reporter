#!/usr/bin/python

import boto3

filename = "results.report"
htmlFile = filename + ".html"
jsonFile = filename + ".json"

s3 = boto3.resource('s3')
UCKET = "your-bucket-name-here"
bucket = s3.Bucket(BUCKET)

s3.Object(BUCKET, htmlFile).put(Body=open(htmlFile, 'rb'), ContentType='text/html')
s3.Object(BUCKET, jsonFile).put(Body=open(jsonFile, 'rb'), ContentType='application/json')
