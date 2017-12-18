import json
import re

print("Setting up the configuration file...")

sns_arn = input("Please enter your AWS SNS ARN: ")
sns_region = input("Please enter your AWS SNS Region (leave blank if using AWS config file): ")
sns_key = input("Please enter your AWS SNS Key (leave blank if using AWS credentials file): ")
sns_secret = input("Please enter your AWS SNS Secret (leave blank if using AWS credentials file): ")
sns_endpoint = input("Please enter the US area code and phone number you want to send notifications to: ")

# reduce the endpoint input to only digits and then take the last ten, adding the country code (as per SNS expectation)
endpoint_digits = re.match('[0-9]+', sns_endpoint).group(0)
sns_endpoint = "+1" + endpoint_digits[-10:]

data = {'aws': {'sns': {'arn': '"' + sns_arn + '"',
                        'region': '"' + sns_region + '"',
                        'key': '"' + sns_key + '"',
                        'secret': '"' + sns_secret + '"',
                        'endpoint': '"' + sns_endpoint + '"'}}}

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
