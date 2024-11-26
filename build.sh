#!/usr/bin/env bash
# Render build step: install deps, collect static files, apply migrations.
# Exit on the first error so a broken build fails loudly instead of deploying.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
