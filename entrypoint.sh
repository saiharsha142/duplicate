#!/bin/bash

set -e

python3 /opt/duplicate.py ${VARIABLE_NAME}

exec "$@"
