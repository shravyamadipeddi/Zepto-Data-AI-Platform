import sqlite3
import pandas as pd

# Read cleaned CSV
df = pd.read_csv("data_pipeline/books_cleaned.csv")

# Connect to SQLite
conn = sqlite3.connect("data_pipeline/books.db")

cursor = conn.cursor()

# Categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE
)
""")

# Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price_gbp REAL,
    price_inr REAL,
    rating INTEGER,
    in_stock INTEGER,
    category_id INTEGER,
    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)
)
""")

# Insert categories
categories = df["category"].unique()

for category in categories:
    cursor.execute(
        "INSERT OR IGNORE INTO categories(category_name) VALUES(?)",
        (category,)
    )

# Insert books
for _, row in df.iterrows():

    cursor.execute(
        "SELECT category_id FROM categories WHERE category_name=?",
        (row["category"],)
    )

    category_id = cursor.fetchone()[0]

    cursor.execute(
        """
        INSERT INTO books(
            title,
            price_gbp,
            price_inr,
            rating,
            in_stock,
            category_id
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            row["title"],
            row["price_gbp"],
            row["price_inr"],
            row["rating"],
            int(row["in_stock"]),
            category_id
        )
    )

conn.commit()

conn.close()

print("books.db created successfully!")