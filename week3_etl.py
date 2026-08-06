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
    pass


def transform_data(data: list) -> list:
    """
    Add a new key 'total' to each dict, which is salary * 12 (annual salary).
    Return the transformed list.
    """
    # TODO: implement
    pass


def load_to_sqlite(data: list, db_path: str) -> None:
    """
    Create a table 'employees' in the SQLite database at db_path.
    Insert all records from data.
    Assume each dict has keys: name, age, salary, total.
    """
    # TODO: implement
    pass


def run_etl(api_url: str, db_path: str) -> None:
    """Run the full ETL pipeline."""
    # TODO: implement: call extract, transform, load
    pass
