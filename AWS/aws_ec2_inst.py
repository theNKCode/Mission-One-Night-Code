import boto3
ec2 = boto3.resource('ec2',
                    'ap-south-1',
                     aws_access_key_id='',
                     aws_secret_access_key='',
                     )
instance = ec2.create_instances(InstanceType='t2.micro',
                                ImageId='',
                                MaxCount=1,
                                MinCount=1)

# #Deleting instance of aws using boto3
# ################################################################################
# import boto3

# def terminate_ec2_instance(instance_id):
#     # Create an EC2 client
#     ec2 = boto3.client(
#         'ec2',
#         region_name='ap-south-1',
#         aws_access_key_id='',
#         aws_secret_access_key=''
#     )

#     try:
#         # Terminate the instance
#         response = ec2.terminate_instances(InstanceIds=[instance_id])
        
#         # Output response
#         print("Terminating the instance. Response:")
#         print(response)
        
#         # Check the termination status
#         for instance in response['TerminatingInstances']:
#             print(f"Instance ID: {instance['InstanceId']}")
#             print(f"Current State: {instance['CurrentState']['Name']}")
#             print(f"Previous State: {instance['PreviousState']['Name']}")
            
#     except Exception as e:
#         print(f"Error terminating the instance: {e}")

# # Replace 'your_instance_id' with the actual instance ID you want to terminate
# instance_id = ''
# terminate_ec2_instance(instance_id)

import boto3

client = boto3.client('logs',
        region_name='ap-south-1',
        aws_access_key_id='',
        aws_secret_access_key=''
    )

import time
current_timestamp = int(time.time()*1000)

log_group_name ='test-log-group'
log_stream_name = 'test-log-stream'

response =client.create_log_group(

response = client.put_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name,
    logEvents=[
        {
            'timestamp': current_timestamp,
            'message': 'Apna 2nd msg'
        },
    ]
)

print(response)