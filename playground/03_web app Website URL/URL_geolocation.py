# script uses the ip-api.com API to retrieve geolocation data for a given website URL

from flask import Flask, render_template, request, jsonify
import requests
import socket
import json
from flask import Response

app = Flask(__name__)

# Constants
IP_API_URL = 'http://ip-api.com/json/{}'

# Helper functions
def get_geolocation(ip_address):
    """Retrieve geolocation data for a given IP address"""
    try:
        response = requests.get(IP_API_URL.format(ip_address))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def get_ip_address(url):
    """Retrieve IP address for a given URL"""
    try:
        return socket.gethostbyname(url)
    except socket.gaierror as e:
        return {'error': str(e)}

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('index.html', error='No URL provided'), 400
        ip_address = get_ip_address(url)
        if isinstance(ip_address, dict) and 'error' in ip_address:
            return render_template('index.html', error=ip_address['error']), 400
        geolocation_data = get_geolocation(ip_address)
        if isinstance(geolocation_data, dict) and 'error' in geolocation_data:
            return render_template('index.html', error=geolocation_data['error']), 400
        return render_template('index.html', url=url, ip_address=ip_address, geolocation_data=geolocation_data)
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    ip_address = get_ip_address(url)
    if isinstance(ip_address, dict) and 'error' in ip_address:
        return jsonify(ip_address), 400
    geolocation_data = get_geolocation(ip_address)
    if isinstance(geolocation_data, dict) and 'error' in geolocation_data:
        return jsonify(geolocation_data), 400
    formatted_output = {
        "Geolocation Data": {
            "URL": url,
            "IP Address": ip_address,
            "Location": {
                "City": geolocation_data["city"],
                "Region": geolocation_data["regionName"],
                "Country": geolocation_data["country"],
                "Zip Code": geolocation_data["zip"]
            },
            "Coordinates": {
                "Latitude": geolocation_data["lat"],
                "Longitude": geolocation_data["lon"]
            },
            "ISP": geolocation_data["isp"],
            "Organization": geolocation_data["org"],
            "Timezone": geolocation_data["timezone"]
        }
    }
    return Response(json.dumps(formatted_output, indent=2), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)