all: dependencies run_dev

dependencies:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest

run_monolithic:
	python3 -m registry.monolithic_server --flagfile=prod.flags $(ARGS) --listen_addr '[::]:50050'

run_dev:
	python3 -m registry.monolithic_server --flagfile=dev.flags $(ARGS) --listen_addr '[::]:50050'
