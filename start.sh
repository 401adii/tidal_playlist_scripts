FILE="./.env"

if [ ! -f "$FILE" ]; then
    echo ".env file not find, runnnig get_credentials.py"
    uv run get_credentials.py
fi

uv run --env-file .env main.py