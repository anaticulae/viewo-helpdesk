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
import utila

import admin_helpdesk
import admin_helpdesk.api


@admin_helpdesk.api.api_message.route('/dialog/add', methods=['POST'])
def message_add() -> str:
    parent = flask.request.form.get('parent', None)
    userid = flask.request.form.get('userid', None)
    date = utila.now()
    title = flask.request.form.get('title', None)
    text = flask.request.form.get('text', None)
    category = flask.request.form.get('category', None)

    new_dialog = parent is None
    admin = flask_login.current_user.is_admin
    if not admin:
        userid = flask_login.current_user.get_id()

    message = admin_helpdesk.Message(
        parent=None if new_dialog else parent,
        userid=userid,
        date=date,
        title=title,
        text=text,
        writer=userid if not admin else None,
        category=category,
    )
    if new_dialog:
        admin_helpdesk.start_conversion(message, current=date)
    else:
        admin_helpdesk.write_message(message, current=date)

    done = {'date': date}
    uri = admin_helpdesk.api_call(f'/dialog/{userid}/{date}')
    dumped = admin_helpdesk.api.dump(done, name='success', uri=uri)
    return dumped
