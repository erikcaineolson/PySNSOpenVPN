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

subject = 'OpenVPN %s: %s' % (sys.argv[1].capitalize(), sys.argv[2])

if sys.argv[1] == 'connect':
    message = 'OpenVPN connection from %s (%s) at %s' % (sys.argv[2], sys.argv[3], time.strftime('%m/%d/%Y %H:%i:%s'))
else:
    message = 'OpenVPN disconnect from %s (%s) at %s; %s bytes sent and %s bytes received' % \
              (sys.argv[2], sys.argv[3], time.strftime('%m/%d/%Y %H:%i:%s'), sys.argv[4], sys.argv[5])


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

