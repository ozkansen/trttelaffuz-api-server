#!/usr/bin/env sh

gunicorn --pythonpath=api-server -w $(nproc) -e DJANGO_SETTINGS_MODULE=sozluk_api_server.settings sozluk_api_server.wsgi -b 0.0.0.0:8000 -k "egg:meinheld#gunicorn_worker" --log-level warning --log-file -
