#!/usr/bin/env bash
source venv/bin/activate
flask db upgrade
exec gunicorn wsgi -c gunicorn.conf.py