"""
This module demonstrates how to:
Scrape websites with Python and BeautifulSoup.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-23
"""


# Import relevant libraries
import requests
from bs4 import BeautifulSoup

# Define the URL
URL = "https://realpython.github.io/fake-jobs/"

# Send a request to get the HTML code from that URL
response = requests.get(URL, headers={"Accept": "text/html"}, timeout=10)

# Parse the response
parsed_response = BeautifulSoup(response.text, "html.parser")

# Format the parsed HTML response in a way that’s easier to read
prettified_html = parsed_response.prettify()

# Write the prettified HTML to a file in the current directory
with open("response.txt", "w", encoding="utf-8") as file:
    file.write(prettified_html)

print("The response has been written to response.txt")

# End-of-file (EOF)
