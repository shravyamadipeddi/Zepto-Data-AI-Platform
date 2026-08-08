import sqlite3
import pandas as pd

conn = sqlite3.connect("data_pipeline/books.db")

query1 = """
SELECT *
FROM books
WHERE rating = 5;
"""

df1 = pd.read_sql(query1, conn)

print("\nQuery 1 - Books with Rating 5")
print(df1)
df1.to_csv(
    "data_pipeline/query1_rating5.csv",
    index=False
)

query2 = """
SELECT title, price_inr
FROM books
ORDER BY price_inr DESC;
"""

df2 = pd.read_sql(query2, conn)

print("\nQuery 2 - Highest Price")
print(df2)

df2.to_csv(
    "data_pipeline/query2_highest_price.csv",
    index=False
)

query3 = """
SELECT *
FROM books
LIMIT 10;
"""

df3 = pd.read_sql(query3, conn)

print("\nQuery 3 - First 10 Books")
print(df3)

df3.to_csv(
    "data_pipeline/query3_limit10.csv",
    index=False
)

query4 = """
SELECT DISTINCT category_name
FROM categories;
"""

df4 = pd.read_sql(query4, conn)

print("\nQuery 4 - Categories")
print(df4)

df4.to_csv(
    "data_pipeline/query4_categories.csv",
    index=False
)

query5 = """
SELECT title, price_gbp
FROM books
WHERE price_gbp
BETWEEN 20 AND 40;
"""

df5 = pd.read_sql(query5, conn)

print("\nQuery 5 - Price Between 20 and 40")
print(df5)

df5.to_csv(
    "data_pipeline/query5_between.csv",
    index=False
)

query6 = """
SELECT
    b.title,
    c.category_name,
    b.rating,
    b.price_inr
FROM books b
JOIN categories c
ON b.category_id = c.category_id
ORDER BY b.title;
"""

join_sql = pd.read_sql(query6, conn)

print("\nQuery 6 - JOIN")
print(join_sql)

join_sql.to_csv(
    "data_pipeline/query6_join.csv",
    index=False
)

books_df = pd.read_sql("SELECT * FROM books", conn)

categories_df = pd.read_sql("SELECT * FROM categories", conn)

merge_df = pd.merge(
    books_df,
    categories_df,
    on="category_id"
)

print("\nPandas Merge Result")
print(merge_df.head())

merge_df.to_csv(
    "data_pipeline/pandas_merge.csv",
    index=False
)

conn.close()

print("\nAll SQL queries executed successfully!")

# Compare SQL JOIN and Pandas Merge

sql_join = join_sql.sort_values(
    by=["title"]
).reset_index(drop=True)

pandas_join = merge_df[
    [
        "title",
        "category_name",
        "rating",
        "price_inr"
    ]
].sort_values(
    by=["title"]
).reset_index(drop=True)

print("\nComparing SQL JOIN and Pandas Merge")

comparison = sql_join.equals(pandas_join)

print("Are they equivalent?", comparison)