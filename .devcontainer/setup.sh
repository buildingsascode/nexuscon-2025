#!/usr/bin/env bash

# Create env directory if it doesn't exist
mkdir -p ./env

# Copy template.env to dev.env if dev.env doesn't exist
if [ -f "./env/dev.env" ]; then
    echo "dev.env file already exists, skipping creation."
else
    cp .devcontainer/template.env ./env/dev.env
fi

# Add source command to .bashrc if not already present
printf "\n# Source development environment variables\nsource ./env/dev.env\n" >> ~/.bashrc
source ~/.bashrc

# Install Python dependencies
pip3 install --user -r requirements.txt