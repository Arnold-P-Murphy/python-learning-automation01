"""
This module demonstrates how to : Use the requests library to make API calls.
use API keys
This module demonstrates how to : Use the requests library to make API calls.

Author: Arnold Murphy
Date: 2025-04-23
"""

import requests

# Replace with your actual API key
API_KEY = "ec9a4a5597b5c2567cfc219bf2ff3a1f"  # <-- Your OpenWeatherMap API key

# Coordinates for Prince Albert, Saskatchewan, Canada
latitude = 53.2033
longitude = -105.7531

# Base URL for weather data by coordinates
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Parameters for API request
params = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
    "units": "metric"  # Use 'imperial' for Fahrenheit
}

# Make the GET request
response = requests.get(BASE_URL, params=params, timeout=10)

# Check the response status and display data
if response.status_code == 200:
    data = response.json()
    city_name = data.get("name", "Unknown location")
    print(f"Weather in {city_name}, Saskatchewan, Canada:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")
else:
    print(
        f"Failed to retrieve weather data: {response.status_code} - "
        f"{response.text}"
    )


# End-of-file (EOF)
