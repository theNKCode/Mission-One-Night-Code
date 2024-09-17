import boto3
from datetime import datetime, timedelta
import time

client = boto3.client('logs'
            'ap-south-1',
            aws_access_key_id='',
            aws_secret_access_key='',
        )

query = "fields @timestamp, @message | parse @message \"username: * ClinicID: * nodename: *\" as username, ClinicID, nodename | filter ClinicID = 7667 and username='simran+test@example.com'"

log_group = '/aws/lambda/NAME_OF_YOUR_LAMBDA_FUNCTION'

start_query_response = client.start_query(
    logGroupName=log_group,
    startTime=int((datetime.today() - timedelta(hours=5)).timestamp()),
    endTime=int(datetime.now().timestamp()),
    queryString=query,
)

query_id = start_query_response['queryId']

response = None

while response == None or response['status'] == 'Running':
    print('Waiting for query to complete ...')
    time.sleep(1)
    response = client.get_query_results(
        queryId=query_id
    