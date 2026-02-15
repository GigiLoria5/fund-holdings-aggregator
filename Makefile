run-pytest := uv run pytest

.PHONY: help install lint test run
help:
	@echo "Portfolio Holdings Aggregator - Available Commands"
	@echo ""
	@echo "  make install    - Install dependencies"
	@echo "  make lint       - Run code linting"
	@echo "  make test       - Run test suite with pytest"
	@echo "  make run        - Run aggregator (requires INPUT var and optionally OUTPUT)"
	@echo ""
	@echo "Examples:"
	@echo "  make run INPUT=holdings.xlsx"
	@echo "  make run INPUT=holdings.xlsx OUTPUT=result.xlsx"
	@echo "  make test"

install:
	uv venv --python 3.12
	uv sync --upgrade

lint:
	ruff check --fix
	ruff format
	mypy .

test:
	${run-pytest} --cov=src --cov-report=html

run:
ifndef INPUT
	$(error INPUT variable required. Usage: make run INPUT=file.xlsx [OUTPUT=result.xlsx])
endif
	uv run src/main.py "$(INPUT)" $(if $(OUTPUT),"$(OUTPUT)")
