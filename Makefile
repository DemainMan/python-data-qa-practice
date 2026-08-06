.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	pytest -v

run:
	python week3_etl.py --api-url "http://example.com" --db-path "data/db.sqlite"

clean:
	rm -rf __pycache__ .pytest_cache
