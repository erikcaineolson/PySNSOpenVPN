# PySNSOpenVPN
Python script to notify an endpoint on Open VPN Connect/Disconnect

This script assumes you have already set up SNS, IAM, and your OpenVPN server

### Requirements
1. Python 3.6+
2. OpenVPN
3. Amazon AWS Account
4. Amazon Python SDK (Boto3)

This script _does not require_ Amazon credentials saved locally in `~/.aws/credentials` or the default region in `/.aws/config`, although you can use them if you prefer

### OpenVPN Setup
Add the following lines to your configuration file _or_ pass `--script-security 2 --up /path/to/your/script` when connecting (I recommend using the config file, especially if sharing your VPN):
```
script-security 2
client-connect python /path/to/app.py $common_name
```

### Installation
Run `python setup.py` (you will need your IAM credentials and SNS Topic for this part if you're not using the AWS CLI or locally-stored credentials)

### Further...
Please feel free to make changes and PR's! Neither Python nor OpenVPN are in my "normal" toolboxes so I'm _certain_ this can be improved upon.
