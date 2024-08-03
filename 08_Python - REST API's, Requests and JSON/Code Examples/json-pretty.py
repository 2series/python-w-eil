# script get method Belgium in json format
# dumps module makes response prettier

from requests import get
from json import dumps

# Sending GET Request
# result = get('https://restcountries.com/v3.1/name/mexico').json()

# print(result)

# print(dumps(result, indent=2))

# Accessing Specific Data (Commented Out)
# print(result[0]['name']['official'])
# print(result[0]['capital'])
# print(result[0]['capital'][0])

# print(result[0]['name']['nativeName']['deu']['official'])

# Demo
# Building a Country Information Application
# A simple command-line application that allows users to retrieve information about a specific country using the REST Countries API. We'll use the script you provided as a starting point and add some features to make it more interactive

def get_country_info(country_name):
    try:
        response = get(f'https://restcountries.com/v3.1/name/{country_name}').json()
        return response[0]
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_country_info(country_info):
    if country_info:
        print(f"Official Name: {country_info['name']['official']}")
        print(f"Capital City: {country_info['capital'][0]}")
        print(f"Population: {country_info['population']}")
        print("Native Languages:")
        for language in country_info['languages'].values():
            print(f"- {language}")

def main():
    country_name = input("Enter a country name: ")
    country_info = get_country_info(country_name)
    print_country_info(country_info)

if __name__ == "__main__":
    main()