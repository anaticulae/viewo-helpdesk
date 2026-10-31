#! /usr/bin/bash

export VIEWO_HELPDESK="${SHARED_SPACE:-$HOME/.tmp/viewo/admin_helpdesk}"

export FLASK_APP=admin_helpdesk/__main__.py
export FLASK_ENV=development

python -m flask run --port 5001 &
