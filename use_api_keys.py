"""
This module demonstrates how to : Use the requests library to make API calls.
use API keys
This module demonstrates how to : Use the requests library to make API calls.

Author: Arnold Murphy
Date: 2025-04-23
"""

# import necessary libraries
import requests

# define base URL
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# define parameters
# parameters = {"q": "Paris,FR", "appid": "cc697336f7223cfe3fe05a30ee3dbe44"}
parameters = {
    "q": "Paris,FR",
    "appid": "cc697336f7223cfe3fe05a30ee3dbe44",
    "units": "metric",
    "cnt": 5
}
# make API request, passing in base URL and parameters
response = requests.get(BASE_URL, params=parameters, timeout=10)

# print out text from API response
print(response.text)


# End-of-file (EOF)
