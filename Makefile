.PHONY: sync lint format format-check typecheck test build verify clean

sync:
	uv sync --all-extras --dev

lint:
	uv run ruff check .

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

typecheck:
	uv run mypy src tests

test:
	uv run pytest --cov=hermes_autopilot_reliability --cov-report=term-missing --cov-fail-under=90

build:
	uv build

verify: sync lint format-check typecheck test build

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov dist build
