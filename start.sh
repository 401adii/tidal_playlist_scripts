#!/bin/bash

FILE="./.env"

if [ ! -f "$FILE" ]; then
    echo ".env file not found, runnning get_credentials.py"
    uv run get_credentials.py

    if [ ! -f "$FILE" ]; then
        echo "Error: .env file was not created. Exiting."
    fi
fi

uv run --env-file .env main.py "$@"