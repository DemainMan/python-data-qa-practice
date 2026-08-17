"""
Week 2: Pandas & SQL

Use pandas to manipulate data, and sqlite3 to query a database.
"""

import pandas as pd
import sqlite3


def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    # TODO: implement
    with open(filepath, 'r') as f:
        df = pd.read_csv(f)
    return df
    


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the DataFrame:
    - Drop rows where 'quantity' is 0 or negative
    - Fill missing 'price' with the column mean
    - Remove duplicate rows
    """
    # TODO: implement
    df = df[df['quantity'] > 0]  # Drop rows where quantity is 0 or negative
    df['price'].fillna(df['price'].mean(), inplace=True)  # Fill missing price with mean
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    return df


def total_sales(df: pd.DataFrame) -> float:
    """Return total sales (sum of quantity * price)."""
    # TODO: implement
    total = (df['quantity'] * df['price']).sum()
    return total


def most_sold_product(df: pd.DataFrame) -> str:
    """Return the product with the highest total quantity sold."""
    # TODO: implement
    product_sales = df.groupby('product')['quantity'].sum()
    most_sold = product_sales.idxmax()
    return most_sold


def query_sales(db_path: str, date: str) -> list:
    """
    Query the SQLite database 'sample_sales.db' and return all rows
    for a given date. The database has a table called 'sales' with
    columns (date, product, quantity, price).
    Return a list of tuples.
    """
    # TODO: implement
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales WHERE date = ?", (date,))
    results = cursor.fetchall()
    conn.close()
    return results
