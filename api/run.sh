#!/bin/bash
set -x
export SIMPLE_SETTINGS=settings
exec bash -c "gunicorn --bind ${FLASK_HOST}:${FLASK_PORT} --workers ${WORKERS} app:${FLASK_APP} --log-level ${LOG_LEVEL} --timeout ${TIMEOUT}"


