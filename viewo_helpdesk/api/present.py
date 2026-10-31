# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_helpdesk
import viewo_helpdesk.api
import viewo_helpdesk.api.auth


@viewo_helpdesk.api.api_message.route(
    '/dialogs/<string(length=16):userid>',
    methods=['GET'],
)
@viewo_helpdesk.api.valid_user
def dialogs(userid):
    result = viewo_helpdesk.load_dialogs(userid)
    dumped = viewo_helpdesk.api.dump(result, 'dialogs')
    return dumped


@viewo_helpdesk.api.api_message.route('/dialogs', methods=['GET'])
@viewo_helpdesk.api.auth.admin_required
def get_dialog():
    result = viewo_helpdesk.load_dialogs()
    dumped = viewo_helpdesk.api.dump(result, 'dialogs')
    return dumped


@viewo_helpdesk.api.api_message.route(
    '/dialog/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
@viewo_helpdesk.api.valid_user
@viewo_helpdesk.api.valid_dialog
def dialog_get(userid: str, date: int):
    messages = viewo_helpdesk.load_messages(userid, date)
    dumped = viewo_helpdesk.api.dump(messages, 'messages')
    return dumped
