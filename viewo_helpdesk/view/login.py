# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_login

import viewo_helpdesk.api.auth
import viewo_helpdesk.view


@viewo_helpdesk.view.view_login.route('/admin/login')
def login_show():
    """Route public pages which are visible without any permissions."""
    if flask_login.current_user.get_id() is not None:
        return flask.redirect(flask.url_for('view_admin.messages_list'))
    return flask.render_template('login.html')


@viewo_helpdesk.view.view_login.route('/admin/login', methods=['POST'])
def login_check():
    user = flask.request.form.get('user', None)
    password = flask.request.form.get('password', None)
    if not viewo_helpdesk.api.auth.login(user, password):
        return flask.render_template('login.html')
    return flask.redirect(flask.url_for('view_admin.messages_list'))
