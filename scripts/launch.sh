#!/usr/bin/env bash



python ../main.py createsuperuser --noinput --email anitolqyn@gmail.com --username toqlyn-admin --password tolqyn2023


: "${MODULE_NAME:=main}"
: "${VARIABLE_NAME:=app}"
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"

uvicorn \
    --proxy-headers \
    --host "$HOST" \
    --port "$PORT" \
    "$APP_MODULE"
