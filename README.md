# Python Data & QA Practice

A collection of coding exercises for practicing **Data Engineering** and **Quality Assurance** with Python.

## Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/python-data-qa-practice.git
cd python-data-qa-practice

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running the tests

```bash
pytest -v
```

Initially, all tests will fail. Your job is to implement the functions in:

- `week1_basics.py`
- `week2_pandas_sql.py`
- `week3_etl.py`
- `week4_qa.py`

Once you've implemented all functions, all tests should pass.

## Project structure

```
python-data-qa-practice/
├── .github/workflows/ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .editorconfig
├── .env.example
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
├── pyproject.toml
├── data/
│   └── sample_sales.csv
├── week1_basics.py
├── week2_pandas_sql.py
├── week3_etl.py
├── week4_qa.py
└── tests/
    ├── __init__.py
    ├── test_week1_basics.py
    ├── test_week2_pandas_sql.py
    ├── test_week3_etl.py
    └── test_week4_qa.py
```

## License

MIT
