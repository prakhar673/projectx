import boto3
import time
import json


def get_number_of_message(queue_url):
    sqs = boto3.client('sqs')
    i=0;
    number_message_list=list()
    while i<10:
        response2= sqs.get_queue_attributes(QueueUrl=queue_url,AttributeNames=['All'])
        number_message=int(response2['Attributes']['ApproximateNumberOfMessages'])
        number_message_list.append(number_message)
        time.sleep(2)
        i=i+1
    return max(number_message_list)


def lambda_invoke():
    sqs = boto3.client('sqs')
    number_message = get_number_of_message('https://sqs.eu-west-1.amazonaws.com/653524338143/dlq_s3_lambda')
    print(number_message)
    print("****************************************\n*************************************")
    i=0
    event_list=list()
    while i<int(number_message):
        x = sqs.receive_message(QueueUrl='https://sqs.eu-west-1.amazonaws.com/653524338143/dlq_s3_lambda')
        print x.keys()
        message=x['Messages'][0]['Body']
        message = json.loads(message)
        message = message['Message']
        event_list.append(x)
        i=i+1
         #   print sqs.receive_message(QueueUrl='https://sqs.eu-west-1.amazonaws.com/653524338143/dlq_s3_lambda',MaxNumberOfMessages=10,WaitTimeSeconds=20)

    lambda1 = boto3.client('lambda')
    for event in event_list:
        response = lambda1.invoke(
                        FunctionName='arn:aws:lambda:eu-west-1:653524338143:function:s3_test',
                        InvocationType='RequestResponse',
                        LogType='None',
                        Payload=bytes(message)
                        )
        print response

lambda_invoke()
