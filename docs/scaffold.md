# Project Scaffold and Best Practices

This project follows a modular, scalable Python structure inspired by best practices for modern development:

- All source code in `src/`
- Tests in `tests/`, mirroring `src/`
- Notebooks for exploration in `notebooks/`
- Docker, GCP, and RPi folders for deployment
- Linting, formatting, and type checking automated via pre-commit and CI
- Dependency management with Poetry and `pyproject.toml`
- Example `.env.example` for environment variables
- Makefile for automation

## Getting Started

1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Activate environment: `poetry shell`
4. Run tests: `make test`
5. Format code: `make format`
6. Lint/type-check: `make lint`

See `/docs/` for detailed guides on each topic.
