# """
# This script uses the ip-api.com API to retrieve geolocation data for a given IP address.
# """
# import requests

# def get_geolocation(ip_address):
#     """
#     Retrieves geolocation data for a given IP address using the ip-api.com API.

#     Args:
#         ip_address (str): The IP address to look up.

#     Returns:
#         dict: A dictionary containing geolocation information or an error message.
#     """

#     # Define the base URL for the ip-api.com API
#     base_url = "http://ip-api.com/json/"

#     # Construct the complete API URL by appending the IP address
#     api_url = base_url + ip_address

#     try:
#         # Send a GET request to the API endpoint
#         response = requests.get(api_url)

#         # Check if the request was successful (status code 200)
#         response.raise_for_status()

#         # Parse the JSON response
#         data = response.json()

#         # Return the geolocation data
#         return data

#     except requests.exceptions.RequestException as e:
#         return {"error": f"An error occurred: {e}"}


# if __name__ == "__main__":
#     # Example usage:
#     ip_address = "151.101.3.5"  # Replace with the IP address you want to look up
#     geolocation_data = get_geolocation(ip_address)

#     # Print the geolocation data
#     if "error" in geolocation_data:
#         print(geolocation_data["error"])
#     else:
#         print(f"Geolocation data for IP address {ip_address}:")
#         for key, value in geolocation_data.items():
#             print(f"{key}: {value}")



"""
This script uses the ip-api.com API to retrieve geolocation data for a given IP address.
"""
import requests

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


def main():
    # Prompt the user to input the IP address
    ip_address = input("Please enter the IP address you want to look up: ")

    # Get the geolocation data
    geolocation_data = get_geolocation(ip_address)

    # Print the geolocation data
    if "error" in geolocation_data:
        print(geolocation_data["error"])
    else:
        print(f"Geolocation data for IP address {ip_address}:")
        for key, value in geolocation_data.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()