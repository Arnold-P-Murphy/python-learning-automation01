"""
This module demonstrates how to: Use the requests library to make API calls.


Author: Arnold Murphy
Date: 2025-04-23
"""

# import necessary libraries
import requests

# define base URL
BASE_URL = "https://api.upcitemdb.com/prod/trial/lookup"

# define parameters
parameters = {"upc": "025000044908"}

# make API request, passing in base URL and parameters
response = requests.get(BASE_URL, params=parameters, timeout=10)

# print out the response URL
print(response.url)


# End-of-file (EOF)
