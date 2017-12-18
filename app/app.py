import sys
import time
import boto3
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

sns = boto3.client(
    'sns',
    aws_access_key_id=data['aws']['sns']['key'],
    aws_secret_access=data['aws']['sns']['secret']
)
topic = sns.topic(data['aws']['sns']['arn'])

subject = 'OpenVPN Connection: ' + sys.argv[1]
message = 'OpenVPN connection from ' + sys.argv[1] + ' at ' + time.strftime('%m/%d/%Y %H:%i:%s')

response = topic.publish(
    PhoneNumber=data['aws']['sns']['endpoint'],
    Message=message,
    Subject=subject,
    MessageStructure='string',
    MessageAttributes={
        'string': {
            'DataType': 'String'
        }
    }
)

# successfully exit
exit(0)

