install:
	pip install -r requirements.txt

format:
	black src tests
	isort src tests

lint:
	flake8 src tests
	mypy src

test:
	pytest

export-requirements:
	poetry export -f requirements.txt --without-hashes > requirements.txt
