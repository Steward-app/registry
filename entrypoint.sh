#!/bin/bash

 poetry run python -m registry.${SERVICE:-monolithic}_server $@
