# script retrieves information about a specific IP address using the ip-api.com API and prints the result in a pretty JSON format
# dumps module Response is prettier

from requests import get
from json import dumps

# ip = '151.101.3.5' #cnn.com

# result = get(f'http://ip-api.com/json/{ip}').json()


# print(result) # response dict of values
# print(result['city']) # response San Francisco

# print(dumps(result, indent=2))


# Demo
# script retrieves the driver and constructor standings from the Ergast API and prints the result in a pretty JSON format

# Set the API endpoints and parameters
driver_standings_endpoint = 'http://ergast.com/api/f1/current/driverStandings.json'
constructor_standings_endpoint = 'http://ergast.com/api/f1/current/constructorStandings.json'

# Make the API requests
driver_standings_response = get(driver_standings_endpoint)
constructor_standings_response = get(constructor_standings_endpoint)

# Check if the requests were successful
if driver_standings_response.status_code == 200 and constructor_standings_response.status_code == 200:
    # Parse the JSON responses
    driver_standings = driver_standings_response.json()
    constructor_standings = constructor_standings_response.json()

    # Print the standings in a pretty JSON format
    print("Driver Standings:")
    print(dumps(driver_standings, indent=2))
    print("\nConstructor Standings:")
    print(dumps(constructor_standings, indent=2))
else:
    print(f"Failed to retrieve standings. Status codes: {driver_standings_response.status_code}, {constructor_standings_response.status_code}")