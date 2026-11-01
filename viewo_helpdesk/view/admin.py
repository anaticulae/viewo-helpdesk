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
import viewo_helpdesk.message.collect
import viewo_helpdesk.view


@viewo_helpdesk.view.view_admin.route('/admin/messages/list')
@flask_login.login_required
def messages_list():
    """Route public pages which are visible without any permissions."""
    dialogs = viewo_helpdesk.message.collect.load_dialogs()
    headers = [
        viewo_helpdesk.message.collect.load_message(item.userid, item.date)
        for item in dialogs
    ]
    return flask.render_template('admin/index.html', dialogs=headers)


@viewo_helpdesk.view.view_admin.route(
    '/admin/messages/reply/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
@flask_login.login_required
def messages_reply(userid: str, date: int):  # pylint:disable=W0612,W0613
    # messages = viewo_helpdesk.message.collect.load_messages(userid, date)
    pass


@viewo_helpdesk.view.view_admin.route(
    '/admin/messages/show/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
@flask_login.login_required
def messages_show(userid: str, date: int):
    messages = viewo_helpdesk.message.collect.load_messages(userid, date)
    dialog = viewo_helpdesk.Dialog(userid, date)
    rendered = flask.render_template(
        'admin/show.html',
        messages=messages,
        dialog=dialog,
    )
    return rendered
