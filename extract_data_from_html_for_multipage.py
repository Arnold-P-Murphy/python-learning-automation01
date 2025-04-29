"""
This module demonstrates how to:
Scrape websites with Python and BeautifulSoup.
line into a list of words.

Multiple pages primers:


Author: Arnold Murphy
Date: 2025-04-29
"""


# import all necessary libraries
import requests
from bs4 import BeautifulSoup

# define url of webpage to scrape from
URL = "https://remote.co/remote-jobs/developer"

# send a request to get html code from the url and save the response
headers = {"Accept": "text/html"}
response_job = requests.get(URL, headers=headers, timeout=10)

# use BeautifulSoup to parse the text from the response
parsed_response = BeautifulSoup(response_job.text, "html.parser")

# find all job titles
titles = parsed_response.find_all("h2", class_="title is-5")

# iterate over the job titles and print the text for each
if titles:
    for title in titles:
        print(title.text)
else:
    print("No titles found.")

# End-of-file (EOF)
