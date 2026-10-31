#! /usr/bin/bash

export FLASK_APP=admin_helpdesk/__main__.py
export FLASK_ENV=development

python -m flask run --port 5001 &
