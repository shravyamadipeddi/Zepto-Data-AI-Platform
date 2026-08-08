import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Base URL
BASE_URL = "https://books.toscrape.com/"

# Store all books
books_data = []

# Scrape first 5 catalogue pages
for page in range(1, 6):

    page_url = f"{BASE_URL}catalogue/page-{page}.html"

    print(f"\nScraping Page {page}")

    response = requests.get(page_url)

    if response.status_code != 200:
        print(f"Failed to load page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"Books found: {len(books)}")

    # Loop through every book on the page
    for book in books:

        try:
            # Title
            title = book.h3.a["title"]

            # Price
            price = book.find("p", class_="price_color").text.strip()

            # Star Rating
            rating = book.find("p")["class"][1]

            # Availability
            availability = (
                book.find("p", class_="instock availability")
                .text.strip()
            )

            # Relative book URL
            relative_link = book.h3.a["href"]

            # Convert to absolute URL
            book_url = urljoin(page_url, relative_link)

            # Open individual book page
            book_response = requests.get(book_url)

            if book_response.status_code == 200:

                book_soup = BeautifulSoup(
                    book_response.text,
                    "html.parser"
                )

                # Breadcrumb:
                # Home > Books > Category > Book
                breadcrumb = book_soup.select("ul.breadcrumb li a")

                if len(breadcrumb) >= 3:
                    category = breadcrumb[2].text.strip()
                else:
                    category = "Unknown"

            else:
                category = "Unknown"

            books_data.append([
                title,
                price,
                rating,
                availability,
                category
            ])

        except Exception as e:

            print(f"Error scraping '{title}': {e}")

# Create DataFrame
df = pd.DataFrame(
    books_data,
    columns=[
        "title",
        "price",
        "star_rating",
        "availability",
        "category"
    ]
)

print("\nFirst 5 Rows\n")
print(df.head())

print("\nTotal Books:", len(df))

# Save CSV
df.to_csv(
    "data_pipeline/books.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nbooks.csv created successfully!")

print("\nCleaning Data...")
df = pd.read_csv("data_pipeline/books.csv")

df["price_gbp"] = (
    df["price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["rating"] = df["star_rating"].map(rating_map)

df["in_stock"] = df["availability"].str.contains("In stock")

df["price_gbp"] = df["price_gbp"].fillna(
    df["price_gbp"].median()
)

df["rating"] = df["rating"].fillna(
    df["rating"].median()
)

df = df.dropna(
    subset=["title", "category"]
)

GBP_TO_INR = 105.50

df["price_inr"] = (
    df["price_gbp"] * GBP_TO_INR
).round(2)

print(df.info())

print(df.head())

df.to_csv(
    "data_pipeline/books_cleaned.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nbooks_cleaned.csv created successfully!")