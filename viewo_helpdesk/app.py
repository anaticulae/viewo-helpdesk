# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_bootstrap

import viewo_helpdesk
import viewo_helpdesk.api.auth
import viewo_helpdesk.api.post
import viewo_helpdesk.api.present
from viewo_helpdesk.api import api_auth
from viewo_helpdesk.api import api_message
from viewo_helpdesk.view import *  # pylint:disable=wildcard-import
from viewo_helpdesk.view import view_login
from viewo_helpdesk.view import view_user


def create(config=None) -> flask.Flask:
    appi = flask.Flask(__name__)
    appi.secret_key = viewo_helpdesk.SECRET_KEY

    viewo_helpdesk.api.auth.create_loginmanager(appi)

    appi.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
    flask_bootstrap.Bootstrap(app=appi)

    if config:
        appi.config.update(config)

    # view
    appi.register_blueprint(view_admin)
    appi.register_blueprint(view_login)
    appi.register_blueprint(view_user)

    # api
    appi.register_blueprint(api_auth, url_prefix=viewo_helpdesk.API_PREFIX)
    appi.register_blueprint(api_message, url_prefix=viewo_helpdesk.API_PREFIX)

    return appi
