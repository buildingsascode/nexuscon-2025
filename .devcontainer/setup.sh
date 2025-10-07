#!/usr/bin/env bash

sudo apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && sudo apt-get -y install --no-install-recommends iputils-ping telnet dnsutils netcat-traditional

# Create env directory if it doesn't exist
mkdir -p ./env

# Copy template.env to dev.env if dev.env doesn't exist
if [ -f "./env/dev.env" ]; then
    echo "dev.env file already exists, skipping creation."
else
    cp .devcontainer/template.env ./env/dev.env
fi

# Add source command to .bashrc if not already present
printf "\n# Source development environment variables\nsource /workspaces/nexuscon-2025/env/dev.env\n" >> ~/.bashrc
source ~/.bashrc

# Install Python dependencies
pip install uv
uv venv --clear
uv pip install -r requirements.txt