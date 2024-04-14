#!/bin/bash

pip install mkdocs
pip install mkdocs-material
pip install mkdocs-awesome-pages-plugin

# Get mkdocs command from arguments
mkdocs_command=$1

configs=("../config/de/mkdocs.yml" "../config/en/mkdocs.yml")

port=8000

for config in "${configs[@]}"
do
    echo "Building $config"
    mkdocs $mkdocs_command --config-file $config -a "localhost:$port" &
    port=$((port+1))
done