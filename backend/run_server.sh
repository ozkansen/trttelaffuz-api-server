#!/usr/bin/env sh

gunicorn --pythonpath=api-server -w $(nproc) main:app -b 0.0.0.0:$PORT -k "egg:meinheld#gunicorn_worker" --log-level warning --log-file -
