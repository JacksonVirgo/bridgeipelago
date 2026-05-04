#!/bin/sh
set -e

echo "Generating config from environment variables..."
python generate_config.py

echo "Starting main application..."
exec python bridgeipelago.py
