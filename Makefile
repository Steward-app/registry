BACKENDS = registry.user_server registry.maintenance_server registry.asset_server registry.schedule_server registry.monolithic_server
BE_ARGS = --flagfile dev.flags

all: dependencies run_monolithic

dependencies:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest

.PHONY: $(BACKENDS) run_monolithic
run_monolithic: registry.monolithic_server

registry.monolithic_server:
	python3 -m $@ $(BE_ARGS) $(ARGS) --listen_addr '[::]:50050'

registry.user_server:
	python3 -m $@ $(BE_ARGS) $(ARGS) --listen_addr '[::]:50051'

registry.maintenance_server:
	python3 -m $@ $(BE_ARGS) $(ARGS) --listen_addr '[::]:50052'

registry.asset_server:
	python3 -m $@ $(BE_ARGS) $(ARGS) --listen_addr '[::]:50053'

registry.schedule_server:
	python3 -m $@ $(BE_ARGS) $(ARGS) --listen_addr '[::]:50054'
