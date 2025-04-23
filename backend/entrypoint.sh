#!/bin/bash
set -e

mkdir -p /app/static
mkdir -p /app/media
mkdir -p /app/files
mkdir -p /app/data

echo "Applying database migrations..."
cd /app
alembic upgrade head

echo "Collecting static files..."
python -c "
import shutil
import os
from pathlib import Path

static_app = Path('/app/app/static')

static_path = Path('/app/static')

static_path.mkdir(exist_ok=True)

if static_app.exists():
    for item in static_app.iterdir():
        if item.is_file():
            shutil.copy2(item, static_path / item.name)
        elif item.is_dir():
            shutil.copytree(item, static_path / item.name, dirs_exist_ok=True)
    print(f'Static files copied to {static_path}')
else:
    print(f'Warning: Static directory {static_app} does not exist')
"

chmod -R 755 /app/static
chmod -R 755 /app/media
chmod -R 755 /app/files
chmod -R 755 /app/data

exec "$@"