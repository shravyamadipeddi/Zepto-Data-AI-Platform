# Module 1 – Data Pipeline

## Project Overview

This module implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python.

The project scrapes book information from the public website "Books to Scrape", cleans and transforms the data, converts book prices from GBP to INR using a fixed conversion rate, stores the cleaned data in a normalized SQLite database, and executes SQL and Pandas queries for analysis.

This project demonstrates web scraping, data cleaning, relational database design, SQL querying, and Pandas integration.

---

## Technologies Used

- Python 3.x
- Requests
- BeautifulSoup4
- Pandas
- SQLite3
- lxml

---

## Project Structure

```
data_pipeline/
│
├── scraper.py
├── database.py
├── queries.py
├── books.csv
├── books_cleaned.csv
├── books.db
├── query1_rating5.csv
├── query2_highest_price.csv
├── query3_limit10.csv
├── query4_categories.csv
├── query5_between.csv
├── query6_join.csv
├── pandas_merge.csv
├── requirements.txt
└── README.md
```

---

## Dataset

Source:

https://books.toscrape.com/

Books Scraped: "100"

Pages Scraped: "First 5 catalogue pages"

Extracted Fields:

- Title
- Price (GBP)
- Star Rating
- Availability
- Category

---

## Data Cleaning

The following cleaning steps were performed:

- Removed the currency symbol from the price.
- Converted price to a floating-point column (`price_gbp`).
- Converted star ratings from text (One–Five) to integers (1–5).
- Converted availability to a Boolean (`True`/`False`).
- Filled missing numeric values using median imputation.
- Removed rows with missing title or category.
- Added a converted price column (`price_inr`).

---

## Currency Conversion

Fixed conversion rate used:

"1 GBP = 105.50 INR"

This is the project-defined fixed conversion rate specified in the assignment.

---

## Database Schema

### Categories Table

| Column | Type |
|---------|------|
| category_id | INTEGER PRIMARY KEY |
| category_name | TEXT UNIQUE |

### Books Table

| Column | Type |
|---------|------|
| book_id | INTEGER PRIMARY KEY |
| title | TEXT |
| price_gbp | REAL |
| price_inr | REAL |
| rating | INTEGER |
| in_stock | INTEGER |
| category_id | INTEGER (Foreign Key) |

Relationship:

```
categories (1)
      |
      | category_id
      |
books (Many)
```

---

## SQL Queries Implemented

The project includes the following SQL queries:

1. SELECT with WHERE
2. ORDER BY
3. LIMIT
4. DISTINCT
5. BETWEEN
6. INNER JOIN

All query outputs are saved as CSV files.

---

## Pandas Operations

- Read SQL query results using `pd.read_sql()`.
- Reproduced the SQL JOIN using `pd.merge()`.
- Verified that both outputs are equivalent.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd Zepto-Data-AI-Platform
```

Install dependencies:

```bash
pip install -r data_pipeline/requirements.txt
```

---

## Running the Project

### Step 1 – Scrape and Clean Data

```bash
python data_pipeline/scraper.py
```

Generates:

- books.csv
- books_cleaned.csv

---

### Step 2 – Create SQLite Database

```bash
python data_pipeline/database.py
```

Generates:

- books.db

---

### Step 3 – Execute SQL Queries

```bash
python data_pipeline/queries.py
```

Generates:

- SQL query outputs
- Pandas merge output

---

## Output Files

- books.csv
- books_cleaned.csv
- books.db
- SQL query CSV files
- pandas_merge.csv

---

## Author

Shravya Madipeddi