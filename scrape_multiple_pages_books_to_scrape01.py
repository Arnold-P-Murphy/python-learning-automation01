
"""
This module demonstrates how to:
Scrape websites with Python and BeautifulSoup.
line into a list of words.
creates a CSV file from the scraped data.

Multiple pages primers:

Author: Arnold Murphy
Date: 2025-04-29
"""

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(
        f"Missing library: {e.name}. "
        f"Please install it using 'pip install {e.name}'."
    )
    exit(1)

# Removed redundant ImportError handling
import csv
import time

BASE_URL = "http://books.toscrape.com/"
START_URL = BASE_URL + "catalogue/category/books_1/index.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_soup(url):
    """
    Fetches the HTML content of a given URL and returns a BeautifulSoup object.

    Args:
        url (str): The URL to fetch.

    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_all_categories():
    """
    Fetches all book categories from the website.

    Returns:
    dict: A dictionary where keys are category names
    and values are their URLs.
    """
    soup = get_soup(BASE_URL)
    category_links = soup.select("div.side_categories ul li ul li a")
    return {
        link.text.strip(): BASE_URL + link["href"]
        for link in category_links
    }


def get_books_from_category(category_url):
    """
    Fetches all books from a given category, including pagination.

    Args:
        category_url (str): The URL of the category page.

    Returns:
    list: A list of tuples where each tuple contains the book title
    and its product page URL.
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
        url (str): The URL of the product page.

    Returns:
        dict: A dictionary containing book details such as title, description,
              price, availability, and more.
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
            continue  # Skip rows that don't have the expected structure
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


def main():
    """
    Main function to scrape book data from multiple categories on the website,
    parse the details, and save the data into a CSV file.
    """

    all_data = []
    categories = get_all_categories()
    print(f"Found {len(categories)} categories. Scraping each...")

    for category, url in categories.items():
        print(f"Scraping category: {category}")
        books = get_books_from_category(url)
        print(f"  ➜ Found {len(books)} books.")
        for title, product_url in books:
            try:
                data = parse_product_page(product_url)
                data["Category"] = category
                all_data.append(data)
                print(f"    ✔ {title}")
                time.sleep(0.5)  # polite delay
            except (requests.RequestException, AttributeError) as e:
                print(f"    ✖ Failed to scrape {product_url}: {e}")

    keys = list(all_data[0].keys()) if all_data else []
    with open("books.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_data)
    print("✅ Data written to books.csv")


if __name__ == "__main__":
    main()
# End-of-file (EOF)
