"""
This module demonstrates how to:
- Scrape websites with Python and BeautifulSoup
- Extract structured data across multiple pages and categories
- Format and export the scraped data as CSV, JSON, XLSX, and readable text

Author: Arnold Murphy
Date: 2025-04-29
"""

import os
import csv
import json
import time
import requests
from bs4 import BeautifulSoup

try:
    import openpyxl  # noqa: F401 pylint: disable=unused-import
    from openpyxl import Workbook  # Used to generate Excel (.xlsx) output

except ImportError as e:
    print(f"Missing library: {e.name}. Install it with 'pip install openpyxl'")
    exit(1)

BASE_URL = "http://books.toscrape.com/"
START_URL = BASE_URL + "catalogue/category/books_1/index.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_soup(url):
    """
    Sends a GET request to the specified URL and returns
    a BeautifulSoup object for parsing HTML content.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing
        the parsed HTML content of the response.
    """
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_all_categories():
    """
    Fetches all book categories from the website and their corresponding URLs.

    Returns:
        dict: A dictionary where keys are category names and values are URLs.
    """
    soup = get_soup(BASE_URL)
    category_links = soup.select("div.side_categories ul li ul li a")
    return {
        link.text.strip(): BASE_URL + link["href"]
        for link in category_links
    }


def get_books_from_category(category_url):
    """
    Fetches all books from a given category URL, including pagination.

    Args:
        category_url (str): The URL of the category page to scrape.

    Returns:
        list: A list of tuples where each tuple contains
        the book title and its product page URL.
    """
    books = []
    while True:
        soup = get_soup(category_url)
        for article in soup.select("article.product_pod"):
            title = article.h3.a["title"]
            relative_link = article.h3.a["href"].replace("../../../", "")
            product_url = BASE_URL + "catalogue/" + relative_link
            books.append((title, product_url))
        next_button = soup.select_one("li.next a")
        if next_button:
            next_page = next_button["href"]
            category_url = category_url.rsplit("/", 1)[0] + "/" + next_page
        else:
            break
    return books


def parse_product_page(url):
    """
    Parses the product page of a book to extract its details.

    Args:
        url (str): The URL of the product page to scrape.

    Returns:
        dict: A dictionary containing the book's details, including title,
        description, pricing, availability, and other metadata.
    """
    soup = get_soup(url)
    title = soup.h1.text.strip()
    description_tag = soup.select_one("#product_description ~ p")
    description = description_tag.text.strip() if description_tag else "N/A"
    table = soup.select("table.table-striped tr")
    data = {}
    for row in table:
        try:
            key = row.th.text.strip()
            value = row.td.text.strip()
            data[key] = value
        except AttributeError:
            continue
    return {
        "Title": title,
        "UPC": data.get("UPC", ""),
        "Product Type": data.get("Product Type", ""),
        "Price (excl. tax)": data.get("Price (excl. tax)", ""),
        "Price (incl. tax)": data.get("Price (incl. tax)", ""),
        "Availability": data.get("Availability", ""),
        "Number of reviews": data.get("Number of reviews", ""),
        "Description": description,
        "Product Page": url
    }


def save_as_csv(data, path):
    """
    Saves the provided data as a CSV file.

    Args:
        data (list of dict): The data to save, where each dictionary
        represents a row.
        path (str): The file path where the CSV file will be saved.

    Returns:
        None
    """
    if not data:
        return
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)


def save_as_json(data, path):
    """
    Saves the provided data as a JSON file.

    Args:
        data (list of dict): The data to save, where each dictionary
        represents an item.
        path (str): The file path where the JSON file will be saved.

    Returns:
        None
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_as_excel(data, path):
    """
    Saves the provided data as an Excel (.xlsx) file.

    Args:
        data (list of dict): The data to save, where each dictionary
        represents a row.
        path (str): The file path where the Excel file will be saved.

    Returns:
        None
    """
    if not data:
        return
    wb = Workbook()
    ws = wb.active
    ws.title = "Books"
    headers = list(data[0].keys())
    ws.append(headers)
    for book in data:
        ws.append([book.get(h, "") for h in headers])
    wb.save(path)


def save_as_text(data, path):
    """
    Saves the provided data as a formatted text file.

    Args:
        data (list of dict): The data to save, where each dictionary
        represents a book with its details.
        path (str): The file path where the text file will be saved.

    Returns:
        None
    """
    with open(path, "w", encoding="utf-8") as f:
        categories = sorted(set(book["Category"] for book in data))
        for category in categories:
            f.write(f"=== {category} ===\n\n")
            for book in data:
                if book["Category"] == category:
                    f.write(f"Title: {book['Title']}\n")
                    f.write(f"Price: {book['Price (incl. tax)']}\n")
                    f.write(f"Availability: {book['Availability']}\n")
                    f.write(f"Page: {book['Product Page']}\n")
                    f.write(f"Description: {book['Description']}\n\n")
            f.write("   " * 3 + "\n\n")  # 3 spaces between categories


def main():
    """
    The main function orchestrates the entire scraping process:
    - Fetches all book categories and their URLs.
    - Scrapes book details from each category and product page.
    - Saves the scraped data in multiple formats (CSV, JSON, Excel, and text).
    """
    all_data = []
    categories = get_all_categories()
    print(f"Found {len(categories)} categories. Scraping...")

    for category, url in categories.items():
        print(f"→ {category}")
        books = get_books_from_category(url)
        for title, product_url in books:
            try:
                data = parse_product_page(product_url)
                data["Category"] = category
                all_data.append(data)
                print(f"   ✔ {title}")
                time.sleep(0.25)
            except (requests.RequestException, AttributeError, KeyError) as e:
                print(f"   ✖ Failed: {product_url} ({e})")

    os.makedirs("formatted_output", exist_ok=True)

    save_as_csv(all_data, "formatted_output/books.csv")
    save_as_json(all_data, "formatted_output/books.json")
    save_as_excel(all_data, "formatted_output/books.xlsx")
    save_as_text(all_data, "formatted_output/books_formatted.txt")

    print("\n✅ Done! Files saved in the 'formatted_output/' folder.")


if __name__ == "__main__":
    main()
