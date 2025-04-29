"""
This module demonstrates how to:
Scrape websites with Python and BeautifulSoup.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-28
"""

# import relevant libraries
import requests
from bs4 import BeautifulSoup

# define the url
# FILL IN before running the code
URL = "https://realpython.github.io/fake-jobs/"

# send a request to get html code from that url
# uncomment the following line and replace with your code
# response = requests.get(url, headers={"Accept": "text/html"})

response = requests.get(URL, headers={"Accept": "text/html"}, timeout=10)
# parse the response
# uncomment the following line and replace with your code
parsed_response = BeautifulSoup(response.text, "html.parser")

# format the parsed HTML response in a way that’s easier to read
# and print it out
# and print it out
# uncomment the following line before running the code
prettified_html = parsed_response.prettify()
print(prettified_html)

# Write the prettified HTML to a file in the current directory
with open("response01.txt", "w", encoding="utf-8") as file:
    file.write(prettified_html)
# print the prettified HTML to a file
print("The response has been written to response01.txt")

# End-of-file (EOF)
