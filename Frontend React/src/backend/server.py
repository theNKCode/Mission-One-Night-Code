from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from flask_cors import CORS
import pywhatkit as kit
import datetime
import os
import subprocess
import boto3
from insta import init
from twitter import init2

app = Flask(__name__)
CORS(app)
access_key = ''
secret_key = ''

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

@app.route('/geocode', methods=['POST'])
def geocode():
    data = request.json
    location_name = data.get('location')
    if not location_name:
        return jsonify({'error': 'No location provided'}), 400
    latitude, longitude = get_coordinates(location_name)
    if latitude is not None and longitude is not None:
        return jsonify({'latitude': latitude, 'longitude': longitude})
    else:
        return jsonify({'error': 'Location not found'}), 404
    

@app.route('/send_instant', methods=['POST'])
def send_instant():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')
    if not phone_number or not message:
        return jsonify({'error': 'Phone number and message are required'}), 400
    try:
        kit.sendwhatmsg_instantly(phone_number, message)
        return jsonify({'status': 'Message sent instantly'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send_scheduled', methods=['POST'])
def send_scheduled():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')
    hour = data.get('hour')
    minute = data.get('minute')
    if not phone_number or not message or hour is None or minute is None:
        return jsonify({'error': 'Phone number, message, hour, and minute are required'}), 400
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        return jsonify({'status': 'Message scheduled'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/speaker', methods=['GET'])
def run_command(cmd):
    import subprocess
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return jsonify({'output': result.stdout, 'error': result.stderr})

@app.route('/api/process', methods=['POST'])
def process_text():
    data = request.json
    text = data.get('text', '')
    processed_text = text.upper()  
    return jsonify({'processed_text': processed_text})

@app.route('/open_notepad', methods=['POST'])
def open_notepad():
    try:
        os.system('notepad.exe')
        return jsonify({"status": "success", "message": "Notepad opened successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/open_vlc', methods=['POST'])
def open_vlc():
    try:
        subprocess.Popen(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"])
        return jsonify({"status": "success", "message": "VLC opened successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/open_firefox', methods=['POST'])
def open_firefox():
    try:
        subprocess.Popen(["C:\\Program Files\\Mozilla Firefox\\firefox.exe"])
        return jsonify({"status": "success", "message": "Firefox opened successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/open_url', methods=['POST'])
def open_url():
    try:
        url = request.json.get('url')
        os.system(f'start {url}')
        return jsonify({"status": "success", "message": f"URL {url} opened successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/sns', methods=['POST'])
def sns():
    data = request.json
    topic = data['topic']
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='ap-south-1'
    )
    sns_client = session.client('sns')
    response = sns_client.create_topic(Name=topic)
    print("Topic ARN:", response['TopicArn'])
    return response['TopicArn']

@app.route('/snsemail', methods=['POST'])
def snsemail():
    data = request.json
    msg = data['message']
    subject = data['subject']
    session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)
    sns_client = session.client('sns')
    response = sns_client.publish(
        TopicArn='arn:aws:sns:ap-south-1:136103717721:nktest',
        Message=msg,        
        Subject=subject,
    )

    print("Email sent successfully and the message id is :",response['MessageId'])
    return response['MessageId']


@app.route('/ec2')
def ec2():
    img = "ami-04f8d7ed2f1a54b14"
    ec2 = boto3.resource(
        "ec2",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='ap-south-1'
    )
    create_instance = ec2.create_instances(
        ImageId=img,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
    )
    instance_id = create_instance[0].id
    print("Instance id is :-", instance_id)
    return jsonify({'instance_id': instance_id})


@app.route('/volume', methods=['POST'])
def volume():
    region = 'ap-south-1'
    size = request.json['size']
    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    response = ec2_client.create_volume(
        AvailabilityZone="ap-south-1a",
        Size=int(size)
    )
    volume_id = response['VolumeId']
    return jsonify({'volume_id': volume_id})

@app.route('/iamuser', methods=['POST'])
def iamuser():
    data = request.json
    name = data['name']
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='ap-south-1'
    )

    iam_client = session.client('iam')


    response = iam_client.create_user(
        UserName=name
    )
    print(f"IAM user '{name}' created successfully!")
    return jsonify({'username': name})
    
@app.route('/createbucket', methods=['POST'])
def createbucket():
    region = 'ap-south-1'
    data = request.json
    name = data['name']
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    bucket_name = 'bucket89484-' + name
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
    return jsonify({'bucket_name': bucket_name})

@app.route('/insta', methods=['GET'])
def insta():
    init()
    return jsonify({'status': 'Success'})

@app.route('/twitter', methods=['GET'])
def twitter():
    init2()
    return jsonify({'status': 'Success'})

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)