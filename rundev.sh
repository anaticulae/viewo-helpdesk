#! /usr/bin/bash

export VIEWO_HELPDESK="${SHARED_SPACE:-$HOME/.tmp/viewo/viewo_helpdesk}"

export FLASK_APP=viewo_helpdesk/__main__.py
export FLASK_ENV=development

python -m flask run --port 5001 &
