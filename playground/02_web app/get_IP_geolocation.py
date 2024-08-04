
# script uses the ip-api.com API to retrieve geolocation data for a given IP address

from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

def get_geolocation(ip_address):
    """
    Retrieves geolocation data for a given IP address using the ip-api.com API.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing geolocation information or an error message.
    """

    # Define the base URL for the ip-api.com API
    base_url = "http://ip-api.com/json/"

    # Construct the complete API URL by appending the IP address
    api_url = base_url + ip_address

    try:
        # Send a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Return the geolocation data
        return data

    except requests.exceptions.RequestException as e:
        return {"error": f"An error occurred: {e}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        geolocation_data = get_geolocation(ip_address)

        if "error" in geolocation_data:
            return render_template('index.html', error=geolocation_data["error"])
        else:
            return render_template('index.html', ip_address=ip_address, geolocation_data=geolocation_data)
    else:
        return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
    ip_address = request.args.get('ip_address')
    if ip_address:
        geolocation_data = get_geolocation(ip_address)
        return jsonify(geolocation_data)
    else:
        return jsonify({"error": "Please provide an IP address"}), 400

if __name__ == "__main__":
    app.run(debug=True)