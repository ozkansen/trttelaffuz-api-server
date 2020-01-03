#!/usr/bin/env sh

gunicorn --pythonpath=api-server -w $(nproc) main:app -b 0.0.0.0:5000 -k "egg:meinheld#gunicorn_worker" --log-level warning --log-file -
