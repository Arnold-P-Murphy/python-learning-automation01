"""
This module demonstrates how to:
Scrape websites with Python and BeautifulSoup.
line into a list of words.

Author: Arnold Murphy
Date: 2025-04-28
"""

# import all necessary libraries
import requests
from bs4 import BeautifulSoup

# define url of webpage to scrape from
URL = "https://realpython.github.io/fake-jobs/"

# send a request to get html code from the url and save the response
response_job = requests.get(URL, headers={"Accept": "text/html"}, timeout=10)

# use BeautifulSoup to parse the text from the response
parsed_response = BeautifulSoup(response_job.text, "html.parser")

# find all job titles
# uncomment the following line of code and FILL IN
titles = parsed_response.find_all("h2", class_="title is-5")

# iterate over the job titles and print the text for each
for title in titles:
    print(title.get_text(strip=True))

# End-of-file (EOF)
