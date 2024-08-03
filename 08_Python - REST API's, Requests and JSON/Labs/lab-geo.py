
# script retrieves information about the user's country and its capital using two APIs: ip-api.com and restcountries.com


from requests import get
from json import dumps

# Get user's country information in JSON
# response = get(f'http://ip-api.com/json/').json()

# print(response)

# country = response['country']
#country = 'canada'

# Get country information
# response_geo = get(f'https://restcountries.com/v3.1/name/{country}?fulltext=true').json()

# print(dumps(response_geo, indent=2))


# Print country and capital
# for record in response_geo:
#     print(record['name']['common'])
#     print(record['capital'][0])

    
    
# Country Information Application
# This application allows users to retrieve information about a specific country using the REST Countries API. The application is built using Python and features a simple command-line interface


# Define a function to retrieve country information
def get_country_info(country_name):
    try:
        # Send a GET request to the REST Countries API
        response = get(f'https://restcountries.com/v3.1/name/{country_name}').json()
        # Return the first result (assuming there's only one match)
        return response[0]
    except Exception as e:
        # Print an error message if something goes wrong
        print(f"Error: {e}")
        return None

# Define a function to print country information
def print_country_info(country_info):
    if country_info:
        # Print official name, capital city, population, and native languages
        print(f"Official Name: {country_info['name']['official']}")
        print(f"Capital City: {country_info['capital'][0]}")
        print(f"Population: {country_info['population']}")
        print("Native Languages:")
        for language, name in country_info['languages'].items():
            print(f"- {name} ({language})")
        print("Currencies:")
        for currency, name in country_info['currencies'].items():
            print(f"- {name} ({currency})")
        print("Flag:")
        print(f"- {country_info['flags']['png']}")
        print("Neighboring Countries:")
        for neighbor in country_info['borders']:
            neighbor_info = get_country_info(neighbor)
            if neighbor_info:
                print(f"- {neighbor_info['name']['official']}")

# Define the main function
def main():
    # Ask the user for a country name
    country_name = input("Enter a country name: ")
    # Retrieve country information
    country_info = get_country_info(country_name)
    # Print country information
    print_country_info(country_info)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()