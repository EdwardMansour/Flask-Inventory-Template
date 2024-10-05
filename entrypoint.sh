#!/bin/bash
set -e
sleep 10
flask db upgrade
flask run --host=0.0.0.0 --port=5000