# PROJECT:

A Python project that scrapes text from websites and retrieves geolocation data using the `ip-api.com` API.

# SUMMARY:

This project uses the Python Requests library to make API calls to `ip-api.com`. It takes an IP address as input, sends a request to the API, parses the JSON response, and extracts geolocation information.

# STEPS:

1. Import the necessary library: `requests`.
2. Define the base URL for the `ip-api.com` API.
3. Get the IP address you want to look up.
4. Construct the complete API URL by appending the IP to the base URL.
5. Send a GET request to the API endpoint using the `requests.get()` method.
6. Check if the request was successful (status code 200).
7. If successful, parse the JSON response using `response.json()`.
8. Extract the desired geolocation data from the parsed JSON object.

# STRUCTURE:

```
└── ip_geolocation.py

```

# DETAILED EXPLANATION:

- `ip_geolocation.py`: This is the main Python script that contains the code for making API requests, parsing JSON data, and extracting information.
# SETUP:

```bash
python ip_geolocation.py
```

# TAKEAWAYS:

1. You learned how to use the Python `requests` library to send HTTP requests.
2. You discovered how to interact with REST APIs.
3. You learned about handling JSON responses and extracting data.
4. You explored how to retrieve geolocation data from an IP address.

# SUGGESTIONS:

1. Implement error handling for invalid IP addresses or API request failures.
2. Create a command-line interface (CLI) to allow users to input different IP addresses.
3. Explore additional features of the `ip-api.com` API.
4. Consider caching API responses to improve performance if you're making frequent requests.
5. Create a web application with a graphical user interface (GUI) to present the geolocation data visually on a map.