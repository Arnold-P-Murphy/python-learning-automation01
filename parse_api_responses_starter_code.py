"""
This module demonstrates how to : PARSE API RESPONSES
Author: Arnold Murphy
Date: 2025-04-23
"""

# import necessary libraries
import json
import requests

# EXAMPLE 1: lemonade with raspberry
print("\nPRODUCT EXAMPLE 1\n")
# define base URL
BASE_URL = "https://api.upcitemdb.com/prod/trial/lookup"
# define parameters
parameters = {"upc": "025000044908"}
# make API request, passing in base URL and parameters
response = requests.get(BASE_URL, params=parameters, timeout=10)
# parse the text from the API response using JSON schema
info = json.loads(response.text)
# extract the first item from info using the index 0
item = info["items"][0]
# extract the product’s title by indexing item
title = item["title"]
# extract the product’s brand by indexing item
brand = item["brand"]
# print out title
print("title:", title)
# print out brand
print("brand:", brand)

# EXAMPLE 2: ridged potato chips
print("\nPRODUCT EXAMPLE 2\n")
# define base URL
BASE_URL = "https://api.upcitemdb.com/prod/trial/lookup"
# define parameters
parameters = {"upc": "028400516686"}
# make API request, passing in base URL and parameters
response = requests.get(BASE_URL, params=parameters, timeout=10)
# parse the text from the API response using JSON schema
info = json.loads(response.text)
# extract the first item from info using the index 0
item = info["items"][0]
# extract the product’s title by indexing item
title = item["title"]
# extract the product’s brand by indexing item
brand = item["brand"]
# print out title
print("title:", title)
# print out brand
print("brand:", brand)

# End-of-file (EOF)
