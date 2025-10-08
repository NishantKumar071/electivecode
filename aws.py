import boto3
import json

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    s3 = boto3.client('s3')
    input_text = event['text']
    response = comprehend.detect_sentiment(
        Text=input_text,
        LanguageCode='en'
    )
    sentiment = response['Sentiment']
    # Store result to S3
    output_bucket = 'your-s3-bucket'
    s3.put_object(
        Bucket=output_bucket,
        Key=f"results/{context.aws_request_id}.json",
        Body=json.dumps({"text": input_text, "sentiment": sentiment})
    )
    return {"sentiment": sentiment}
