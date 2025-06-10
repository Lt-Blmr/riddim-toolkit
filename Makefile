# Sample Makefile for dependency and test automation
requirements.txt: pyproject.toml
	poetry export -f requirements.txt --without-hashes > requirements.txt

test:
	pytest tests/

format:
	black src tests
	isort src tests

lint:
	flake8 src tests
	mypy src
