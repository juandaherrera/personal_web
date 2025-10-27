ruff:
	uv run ruff check --fix
	uv run ruff format
install:
	uv sync --all-extras
run:
	uv run reflex run