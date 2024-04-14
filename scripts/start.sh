#!/bin/bash

pip install mkdocs
pip install mkdocs-material

pip install mkdocs-awesome-pages-plugin
pip install mkdocs-static-i18n

# Get mkdocs command from arguments
mkdocs_command=$1

config="../config/mkdocs.yml" 

echo "Building $config"
mkdocs $mkdocs_command --config-file $config
port=$((port+1))
