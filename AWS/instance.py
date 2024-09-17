import boto3

def AWS_login():
    myinstance = boto3.resource(
    region_name='ap-south-1',
    service_name="ec2",
    aws_access_key_id="",
    aws_secret_access_key="")
    
    return myinstance
def InitiateInstance(login_cradiential):
    login_cradiential.create_instances(ImageId = "ami-0cc9838aa7ab1dce7",
                               InstanceType= "t2.micro",
                                MaxCount = 1,
                                MinCount = 1
    )


    
User_login = AWS_login()
InitiateInstance(User_login)
