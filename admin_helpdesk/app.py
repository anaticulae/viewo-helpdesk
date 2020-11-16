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

import admin_helpdesk.config
from admin_helpdesk.api import api_message


def create(config=None) -> flask.Flask:
    appi = flask.Flask(__name__)
    appi.secret_key = admin_helpdesk.config.SECRET_KEY

    if config:
        appi.config.update(config)

    url_prefix = admin_helpdesk.config.API_PREFIX
    appi.register_blueprint(api_message, url_prefix=url_prefix)
    return appi


def now():
    result = int(time.time())
    return result
