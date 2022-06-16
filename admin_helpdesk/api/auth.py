# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import functools
import http

import flask
import flask_login

import admin_helpdesk.api
import admin_helpdesk.config

NO_ACCESS = 'LOGIN REQUIRED'


@dataclasses.dataclass
class FlaskUser(flask_login.UserMixin):
    identifier: str = None

    def get_id(self):
        return self.identifier

    @property
    def is_admin(self):
        return self.identifier == admin_helpdesk.config.ADMIN_NAME


def create_loginmanager(app):
    loginmanager = flask_login.LoginManager()
    loginmanager.login_view = 'api_auth.show_login'
    loginmanager.init_app(app)

    loginmanager._user_callback = load_user  # pylint:disable=W0212


def verify_password(user: str, password: str) -> bool:
    if user == admin_helpdesk.config.ADMIN_NAME:
        if password == admin_helpdesk.config.ADMIN_PASSWORD:
            return True
    return False


def login(user, password) -> bool:
    if not verify_password(user, password):
        return False
    user = load_user(user)
    flask_login.login_user(user)
    return True


def load_user(userid):
    return FlaskUser(identifier=userid)


@admin_helpdesk.api.api_auth.route('/auth')
def show_login():
    return NO_ACCESS, http.HTTPStatus.UNAUTHORIZED


@admin_helpdesk.api.api_auth.route('/logout')
def logout():
    flask_login.logout_user()
    return 'DONE'


@admin_helpdesk.api.api_auth.route('/auth', methods=['POST'])
def check_login():
    if flask_login.current_user.is_authenticated:
        return 'DONE'

    user = flask.request.form['user']
    password = flask.request.form['password']

    # verify
    if not verify_password(user, password):
        return 'INVALID PASSWORD', http.HTTPStatus.NOT_FOUND

    # login
    login(user, password)
    if flask_login.current_user.is_admin:
        return flask.jsonify({'link': '/admin/messages/list'})
    return 'DONE'


def admin_required(func):

    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        if not flask_login.current_user.is_authenticated:
            return flask.current_app.login_manager.unauthorized()
        if not flask_login.current_user.is_admin:
            return flask.current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return decorated_view
