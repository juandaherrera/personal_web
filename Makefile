ruff:
	uv run ruff check --fix
	uv run ruff format
install:
	uv sync --all-extras