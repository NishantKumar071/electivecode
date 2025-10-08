from flask import Flask, jsonify
import boto3
import json

app = Flask(_name_)
s3 = boto3.client('s3')

@app.route('/api/sentiment_results')
def get_sentiments():
    bucket = 'your-s3-bucket'
    response = s3.list_objects_v2(Bucket=bucket, Prefix='results/')
    results = []
    for obj in response.get('Contents', []):
        data = s3.get_object(Bucket=bucket, Key=obj['Key'])
        result = json.loads(data['Body'].read())
        results.append(result)
    return jsonify(results)

if _name_ == '_main_':
    app.run(debug=True)
