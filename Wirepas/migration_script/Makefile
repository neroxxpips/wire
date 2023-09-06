SHELL		:= /usr/bin/env bash

help:
	@echo "Possible parameters"
	@echo "clean			Remove JSON with imported data"
	@echo "pkg_requirements"	"Install requirements.txt"
	@echo "export_json		Export data from WNT backend to JSON"
	@echo "import_json		Import data from JSON to WNT backend"

clean:
	rm -rf data*.json
	rm -r .env

pkg_add:
	python3 -m venv .env
	.env/bin/pip3 install $(PKG); \

pkg_delete:
	python3 -m venv .env
	.env/bin/pip3 uninstall $(PKG); \

pkg_requirements:
	python3 -m venv .env
	.env/bin/pip3 install -r requirements.txt \

export_json: pkg_requirements
	.env/bin/python3 anchordataexporter.py \

import_json: pkg_requirements
	.env/bin/python3 anchordataimporter.py \
