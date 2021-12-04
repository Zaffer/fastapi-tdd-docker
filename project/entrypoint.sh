#!/bin/sh

# Script to wait for db to start

set -e

echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"