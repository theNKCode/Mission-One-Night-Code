import boto3
def AWS_clinet_login():
    
    ec2_client = boto3.client(
        service_name="ec2",
        region_name='ap-south-1',
        aws_access_key_id="",
        aws_secret_access_key=""
    )
    
    return ec2_client
def DeleteInstance(ec2_client):
    list_instances=[input('Instance-id:') for i in range(int(input('number of instances to delete:')))]
    response = ec2_client.terminate_instances(
        InstanceIds=list_instances
    )
    print("Instances Terminated!!!")
    return response

ec2_client = AWS_clinet_login()
response = DeleteInstance(ec2_client)
print(response)
