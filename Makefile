run-pytest := uv run pytest

.PHONY: venv lint test run
venv:
	uv venv --python 3.12
	uv sync --upgrade
lint:
	ruff check --fix
	ruff format
	mypy .
test:
	${run-pytest} --cov=src --cov-report=html
run:
	uv run src/main.py
