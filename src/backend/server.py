from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
from flask_cors import CORS
import pywhatkit as kit
import datetime
import os
import subprocess

app = Flask(__name__)
CORS(app)

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

@app.route('/api/open', methods=['POST'])
def open_application():
    data = request.json
    app_type = data.get('app_type')
    
    if app_type == "notepad":
        os.system("notepad")
    elif app_type == "firefox":
        os.system("start firefox")
    elif app_type == "vlc":
        os.system("start vlc")
    elif app_type == "url":
        url = data.get('url')
        os.system(f"start {url}")
    else:
        return jsonify({"error": "Invalid application type"}), 400
    
    return jsonify({"status": "success"}), 200

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

if __name__ == "__main__":
    app.run(debug=True)