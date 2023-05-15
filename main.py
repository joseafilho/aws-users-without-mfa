import boto3

iam_client = boto3.client('iam')
response = iam_client.list_users()

mfa_users = []

for user in response['Users']:
    userMfa = iam_client.list_mfa_devices(UserName=user['UserName'])

    for uname in userMfa['MFADevices']:
        virtualEnabled = []
        virtualEnabled.append(uname['UserName'])

    if len(userMfa['MFADevices']) == 0:
        if user['UserName'] not in virtualEnabled:
            mfa_users.append(user['UserName'])

print(mfa_users)