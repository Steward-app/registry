all: dependencies run_dev

dependencies:
	poetry install

test:
	poetry run pytest

run_monolithic:
	poetry run python -m registry.monolithic_server --flagfile=prod.flags $(ARGS) --listen_addr '[::]:50050'

run_dev:
	poetry run python -m registry.monolithic_server --flagfile=dev.flags $(ARGS) --listen_addr '[::]:50050'
