#!/usr/bin/env bash

# Set defaults if not provided in environment
: "${MODULE_NAME:=main}"
: "${VARIABLE_NAME:=app}"
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"

# Start uvicorn with live-reload
uvicorn \
    --proxy-headers \
    --host "$HOST" \
    --port "$PORT" \
    "$APP_MODULE"