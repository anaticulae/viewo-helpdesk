# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import flask_login

import admin_helpdesk.api.auth
import admin_helpdesk.message.collect
import admin_helpdesk.view


@admin_helpdesk.view.view_admin.route('/admin/messages/list')
@flask_login.login_required
def messages_list():
    """Route public pages which are visible without any permissions."""
    dialogs = admin_helpdesk.message.collect.load_dialogs()
    headers = [
        admin_helpdesk.message.collect.load_message(item.userid, item.date)
        for item in dialogs
    ]
    return flask.render_template('admin/index.html', dialogs=headers)


@admin_helpdesk.view.view_admin.route(
    '/admin/messages/reply/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
@flask_login.login_required
def messages_reply(userid: str, date: int):
    messages = admin_helpdesk.message.collect.load_messages(userid, date)
    pass


@admin_helpdesk.view.view_admin.route(
    '/admin/messages/show/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
@flask_login.login_required
def messages_show(userid: str, date: int):
    messages = admin_helpdesk.message.collect.load_messages(userid, date)
    dialog = admin_helpdesk.Dialog(userid, date)
    rendered = flask.render_template(
        'admin/show.html',
        messages=messages,
        dialog=dialog,
    )
    return rendered
