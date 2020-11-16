# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses

import flask_login

import admin_helpdesk.api


@dataclasses.dataclass
class FlaskUser(flask_login.UserMixin):
    identifier: str = None

    def get_id(self):
        return self.identifier


def create_loginmanager(app):
    loginmanager = flask_login.LoginManager()
    loginmanager.login_view = 'admin_helpdesk.api.auth'
    loginmanager.init_app(app)

    loginmanager._user_callback = load_user  # pylint:disable=W0212


def load_user(userid):
    return FlaskUser(identifier=userid)


@admin_helpdesk.api.api_auth.route('/auth')
def login_show():
    return 'LOGIN REQUIRED'
