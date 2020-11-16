# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import time

import flask

import admin_helpdesk
import admin_helpdesk.api.auth
from admin_helpdesk.api import api_auth
from admin_helpdesk.api import api_message


def create(config=None) -> flask.Flask:
    appi = flask.Flask(__name__)
    appi.secret_key = admin_helpdesk.SECRET_KEY

    admin_helpdesk.api.auth.create_loginmanager(appi)

    if config:
        appi.config.update(config)

    appi.register_blueprint(api_auth, url_prefix=admin_helpdesk.API_PREFIX)
    appi.register_blueprint(api_message, url_prefix=admin_helpdesk.API_PREFIX)
    return appi


def now():
    result = int(time.time())
    return result
