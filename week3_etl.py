"""
Week 3: ETL Pipeline

Build a mini ETL that:
- Extracts data from a JSON API endpoint
- Transforms it (adds a total field)
- Loads it into a SQLite database
"""

import requests
import sqlite3
import json


def extract_from_api(api_url: str) -> list:
    """
    Simulate extracting data from an API.
    The API returns a list of dicts like:
        [{"name": "Alice", "age": 30, "salary": 50000}]
    Use requests.get() to fetch and return the JSON content.
    """
    # TODO: implement (use requests.get(...).json())
    response = requests.get(api_url)
    data = response.json()
    return data


def transform_data(data: list) -> list:
    """
    Add a new key 'total' to each dict, which is salary * 12 (annual salary).
    Return the transformed list.
    """
    # TODO: implement
    for record in data:
        record['total'] = record['salary'] * 12
    return data


def load_to_sqlite(data: list, db_path: str) -> None:
    """
    Create a table 'employees' in the SQLite database at db_path.
    Insert all records from data.
    Assume each dict has keys: name, age, salary, total.
    """
    # TODO: implement
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            name TEXT,
            age INTEGER,
            salary REAL,
            total REAL
        )
    """)
    for record in data:
        cursor.execute("""
            INSERT INTO employees (name, age, salary, total)
            VALUES (?, ?, ?, ?)
        """, (record['name'], record['age'], record['salary'], record['total']))
    conn.commit()
    conn.close()    


def run_etl(api_url: str, db_path: str) -> None:
    """Run the full ETL pipeline."""
    # TODO: implement: call extract, transform, load
    data = extract_from_api(api_url)
    transformed_data = transform_data(data)
    load_to_sqlite(transformed_data, db_path)   
