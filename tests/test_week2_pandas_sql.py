import pandas as pd
import sqlite3
import pytest
from week2_pandas_sql import load_csv, clean_data, total_sales, most_sold_product, query_sales


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'date': ['2024-01-01', '2024-01-01', '2024-01-02'],
        'product': ['Apple', 'Banana', 'Apple'],
        'quantity': [2, 5, 0],
        'price': [1.5, 0.75, 2.0]
    })


def test_clean_data(sample_df):
    cleaned = clean_data(sample_df)
    assert len(cleaned) == 2  # row with quantity=0 dropped
    assert cleaned['price'].isna().sum() == 0


def test_total_sales(sample_df):
    # After cleaning: Apple=2*1.5, Banana=5*0.75 => 3 + 3.75 = 6.75
    cleaned = clean_data(sample_df)
    assert total_sales(cleaned) == 6.75


def test_most_sold_product(sample_df):
    cleaned = clean_data(sample_df)
    assert most_sold_product(cleaned) == 'Banana'  # 5 > 2


def test_query_sales(tmp_path):
    # Create a temporary SQLite DB
    db_path = tmp_path / "sales.db"
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("CREATE TABLE sales (date TEXT, product TEXT, quantity INTEGER, price REAL)")
        conn.execute("INSERT INTO sales VALUES ('2024-01-05', 'Apple', 2, 1.5)")
        conn.execute("INSERT INTO sales VALUES ('2024-01-05', 'Banana', 3, 0.75)")
        conn.commit()
    finally:
        conn.close()

    result = query_sales(str(db_path), '2024-01-05')
    assert len(result) == 2
    assert result[0][1] in ['Apple', 'Banana']
