import boto3

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances(
    # Filters=[
    #     {
    #         # 'Name': 'string',
    #         # 'Values': [
    #         #     'string',
    #         # ],
    #         # 'Name': 'availability-zone',
    #         # 'Values': [
    #         #     'us-east-2',
    #         #     'us-east-1',
    #         #     'us-west-1',
    #         #     'us-west-2',
    #         ]
    #     },
    # ],
    # # InstanceIds=[
    # #     'string',
    # # ],
    # DryRun=False,
    # MaxResults=123,
    # # NextToken='string'
)

for r in response['Reservations']:
    for i in r['Instances']:
        print(i['InstanceId'], i['Hypervisor'])
        for b in i['BlockDeviceMappings']:
            print(b['Ebs']['DeleteOnTermination'])


