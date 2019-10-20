# You can set these variables from the command line.
NODE_MODULES = static/node_modules
PROTO_OUT = steward
PROTO_IN = proto/steward
PROTO_INCLUDE = proto
BACKENDS = registry.user_server registry.maintenance_server
BE_ARGS = --env dev --logtostderr --db=mongodb://127.0.0.1:27017
FE_PORT = 5000

dependencies:
	sudo pip3 install -r requirements.txt

.PHONY: app proto clean run_backend $(BACKENDS) run_frontend
app:
	cd app; yarn install --modules-folder $(NODE_MODULES)
	cd app; FLASK_APP=__init__.py flask assets build

proto:
	rm -rf $(PROTO_OUT)/*.py
	rm -rf $(PROTO_OUT)/__pycache__
	python3 -m grpc_tools.protoc -I $(PROTO_INCLUDE) --python_out=. --grpc_python_out=. $(PROTO_IN)/*.proto

clean:
	rm  -rf app/$(NODE_MODULES) $(PROTO_OUT)

run_backend: $(BACKENDS)

registry.user_server:
	python3 -m $@ $(BE_ARGS) $(ARGS)

registry.maintenance_server:
	python3 -m $@ $(BE_ARGS) $(ARGS)

run_frontend:
	python3 -c 'from app import app; app.run(host="0.0.0.0", port=$(FE_PORT))'

test:
	python3 -m pytest