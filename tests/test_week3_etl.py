import sqlite3
import json
import pytest
from week3_etl import extract_from_api, transform_data, load_to_sqlite, run_etl


def fake_api_response(*args, **kwargs):
    class FakeResponse:
        def json(self):
            return [
                {"name": "Alice", "age": 30, "salary": 50000},
                {"name": "Bob", "age": 25, "salary": 60000},
            ]
    return FakeResponse()


def test_extract_from_api(mocker):
    mocker.patch("week3_etl.requests.get", side_effect=fake_api_response)
    data = extract_from_api("http://fake-api.com/employees")
    assert len(data) == 2
    assert data[0]["name"] == "Alice"


def test_transform_data():
    data = [
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob", "age": 25, "salary": 60000},
    ]
    transformed = transform_data(data)
    assert transformed[0]["total"] == 600000
    assert transformed[1]["total"] == 720000


def test_load_to_sqlite(tmp_path):
    db_path = tmp_path / "test.db"
    data = [
        {"name": "Alice", "age": 30, "salary": 50000, "total": 600000}
    ]
    load_to_sqlite(data, str(db_path))
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    assert len(rows) == 1
    assert rows[0][0] == "Alice"
    assert rows[0][3] == 600000


def test_run_etl(mocker, tmp_path):
    mocker.patch("week3_etl.requests.get", side_effect=fake_api_response)
    db_path = tmp_path / "etl.db"
    run_etl("http://fake-api.com", str(db_path))
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0]
    conn.close()
    assert count == 2
